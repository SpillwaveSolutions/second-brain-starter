#!/usr/bin/env python3
"""Shared second-brain helpers: validate, pack, doctor, write, whoami."""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG_PATH = ROOT / "scripts" / "registry.json"
AGENTS_PATH = ROOT / "agents" / "registry.json"

try:
    import yaml
except ImportError:
    yaml = None


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def slugify(title: str) -> str:
    s = title.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-") or "untitled"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    if yaml:
        meta = yaml.safe_load(parts[1]) or {}
        return meta, parts[2].lstrip("\n")
    return _naive_frontmatter(parts[1]), parts[2].lstrip("\n")


def _naive_frontmatter(block: str) -> dict:
    """Parse the subset of YAML this repo actually writes (scalars + tag lists + link lists)."""
    meta: dict = {}
    i = 0
    lines = block.splitlines()
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if ":" not in line or line.startswith(" ") or line.startswith("\t"):
            i += 1
            continue
        key, raw = line.split(":", 1)
        key = key.strip()
        raw = raw.strip()
        if raw:
            meta[key] = raw.strip('"').strip("'")
            i += 1
            continue
        # block collection
        i += 1
        items: list = []
        current = None
        while i < len(lines) and (lines[i].startswith("  ") or lines[i].startswith("\t") or lines[i].startswith(" -")):
            ln = lines[i]
            stripped = ln.strip()
            if stripped.startswith("- "):
                rest = stripped[2:]
                if ":" in rest:
                    k, v = rest.split(":", 1)
                    current = {k.strip(): v.strip()}
                    items.append(current)
                else:
                    current = None
                    items.append(rest.strip('"').strip("'"))
            elif stripped and ":" in stripped and current is not None:
                k, v = stripped.split(":", 1)
                current[k.strip()] = v.strip()
            i += 1
        meta[key] = items
    return meta


def dump_frontmatter(meta: dict) -> str:
    lines = ["---"]
    for k, v in meta.items():
        if v is None:
            continue
        if isinstance(v, list):
            lines.append(f"{k}:")
            for item in v:
                if isinstance(item, dict):
                    lines.append(f"  - target: {item.get('target', '')}")
                    if item.get("rel"):
                        lines.append(f"    rel: {item['rel']}")
                else:
                    lines.append(f"  - {item}")
        elif isinstance(v, bool):
            lines.append(f"{k}: {'true' if v else 'false'}")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def iter_concepts(bundle: Path) -> list[dict]:
    out = []
    for p in sorted(bundle.rglob("*.md")):
        if p.name == "log.md":
            continue
        text = p.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        rel = "/" + str(p.relative_to(bundle)).replace("\\", "/")
        out.append({"path": rel, "abs": p, "meta": meta or {}, "body": body})
    return out


def cmd_validate(args) -> int:
    bundle = Path(args.bundle)
    registry = load_json(REG_PATH)
    types = registry["types"]
    errors = []
    concepts = iter_concepts(bundle)
    paths = {c["path"] for c in concepts}
    for c in concepts:
        meta = c["meta"]
        typ = meta.get("type")
        if c["path"].endswith("/index.md") or meta.get("okf_version"):
            continue
        if not typ:
            errors.append(f"{c['path']}: missing type")
            continue
        if not meta.get("title"):
            errors.append(f"{c['path']}: missing title")
        spec = types.get(typ)
        if spec is None:
            # Index and other non-registry types are allowed
            if typ not in {"Index", "Catalog"}:
                errors.append(f"{c['path']}: unknown type {typ}")
            continue
        allowed = set(spec.get("rels") or [])
        for link in meta.get("links") or []:
            if not isinstance(link, dict):
                continue
            rel = link.get("rel")
            target = link.get("target", "")
            if rel and rel not in allowed:
                errors.append(f"{c['path']}: rel {rel} not allowed for {typ}")
            if target.startswith("/") and target not in paths:
                # allow missing plugin stub
                if not (bundle / target.lstrip("/")).exists():
                    errors.append(f"{c['path']}: broken link {target}")
    result = {"ok": len(errors) == 0, "concepts": len(concepts), "errors": errors}
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


def cmd_pack(args) -> int:
    bundle = Path(args.bundle)
    concepts = {c["path"]: c for c in iter_concepts(bundle)}
    root = args.root
    if not root.startswith("/"):
        matches = [
            p
            for p, c in concepts.items()
            if c["meta"].get("title", "").lower() == root.lower()
            or p.endswith("/" + root + ".md")
            or p.endswith("/" + slugify(root) + ".md")
        ]
        if not matches:
            print(json.dumps({"error": f"root not found: {root}"}))
            return 1
        root = matches[0]
    hops = int(args.hops)
    max_nodes = int(args.max_nodes)

    def neighbors(path: str):
        c = concepts.get(path)
        if not c:
            return []
        out = []
        for link in c["meta"].get("links") or []:
            if isinstance(link, dict) and link.get("target"):
                out.append(link["target"])
            elif isinstance(link, str):
                out.append(link)
        for m in re.findall(r"\(/[^\)]+\.md\)", c["body"]):
            out.append(m[1:-1])
        return out

    included = []
    frontier = [(root, 0)]
    seen = set()
    while frontier and len(included) < max_nodes:
        node, d = frontier.pop(0)
        if node in seen or node not in concepts:
            continue
        seen.add(node)
        included.append(node)
        if d < hops:
            for n in neighbors(node):
                if n not in seen:
                    frontier.append((n, d + 1))

    header = dump_frontmatter(
        {
            "type": "ContextPack",
            "title": f"Pack: {concepts[root]['meta'].get('title', root)}",
            "status": "generated",
            "timestamp": now_iso(),
            "author": "Laptop: Packer",
            "tags": ["generated", "pack"],
            "links": [{"target": root, "rel": "originates_from"}],
        }
    )
    lines = [
        header.rstrip(),
        "",
        f"# Context pack: {concepts[root]['meta'].get('title', root)}",
        "",
        f"Hops: {hops} | Nodes: {len(included)} | Generated: {now_iso()}",
        "",
        "Outbound BFS. Rank is encounter order from the root.",
        "",
    ]
    for p in included:
        c = concepts[p]
        lines.append(f"## {c['meta'].get('title')} (`{c['meta'].get('type')}`)")
        lines.append(f"Path: `{p}`")
        lines.append(f"Author: {c['meta'].get('author', '')}")
        desc = (c["body"] or "").strip().split("\n")[0][:240]
        lines.append(desc)
        lines.append("")
    out = Path(args.out) if args.out else bundle / "packs" / f"{slugify(concepts[root]['meta'].get('title', 'pack'))}-pack.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"ok": True, "path": str(out), "root": root, "nodes": included}))
    return 0


def cmd_doctor(args) -> int:
    bundle = Path(args.bundle)
    registry = load_json(REG_PATH)
    agents = load_json(AGENTS_PATH)
    concepts = iter_concepts(bundle)
    by_type: dict[str, int] = {}
    by_author: dict[str, int] = {}
    for c in concepts:
        typ = c["meta"].get("type") or "(none)"
        by_type[typ] = by_type.get(typ, 0) + 1
        author = c["meta"].get("author") or "(none)"
        by_author[author] = by_author.get(author, 0) + 1
    missing_catalogs = []
    for folder in registry["catalogs"]:
        if not (bundle / folder).exists():
            missing_catalogs.append(folder)
    report = {
        "ok": True,
        "bundle": str(bundle),
        "concepts": len(concepts),
        "agents": len(agents["agents"]),
        "by_type": dict(sorted(by_type.items())),
        "by_author": dict(sorted(by_author.items())),
        "missing_catalogs": missing_catalogs,
    }
    print(json.dumps(report, indent=2))
    return 0


def cmd_write(args) -> int:
    registry = load_json(REG_PATH)
    spec = registry["types"].get(args.type)
    if not spec:
        print(json.dumps({"error": f"unknown type {args.type}"}))
        return 1
    if args.author:
        agents = load_json(AGENTS_PATH)["agents"]
        allowed_authors = {a["identity"] for a in agents} | {a.get("alias") for a in agents if a.get("alias")}
        owners = [a for a in agents if a["plugin"] == spec["plugin"]]
        owner_ids = {a["identity"] for a in owners} | {a.get("alias") for a in owners if a.get("alias")}
        if args.author not in owner_ids and args.author in allowed_authors:
            print(json.dumps({"error": f"{args.author} may not write {args.type} (owned by {spec['plugin']})"}))
            return 1
    bundle = Path(args.bundle)
    folder = args.folder or spec["folder"]
    slug = args.slug or slugify(args.title)
    path = bundle / folder / f"{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    meta = {
        "type": args.type,
        "title": args.title,
        "status": args.status,
        "timestamp": now_iso(),
        "author": args.author or f"Grok Bot: {spec['plugin']}",
        "tags": [t for t in args.tags.split(",") if t] if args.tags else [],
        "links": [],
    }
    body = args.body or f"# {args.title}\n"
    path.write_text(dump_frontmatter(meta) + "\n" + body.rstrip() + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "path": str(path), "type": args.type, "plugin": spec["plugin"]}))
    return 0


def cmd_whoami(args) -> int:
    agents = load_json(AGENTS_PATH)["agents"]
    if args.identity:
        hits = [a for a in agents if a["identity"] == args.identity or a.get("alias") == args.identity or a["slug"] == args.identity]
        if not hits:
            print(json.dumps({"error": f"unknown identity {args.identity}"}))
            return 1
        print(json.dumps(hits[0], indent=2))
        return 0
    print(json.dumps(agents, indent=2))
    return 0


def cmd_init(args) -> int:
    bundle = Path(args.bundle)
    registry = load_json(REG_PATH)
    bundle.mkdir(parents=True, exist_ok=True)
    idx = bundle / "index.md"
    if not idx.exists():
        idx.write_text(
            dump_frontmatter(
                {
                    "okf_version": "0.2",
                    "title": args.title,
                    "description": args.description or args.title,
                    "timestamp": now_iso(),
                }
            )
            + f"\n# {args.title}\n\nShared second-brain bundle.\n",
            encoding="utf-8",
        )
    for folder in registry["catalogs"]:
        d = bundle / folder
        d.mkdir(parents=True, exist_ok=True)
        cat = d / "index.md"
        if not cat.exists():
            cat.write_text(
                dump_frontmatter({"type": "Index", "title": folder, "timestamp": now_iso()})
                + f"\n# {folder}\n\nCatalog.\n",
                encoding="utf-8",
            )
    print(json.dumps({"ok": True, "bundle": str(bundle), "catalogs": registry["catalogs"]}))
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Shared second-brain CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    i = sub.add_parser("init-bundle")
    i.add_argument("--bundle", default=str(ROOT / "knowledge"))
    i.add_argument("--title", default="Second Brain")
    i.add_argument("--description", default="")

    v = sub.add_parser("validate")
    v.add_argument("--bundle", default=str(ROOT / "knowledge"))

    k = sub.add_parser("pack")
    k.add_argument("--bundle", default=str(ROOT / "knowledge"))
    k.add_argument("--root", required=True)
    k.add_argument("--hops", default="2")
    k.add_argument("--max-nodes", default="20")
    k.add_argument("--out", default="")

    d = sub.add_parser("doctor")
    d.add_argument("--bundle", default=str(ROOT / "knowledge"))

    wri = sub.add_parser("write")
    wri.add_argument("--bundle", default=str(ROOT / "knowledge"))
    wri.add_argument("--type", required=True)
    wri.add_argument("--title", required=True)
    wri.add_argument("--folder", default="")
    wri.add_argument("--slug", default="")
    wri.add_argument("--status", default="active")
    wri.add_argument("--author", default="")
    wri.add_argument("--tags", default="")
    wri.add_argument("--body", default="")

    who = sub.add_parser("whoami")
    who.add_argument("--identity", default="")

    args = p.parse_args()
    return {
        "init-bundle": cmd_init,
        "validate": cmd_validate,
        "pack": cmd_pack,
        "doctor": cmd_doctor,
        "write": cmd_write,
        "whoami": cmd_whoami,
    }[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())

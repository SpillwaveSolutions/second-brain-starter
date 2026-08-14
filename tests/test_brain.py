#!/usr/bin/env python3
"""Validate the shared second-brain sample graph."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRAIN = ROOT / "scripts" / "brain.py"
BUNDLE = ROOT / "knowledge"


def run(args: list[str]) -> dict:
    proc = subprocess.run(
        [sys.executable, str(BRAIN), *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0 and not proc.stdout.strip().startswith("{"):
        raise AssertionError(f"{args} failed:\n{proc.stdout}\n{proc.stderr}")
    return json.loads(proc.stdout)


def test_validate():
    result = run(["validate", "--bundle", str(BUNDLE)])
    assert result["ok"], result
    assert result["concepts"] >= 20, result


def test_pack_article_crosses_domains():
    result = run(
        [
            "pack",
            "--bundle",
            str(BUNDLE),
            "--root",
            "The work is happening you just cannot see it",
            "--hops",
            "2",
            "--max-nodes",
            "20",
        ]
    )
    assert result["ok"], result
    joined = " ".join(result["nodes"])
    assert "articles/the-work-is-happening.md" in joined
    assert "offers/shared-ai-engineering-sprint.md" in joined or "series/visible-work.md" in joined
    assert len(result["nodes"]) >= 4


def test_whoami_articles():
    result = run(["whoami", "--identity", "Grok Bot: Articles"])
    assert result["plugin"] == "content-media"
    assert "Article" in result["writes"]


def test_write_rejects_cross_plugin_author():
    result = run(
        [
            "write",
            "--bundle",
            str(BUNDLE),
            "--type",
            "Article",
            "--title",
            "Should Fail Cross Write",
            "--author",
            "Grok Bot: Sales",
        ]
    )
    assert "error" in result


def test_doctor():
    result = run(["doctor", "--bundle", str(BUNDLE)])
    assert result["concepts"] >= 20
    assert result["agents"] >= 8


def main() -> int:
    tests = [
        test_validate,
        test_pack_article_crosses_domains,
        test_whoami_articles,
        test_write_rejects_cross_plugin_author,
        test_doctor,
    ]
    failed = 0
    for fn in tests:
        try:
            fn()
            print(f"ok  {fn.__name__}")
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"FAIL {fn.__name__}: {exc}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

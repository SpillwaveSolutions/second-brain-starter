#!/usr/bin/env python3
"""Validate the shared second-brain sample graph."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
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


def test_whoami_unclaimed_does_not_invent_a_name():
    result = run(["whoami", "--bundle", str(BUNDLE)])
    # Sample tree has no claimed identity unless a previous test wrote one.
    # Clear first so this is deterministic.
    run(["whoami", "--clear", "--bundle", str(BUNDLE)])
    result = run(["whoami", "--bundle", str(BUNDLE)])
    assert result["claimed"] is False
    assert result["identity"] == ""
    assert "Ask the user" in result["hint"]


def test_whoami_claim_and_write_uses_it():
    tmp = Path(tempfile.mkdtemp())
    bundle = tmp / "knowledge"
    bundle.mkdir()
    try:
        claim = run(["whoami", "--claim", "Maya", "--plugin", "content-media", "--bundle", str(bundle)])
        assert claim["claimed"] is True
        assert claim["identity"] == "Maya"
        shown = run(["whoami", "--bundle", str(bundle)])
        assert shown["identity"] == "Maya"
        written = run(
            [
                "write",
                "--bundle",
                str(bundle),
                "--type",
                "Draft",
                "--title",
                "Claimed Author Draft",
            ]
        )
        assert written.get("ok"), written
        text = (bundle / "drafts" / "claimed-author-draft.md").read_text(encoding="utf-8")
        assert "author: Maya" in text
    finally:
        shutil.rmtree(tmp)


def test_write_requires_identity():
    tmp = Path(tempfile.mkdtemp())
    bundle = tmp / "knowledge"
    bundle.mkdir()
    try:
        result = run(
            [
                "write",
                "--bundle",
                str(bundle),
                "--type",
                "Draft",
                "--title",
                "No Identity",
            ]
        )
        assert "error" in result
        assert "no identity" in result["error"]
    finally:
        shutil.rmtree(tmp)



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
        test_whoami_unclaimed_does_not_invent_a_name,
        test_whoami_claim_and_write_uses_it,
        test_write_requires_identity,
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

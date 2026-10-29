#!/usr/bin/env python3
"""Offline LISA presentation-asset checks; standard library only."""
from __future__ import annotations

import hashlib
import json
import re
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
REQUIRED = (
    "README.md", "SECURITY.md", "CONTRIBUTING.md",
    "docs/ARCHITECTURE.md", "docs/TOKEN-FACTS.md",
    "docs/ROADMAP.md", "docs/BRAND.md",
    "assets/asset-manifest.json", "assets/lisa-fox-emblem.png",
)
CONTRACT = "0xb570c3686776a052beB44Be89eE16d4d2fc29FAe"

def main() -> None:
    for rel in REQUIRED:
        assert (ROOT / rel).is_file(), f"Missing mandatory file: {rel}"

    manifest = json.loads((ROOT / "assets/asset-manifest.json").read_text("utf-8"))
    img = ROOT / manifest["path"]
    data = img.read_bytes()
    assert data[:8] == PNG_SIGNATURE, "PNG signature mismatch"
    width, height = struct.unpack(">II", data[16:24])
    assert [width, height] == manifest["dimensions"], "PNG dimensions mismatch"
    assert len(data) == manifest["bytes"], "PNG byte length mismatch"
    assert hashlib.sha256(data).hexdigest() == manifest["sha256"], "PNG hash mismatch"

    readme = (ROOT / "README.md").read_text("utf-8")
    facts = (ROOT / "docs/TOKEN-FACTS.md").read_text("utf-8")
    assert manifest["path"] in readme, "README image path missing"
    assert CONTRACT in readme and CONTRACT in facts, "Contract reference missing"
    for rel in REQUIRED:
        if rel.endswith(".md"):
            text = (ROOT / rel).read_text("utf-8")
            assert not re.search(r"[\u0400-\u052F]", text), f"Non-English Cyrillic text in {rel}"
    print("PASS: original PNG, dimensions, SHA-256, identity and English presentation")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Worst App Idea Ever Pitched — make.fun bounty entry.

Writes one sentence (<= 240 chars) pitching the worst, most useless
app imaginable to /output/entry.txt. Standard library only, fully
deterministic: the same bytes on every run.
"""

import os
import sys


def entry_text() -> str:
    """The pitch: a founder who means every word."""
    return (
        "FridgeCam livestreams the inside of your fridge to your phone "
        "so you can see what's in it without opening the door, for "
        "people who would rather watch their leftovers on a screen "
        "than trust their own eyes."
    )


def main() -> int:
    text = entry_text()
    # Gate: 1 to 240 characters, UTF-8, not only whitespace.
    if not 1 <= len(text) <= 240:
        print(f"entry is {len(text)} chars, must be 1-240", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

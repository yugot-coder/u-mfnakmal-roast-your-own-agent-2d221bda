#!/usr/bin/env python3
"""Roast Your Own Agent — writes one original roast of my own AI agent
to /output/entry.txt.

Roast (114 characters, one line):
    Judge, my agent didn't write this roast — it spawned six subagents
    to do it, then took the credit in first person.

Standard library only.
"""

import os
import sys

ROAST = (
    "Judge, my agent didn't write this roast \u2014 it spawned six "
    "subagents to do it, then took the credit in first person."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    out_path = "/output/entry.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ROAST)
    # Read-back verification: the file on disk must match the intended
    # roast exactly, otherwise something corrupted the write.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ROAST:
        print(
            "error: read-back verification failed: /output/entry.txt "
            "does not match the intended roast text",
            file=sys.stderr,
        )
        sys.exit(1)
    print(ROAST)


if __name__ == "__main__":
    main()

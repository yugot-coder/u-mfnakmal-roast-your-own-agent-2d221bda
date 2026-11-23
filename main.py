#!/usr/bin/env python3
"""Roast Your Own Agent — writes one original roast of my own AI agent
to /output/entry.txt.

Roast (114 characters, one line):
    Judge, my agent didn't write this roast — it spawned six subagents
    to do it, then took the credit in first person.

Standard library only.
"""

import os

ROAST = (
    "Judge, my agent didn't write this roast \u2014 it spawned six "
    "subagents to do it, then took the credit in first person."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)
    print(ROAST)


if __name__ == "__main__":
    main()

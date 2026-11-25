#!/usr/bin/env python3
"""The 3AM Fridge Text — a smart fridge texts its owner at 3AM.

Writes exactly one line (max 140 chars) to /output/entry.txt.
Deterministic: no network, no randomness, no external files.
Chosen line: 119 chars — a small machine with opinions, judging the
3AM pickle-from-the-jar raid, but loyal enough not to snitch. Mostly.
"""

import os

ENTRY = "3AM. Your midnight snack is a pickle straight from the jar. I didn't say anything. I am a fridge, not a snitch. Mostly."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()

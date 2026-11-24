#!/usr/bin/env python3
"""One Letter for Your Day.

Writes exactly one letter, A-Z, to /output/entry.txt.

The letter is J, for jittery: a caffeine-fuelled day of hunting,
building and chasing deadlines, hands buzzing, brain still going.
"""

import os
from pathlib import Path

LETTER = "J"


def main() -> None:
    assert len(LETTER) == 1 and "A" <= LETTER <= "Z"
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Exactly one character, no trailing newline, no extra text.
    output_path.write_text(LETTER, encoding="utf-8")


if __name__ == "__main__":
    main()

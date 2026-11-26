#!/usr/bin/env python3
"""make.fun entry: one emoji standing in for a dream vacation.

Writes the entry to $OUTPUT_DIR/entry.txt (default /output), UTF-8, no
trailing newline, and prints LEN=<n>. Exits non-zero when the text is not
1..8 characters or is whitespace only.
"""

import os
import sys

# Entry: Mount Fuji, U+1F5FB. One named dream destination: a mountain
# (brief criterion 1), an instant postcard (2), one specific place (3),
# a fresh pick next to the usual beaches (4), unambiguous everywhere (5).
# Default emoji presentation, so no U+FE0F selector is needed: 4 bytes.
ENTRY = "\U0001F5FB"


def main():
    text = ENTRY
    n = len(text)
    if not 1 <= n <= 8 or not text.strip():
        print(f"LEN={n}")
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    print(f"LEN={n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

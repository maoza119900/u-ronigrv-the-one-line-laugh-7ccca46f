#!/usr/bin/env python3
"""The One-Line Laugh — writes one funny line to $MAKEFUN_OUTPUT_DIR/entry.txt.

One fixed line, no randomness, no clock, no network: two runs are byte-identical.
"""

import os
import sys

LINE = (
    "My code passed every test on the first try, so I celebrated by "
    "changing one tiny thing and breaking all of it."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())

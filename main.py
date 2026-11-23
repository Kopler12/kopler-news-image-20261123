#!/usr/bin/env python3
"""Entry program for news-image-20261123.

Copies the bundled front-page image to the output directory as
entry.png. Standard library only, no network, deterministic.
"""

import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Verify the copy landed whole before reporting success.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit("entry.png copy incomplete")
    print("wrote", dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())

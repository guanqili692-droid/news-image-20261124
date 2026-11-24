"""news-image-20261124 entry (Python 3.13, standard library only).

The image is the entry.png beside this file. The program copies it,
byte for byte, to /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png
outside the grader). No network, no randomness, no other input, so
every run writes identical bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT = OUT_DIR / "entry.png"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()

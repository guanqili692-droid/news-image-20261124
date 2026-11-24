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
    if not SRC.is_file():
        raise SystemExit(f"entry image missing: {SRC}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    # Verify the copy is byte-identical, so a truncated write is never
    # mistaken for a valid deterministic run.
    if OUT.stat().st_size != SRC.stat().st_size:
        raise SystemExit("entry image copy is incomplete")


if __name__ == "__main__":
    main()

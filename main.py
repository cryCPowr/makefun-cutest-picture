# Cutest picture entry for make.fun bounty cutest-picture-01.
# The picture is the entry.png beside this file; the program copies it
# to /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png for local runs).
# Standard library only, no network, no clock: two runs write identical bytes.

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT_DIR.mkdir(parents=True, exist_ok=True)
SRC = HERE / "entry.png"

# Fail loudly if the bundled picture is not a whole PNG.
if SRC.read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
    raise SystemExit("entry.png is not a PNG file")

shutil.copyfile(SRC, OUT_DIR / "entry.png")

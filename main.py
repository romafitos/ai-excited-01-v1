"""Whale Through Glass - ai-excited-01 entry.

Copies the champion image to the output path as entry.png.
The bytes are JPEG (the gate accepts JPEG bytes under the entry.png
name, per RULES.txt); a plain copy keeps them byte-identical.
"""

import os
import shutil


def main():
    # Byte copy only: no re-encoding, no resize, so the output hash
    # always matches the champion image hash.
    src = os.path.join(os.path.dirname(__file__), "entry.jpg")
    dst = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")
    shutil.copy(src, dst)


if __name__ == "__main__":
    main()

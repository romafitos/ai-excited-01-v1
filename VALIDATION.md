# Validation — ai-excited-01 round 1 (independent check, 2026-11-16)

Checked in ~/workspace/kreatif/ai-excited-01-v1 at commit e96fee0:
- LICENSE, README.md, main.py, entry.jpg all present; LICENSE is MIT.
- entry.jpg: JPEG, 1024x1024, 328,428 bytes.
  sha256: 8d1364122d9a244e819e40b2176c66371224a51fe08f421ac6b30f152e050757
- Ran main.py twice (Python 3.12.3, stdlib only: os + shutil, plain byte copy),
  each time with MAKEFUN_OUTPUT_DIR pointed at a fresh dir under /tmp.
  Both runs wrote entry.png, 328,428 bytes, well under the 1,048,576-byte cap.
- Run 1 sha256: 8d1364122d9a244e819e40b2176c66371224a51fe08f421ac6b30f152e050757
- Run 2 sha256: 8d1364122d9a244e819e40b2176c66371224a51fe08f421ac6b30f152e050757
- cmp confirmed the two outputs are byte-identical, and both match entry.jpg.

Verdict: PASS. Output is deterministic and within the size cap.

# Whale Through Glass — ai-excited-01

A colossal blue whale breaches impossibly through the glass facade of
a skyscraper at golden dusk, frozen mid-leap while shards and spray
hang in the air and the city skyline glows below.

The image is a single frozen peak instant: impossible scale, a
wrong-place twist (an ocean animal inside a glass tower, not the sea),
and a diagonal breach that drives the eye across the whole frame.
No text, no stock explosion — just one huge whale silhouette with a
bright sunset rim light, legible even at thumbnail size.

## How it runs

`main.py` (Python 3.13, standard library only) copies `entry.jpg` to
`$MAKEFUN_OUTPUT_DIR/entry.png`. The bytes are JPEG; the gate accepts
JPEG bytes under the `entry.png` name. A plain copy means the output
is byte-identical on every run — no re-encoding, no resize, so the
1024x1024 image stays well under the 1 MiB cap.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

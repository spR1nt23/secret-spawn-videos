#!/usr/bin/env bash
# Secret Spawn - one-time setup on a clean Linux (Ubuntu/Debian) cloud machine.
#   bash tools/setup.sh            # installs deps + downloads model/fonts into ./assets
#   SS_ASSETS=/some/dir bash tools/setup.sh
# Needs network access to: pypi, npm registry, github.com (release downloads).
set -euo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
ASSETS="${SS_ASSETS:-$REPO/assets}"
mkdir -p "$ASSETS"

echo "== 1/4 system packages (ffmpeg, node/npm for fonts)"
need_apt=()
command -v ffmpeg >/dev/null || need_apt+=(ffmpeg)
command -v npm    >/dev/null || need_apt+=(npm)
command -v curl   >/dev/null || need_apt+=(curl)
if [ ${#need_apt[@]} -gt 0 ]; then
  SUDO=""; [ "$(id -u)" -ne 0 ] && SUDO="sudo"
  $SUDO apt-get update -y && $SUDO apt-get install -y "${need_apt[@]}" libsndfile1
fi

echo "== 2/4 python packages"
PIP="python3 -m pip install -q"
$PIP kokoro-onnx soundfile pillow numpy fonttools brotli 2>/dev/null \
  || $PIP --break-system-packages kokoro-onnx soundfile pillow numpy fonttools brotli

echo "== 3/4 Kokoro TTS model (GitHub release, ~120 MB)"
BASE=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
for f in kokoro-v1.0.int8.onnx voices-v1.0.bin; do
  if [ ! -s "$ASSETS/$f" ]; then
    curl -fL --retry 3 -o "$ASSETS/$f.part" "$BASE/$f" && mv "$ASSETS/$f.part" "$ASSETS/$f"
  fi
done

echo "== 4/4 fonts (Bebas Neue + Lilita One from npm @fontsource, woff -> ttf)"
if [ ! -s "$ASSETS/BebasNeue.ttf" ] || [ ! -s "$ASSETS/LilitaOne.ttf" ]; then
  TMP="$(mktemp -d)"
  ( cd "$TMP" && npm pack @fontsource/bebas-neue @fontsource/lilita-one --silent >/dev/null \
      && mkdir bebas lilita \
      && tar xzf fontsource-bebas-neue-*.tgz -C bebas \
      && tar xzf fontsource-lilita-one-*.tgz -C lilita )
  python3 - "$TMP" "$ASSETS" <<'EOF'
import sys
from fontTools.ttLib import TTFont
tmp, out = sys.argv[1], sys.argv[2]
for src, dst in [(f'{tmp}/bebas/package/files/bebas-neue-latin-400-normal.woff', f'{out}/BebasNeue.ttf'),
                 (f'{tmp}/lilita/package/files/lilita-one-latin-400-normal.woff', f'{out}/LilitaOne.ttf')]:
    f = TTFont(src); f.flavor = None; f.save(dst); print('font ->', dst)
EOF
  rm -rf "$TMP"
fi

python3 - "$ASSETS" <<'EOF'
import sys, os
a = sys.argv[1]
for f in ['kokoro-v1.0.int8.onnx', 'voices-v1.0.bin', 'BebasNeue.ttf', 'LilitaOne.ttf']:
    p = os.path.join(a, f); print(f'{f:28s}', 'OK' if os.path.getsize(p) > 1000 else 'MISSING', os.path.getsize(p))
import kokoro_onnx, soundfile, PIL, numpy  # noqa
print('python deps OK')
EOF
ffmpeg -version | head -1
echo "Setup done. Assets in: $ASSETS"

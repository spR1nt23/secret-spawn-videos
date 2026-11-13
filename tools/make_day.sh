#!/usr/bin/env bash
# Build one full day (3 Shorts + 1 long + thumbnails + upload manifest) from a content file.
#   bash tools/make_day.sh content/2026-11-14.py            # everything
#   bash tools/make_day.sh content/2026-11-14.py short1     # only some targets (short1 short2 short3 long)
# Output: work/<DATE>/out (intermediate) and work/<DATE>/final (mp4, png, upload_manifest.json)
# Long TTS+render takes ~10-15 min on a small CPU box: run with nohup if your tool has a timeout.
set -euo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
CONTENT_FILE="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"; shift
DAY="$(basename "$CONTENT_FILE" .py)"
TARGETS=("$@"); [ ${#TARGETS[@]} -eq 0 ] && TARGETS=(short1 short2 short3 long)
export CONTENT="$CONTENT_FILE"
export OUTDIR="${OUTDIR:-$REPO/work/$DAY/out}"
export FINALDIR="${FINALDIR:-$REPO/work/$DAY/final}"
mkdir -p "$OUTDIR" "$FINALDIR"
T="$REPO/tools"
SHORTS=(); LONG=0
for t in "${TARGETS[@]}"; do [ "$t" = long ] && LONG=1 || SHORTS+=("$t"); done

if [ ${#SHORTS[@]} -gt 0 ]; then
  echo "== TTS shorts (am_michael, speed 1.12)"
  python3 "$T/tts.py" am_michael 1.12 --shorts-only
fi
if [ $LONG -eq 1 ]; then
  echo "== TTS long (am_michael, speed 1.02)"
  python3 "$T/tts.py" am_michael 1.02 --long-only
fi

echo "== frame check sheets"
python3 "$T/check_frames.py" "${TARGETS[@]}"

echo "== render + mux"
for t in "${TARGETS[@]}"; do
  python3 "$T/render.py" "$t"
  FILE="$(python3 -c "import sys; sys.path.insert(0,'$T'); from common import load_content; c=load_content(); print(getattr(c,'UPLOAD',{}).get('$t',{}).get('file','$t'))")"
  python3 "$T/mux.py" "$t" "$FILE"
done

echo "== thumbnails"
if [ $LONG -eq 1 ]; then python3 "$T/thumbnail.py" long; fi
[ ${#SHORTS[@]} -gt 0 ] && python3 "$T/thumbnail.py" "${SHORTS[@]}"

echo "== upload manifest + durations"
python3 - <<EOF
import json, os, subprocess, sys
sys.path.insert(0, "$T")
from common import load_content, FINALDIR
c = load_content(); up = getattr(c, 'UPLOAD', {})
man = {}
for k, v in up.items():
    p = os.path.join(FINALDIR, v.get('file', k) + '.mp4')
    if os.path.exists(p):
        d = float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p]).decode())
        v = dict(v, path=p, duration_s=round(d, 1))
    man[k] = v
json.dump(man, open(os.path.join(FINALDIR, 'upload_manifest.json'), 'w'), indent=2, ensure_ascii=False)
for k, v in man.items(): print(f"{k:7s} {v.get('duration_s','-'):>6} s  {v.get('schedule_ist','')}  {v.get('title','')}")
EOF
echo "Done -> $FINALDIR"

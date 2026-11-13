import re, json, sys, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
import os
from common import load_content, KOKORO_MODEL, KOKORO_VOICES, OUTDIR
_C = load_content()
SHORTS, LONG = _C.SHORTS, _C.LONG

VOICE = sys.argv[1] if len(sys.argv) > 1 else "am_michael"
SPEED = float(sys.argv[2]) if len(sys.argv) > 2 else 1.12
k = Kokoro(KOKORO_MODEL, KOKORO_VOICES)
SR = 24000
OUTD = OUTDIR
GAP = 0.10      # between sentences
SCENE_TAIL = 0.30

def spoken(t):
    t = t.replace('*', '')
    t = re.sub(r'\bEXP\b', 'E X P', t)
    t = re.sub(r'\bRNG\b', 'R N G', t)
    return t

def trim(a, thr=0.012):
    idx = np.where(np.abs(a) > thr)[0]
    if len(idx) == 0: return a
    s = max(idx[0] - int(0.02 * SR), 0); e = min(idx[-1] + int(0.06 * SR), len(a))
    return a[s:e]

def words_of(sentence):
    out = []
    for w in sentence.split():
        hi = '*' in w
        out.append({"w": w.replace('*', ''), "hi": hi})
    return out

def weight(w):
    x = len(re.sub(r'[^A-Za-z0-9]', '', w)) + 2.5
    if w.endswith(','): x += 3
    if w[-1:] in '.?!:': x += 5
    return x

def build(name, scenes):
    audio = []; t = 0.0; timeline = []
    for sc in scenes:
        start = t; words = []
        sents = re.split(r'(?<=[.?!])\s+', sc["vo"].strip())
        for s in sents:
            if not s: continue
            a, sr = k.create(spoken(s), voice=VOICE, speed=SPEED, lang='en-us')
            a = trim(a)
            dur = len(a) / SR
            ws = words_of(s); tot = sum(weight(x["w"]) for x in ws); acc = 0.0
            for x in ws:
                x["t"] = round(t + dur * acc / tot, 3); acc += weight(x["w"])
            words += ws
            audio.append(a); t += dur
            audio.append(np.zeros(int(GAP * SR), dtype=np.float32)); t += GAP
        audio.append(np.zeros(int(SCENE_TAIL * SR), dtype=np.float32)); t += SCENE_TAIL
        timeline.append({"start": round(start, 3), "end": round(t, 3), "words": words})
    a = np.concatenate(audio).astype(np.float32)
    a = a / max(1e-6, np.abs(a).max()) * 0.89
    sf.write(f'{OUTD}/{name}.wav', a, SR)
    json.dump(timeline, open(f'{OUTD}/{name}.json', 'w'))
    print(name, round(t, 2), 's')

os.makedirs(OUTD, exist_ok=True)
if "--long-only" not in sys.argv:
    for n, v in SHORTS.items(): build(n, v["scenes"])
if "--shorts-only" not in sys.argv:
    build('long', LONG["scenes"])

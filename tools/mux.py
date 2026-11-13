import os
import json, sys, subprocess, numpy as np, soundfile as sf
SR = 24000
from common import OUTDIR as OUT, FINALDIR as FINAL


def whoosh(dur=0.38, seed=0):
    rng = np.random.default_rng(seed)
    n = int(dur * SR)
    x = rng.standard_normal(n)
    # simple time-varying low-pass via moving average with shrinking window -> rising sweep
    y = np.zeros(n)
    acc = 0.0
    for i in range(n):
        k = 0.02 + 0.5 * (i / n) ** 2
        acc += k * (x[i] - acc)
        y[i] = acc
    env = np.sin(np.pi * np.linspace(0, 1, n)) ** 2
    y = y * env
    return (y / np.abs(y).max()).astype(np.float32)


def build(name, title):
    v, sr = sf.read(f'{OUT}/{name}.wav', dtype='float32')
    tl = json.load(open(f'{OUT}/{name}.json'))
    w = whoosh()
    mix = np.concatenate([v, np.zeros(int(0.2 * SR), dtype=np.float32)])
    for i, sc in enumerate(tl[1:], 1):
        s = int(max(0, sc['start'] - 0.18) * SR)
        e = min(len(mix), s + len(w))
        mix[s:e] += w[:e - s] * 0.13
    mix = mix / max(1.0, np.abs(mix).max() / 0.95)
    sf.write(f'{OUT}/{name}_mix.wav', mix, SR)
    dst = f'{FINAL}/{title}.mp4'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{OUT}/{name}_video.mp4', '-i', f'{OUT}/{name}_mix.wav',
                    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
                    '-af', 'loudnorm=I=-14:TP=-1.0:LRA=11', '-shortest', '-movflags', '+faststart', dst], check=True)
    print(dst)


if __name__ == '__main__':
    import os; os.makedirs(FINAL, exist_ok=True)
    build(sys.argv[1], sys.argv[2])

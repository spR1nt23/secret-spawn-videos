"""Kapak / thumbnail generator (same visual style as the videos).

  CONTENT=content/2026-11-14.py python3 tools/thumbnail.py            -> FINALDIR/<long name>_thumb.png (1280x720)
  CONTENT=... python3 tools/thumbnail.py short1 short2 short3          -> FINALDIR/<short name>_cover.png (1080x1920)

Long thumbnail: big two-line headline + up to 3 icons from the first item scenes.
Headline comes from LONG['thumb'] = [("LINE 1", "white"), ("LINE 2", "yellow")] if present,
otherwise from the intro scene's 'lines'.
Short cover: the short's title_lines + first item icon (useful as a Shorts cover frame reference;
YouTube web Studio may not allow custom Shorts thumbnails).
Note: custom thumbnails for long videos need a phone-verified channel; if Studio's
"Upload file" thumbnail button is disabled, skip uploading the thumbnail.
"""
import os, sys, json
from PIL import Image, ImageDraw
import render as R
from common import FINALDIR
from palette import PAL, ACC

os.makedirs(FINALDIR, exist_ok=True)


def names():
    up = getattr(R._C, 'UPLOAD', {})
    return {k: v.get('file', k) for k, v in up.items()}


def bg(W, H, pal):
    im = R.gradient(W, H, *PAL[pal])
    im.alpha_composite(R.stripes(W, H).crop((0, 0, W, H)))
    for p in R.particles(W, H, n=40, seed=3):
        im.alpha_composite(R.dot(p['r'], p['a']), (int(p['x']), int(p['y'])))
    return im


def long_thumb():
    W, H = 1280, 720
    sc0 = R.LONG['scenes'][0]
    lines = R.LONG.get('thumb') or sc0.get('lines') or [("ROBLOX NEWS", "white"), ("TODAY", "yellow")]
    im = bg(W, H, sc0.get('bg', 'purple'))
    items = [s for s in R.LONG['scenes'] if s['type'] == 'item'][:3]
    # icons on the right
    for i, s in enumerate(items):
        ic = R.ICONS[s['icon']](250 if i == 0 else 190)
        pos = [(930, 250), (1120, 120), (1110, 470)][i]
        im.alpha_composite(ic, (int(pos[0] - ic.width / 2), int(pos[1] - ic.height / 2)))
    head = R.stack_lines(lines, 150, 9, lh=0.9)
    if head.width > 760:
        k = 760 / head.width
        head = head.resize((int(head.width * k), int(head.height * k)), Image.LANCZOS)
    im.alpha_composite(head, (60, int(H / 2 - head.height / 2 + 30)))
    hdr = R.header(False)
    im.alpha_composite(hdr, (40, 34))
    tag = sc0.get('tag')
    if tag:
        t = R.tilt_badge(tag, 46, R.RED)
        im.alpha_composite(t, (60, H - t.height - 40))
    return im.convert('RGB')


def short_cover(name):
    W, H = 1080, 1920
    sh = R.SHORTS[name]
    im = bg(W, H, sh['scenes'][0].get('bg', 'purple'))
    item = next((s for s in sh['scenes'] if s['type'] == 'item'), None)
    if item:
        ic = R.ICONS[item['icon']](560)
        im.alpha_composite(ic, (int(W / 2 - ic.width / 2), 1180))
    head = R.stack_lines(sh['title_lines'], 200, 10, lh=0.9)
    if head.width > 980:
        k = 980 / head.width
        head = head.resize((int(head.width * k), int(head.height * k)), Image.LANCZOS)
    im.alpha_composite(head, (int(W / 2 - head.width / 2), 560))
    if sh.get('tag'):
        t = R.tilt_badge(sh['tag'], 64, R.RED)
        im.alpha_composite(t, (int(W / 2 - t.width / 2), 560 + head.height + 40))
    im.alpha_composite(R.header(True), (48, 120))
    return im.convert('RGB')


if __name__ == '__main__':
    nm = names()
    targets = sys.argv[1:] or ['long']
    for t in targets:
        if t == 'long':
            dst = os.path.join(FINALDIR, nm.get('long', 'long') + '_thumb.png')
            long_thumb().save(dst)
        else:
            dst = os.path.join(FINALDIR, nm.get(t, t) + '_cover.png')
            short_cover(t).save(dst)
        print(dst)

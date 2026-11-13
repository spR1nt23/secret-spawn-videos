"""Kare kontrolü (frame QA).

Usage:
  python3 tools/check_frames.py NAME [NAME ...]

For each NAME (short1/short2/short3/long) it renders preview frames for every scene
(1.6 s after the scene starts and 0.4 s before it ends) WITHOUT encoding the video,
then builds one contact sheet per NAME: OUTDIR/sheet_<NAME>.jpg

Open the sheet(s) and check, scene by scene:
  - no text runs off the frame or overlaps the header / caption strip / icon
  - titles wrap into 1-2 balanced lines (no single orphan word)
  - code boxes show the exact code (case matters to the reader), badges are short
  - captions show highlighted (accent-coloured) keywords
  - no Roblox logo, character or game footage anywhere (only our own flat icons)
Also run after the final mux on the finished mp4:
  ffmpeg -v error -ss 5 -i FINAL.mp4 -frames:v 1 check.jpg
"""
import os, sys, json, glob
from PIL import Image
import render as R
from common import OUTDIR

for name in sys.argv[1:]:
    for f in glob.glob(f'{OUTDIR}/prev_{name}_*.jpg'):
        os.remove(f)
    tl = json.load(open(f'{OUTDIR}/{name}.json'))
    fr = set()
    for st in tl:
        fr.add(int((st['start'] + 1.6) * R.FPS)); fr.add(int((st['end'] - 0.4) * R.FPS))
    R.render(name, fr)
    files = sorted(glob.glob(f'{OUTDIR}/prev_{name}_*.jpg'))
    ims = [Image.open(f) for f in files]
    short = name.startswith('short')
    tw = 270 if short else 480
    th = int(tw * ims[0].height / ims[0].width)
    cols = 6 if short else 4
    rows = (len(ims) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * tw, rows * th), (0, 0, 0))
    for i, im in enumerate(ims):
        sheet.paste(im.resize((tw, th)), ((i % cols) * tw, (i // cols) * th))
    dst = f'{OUTDIR}/sheet_{name}.jpg'
    sheet.save(dst, quality=85)
    print(dst, len(ims), 'frames')

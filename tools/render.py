import json, math, random, subprocess, sys, os
from functools import lru_cache
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from common import load_content, BEBAS, LILITA, OUTDIR
from palette import PAL, ACC
_C = load_content()
SHORTS, LONG = _C.SHORTS, _C.LONG
from icons import ICONS, OUT

FPS = 30
DARK = (27, 24, 44)
WHITE = (255, 255, 255)
RED = (230, 40, 56)
os.makedirs(OUTDIR, exist_ok=True)


@lru_cache(None)
def F(path, size):
    return ImageFont.truetype(path, size)


def acc(name):
    return WHITE if name == 'white' else ACC[name]


# ---------- primitives ----------
def text_img(txt, font, fill, stroke=0, stroke_fill=(0, 0, 0), pad=None):
    pad = pad if pad is not None else stroke + 4
    d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
    l, t, r, b = d0.textbbox((0, 0), txt, font=font, stroke_width=stroke)
    asc, desc = font.getmetrics()
    w = r - l + pad * 2
    h = asc + desc + stroke * 2 + pad * 2
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((pad - l, pad + stroke), txt, font=font, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)
    return im


def crop_alpha(im, pad=2):
    bb = im.getbbox()
    if not bb: return im
    l, t, r, b = bb
    return im.crop((max(l - pad, 0), max(t - pad, 0), min(r + pad, im.width), min(b + pad, im.height)))


def pill(w, h, fill, r=None, outline=None, ow=0):
    S = 3
    im = Image.new('RGBA', (w * S, h * S), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle([0, 0, w * S - 1, h * S - 1], radius=(r if r is not None else h // 2) * S,
                                         fill=fill, outline=outline, width=ow * S)
    return im.resize((w, h), Image.LANCZOS)


def label_box(txt, font, fg, bg, padx, h, r=None, outline=None, ow=0):
    t = crop_alpha(text_img(txt, font, fg), 0)
    w = t.width + padx * 2
    box = pill(w, h, bg, r=r, outline=outline, ow=ow)
    box.alpha_composite(t, ((w - t.width) // 2, (h - t.height) // 2))
    return box


def wrap(txt, font, maxw):
    words = txt.split(); lines = []; cur = ''
    for w in words:
        test = (cur + ' ' + w).strip()
        if font.getlength(test) <= maxw or not cur: cur = test
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines


def circle_num(n, r, color, fs):
    S = 3; D = r * 2 + 12
    im = Image.new('RGBA', (D * S, D * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse([6 * S, 6 * S, (D - 6) * S, (D - 6) * S], fill=color, outline=DARK, width=7 * S)
    im = im.resize((D, D), Image.LANCZOS)
    t = crop_alpha(text_img(str(n), F(BEBAS, fs), DARK), 0)
    im.alpha_composite(t, ((D - t.width) // 2, (D - t.height) // 2 + 2))
    return im


def tilt_badge(txt, fs, bg):
    b = label_box(txt, F(LILITA, fs), WHITE, bg, int(fs * 0.45), int(fs * 1.55), r=int(fs * 0.3), outline=DARK, ow=max(3, fs // 12))
    return b.rotate(8, resample=Image.BICUBIC, expand=True)


def title_block(txt, size, maxw, accent, stroke, lh=0.92):
    font = F(BEBAS, size)
    lines = wrap(txt, font, maxw)
    while len(lines) > 2 and size > 40:
        size -= 6; font = F(BEBAS, size); lines = wrap(txt, font, maxw)
    if len(lines) == 2:
        ws = txt.split(); best = None
        for k in range(1, len(ws)):
            a, b = ' '.join(ws[:k]), ' '.join(ws[k:])
            m = max(font.getlength(a), font.getlength(b))
            if m <= maxw and (best is None or m < best[0]): best = (m, [a, b])
        if best: lines = best[1]
    imgs = []
    for i, ln in enumerate(lines):
        col = accent if (len(lines) == 1 or i == len(lines) - 1) else WHITE
        imgs.append(crop_alpha(text_img(ln, font, col, stroke=stroke, stroke_fill=(0, 0, 0)), 0))
    step = int(size * lh)
    H = step * (len(imgs) - 1) + imgs[-1].height
    W = max(i.width for i in imgs)
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    for i, li in enumerate(imgs):
        im.alpha_composite(li, ((W - li.width) // 2, i * step))
    return im


def stack_lines(lines, size, stroke, lh=0.95):
    font = F(BEBAS, size)
    imgs = [crop_alpha(text_img(t, font, acc(c), stroke=stroke), 0) for t, c in lines]
    step = int(size * lh)
    H = step * (len(imgs) - 1) + imgs[-1].height
    W = max(i.width for i in imgs)
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    for i, li in enumerate(imgs):
        im.alpha_composite(li, ((W - li.width) // 2, i * step))
    return im


def fit_lines(lines, size, stroke, maxw, lh=0.95):
    """stack_lines, shrinking the font until the widest line fits maxw (prevents edge clipping)."""
    im = stack_lines(lines, size, stroke, lh)
    while im.width > maxw and size > 60:
        size -= 8
        im = stack_lines(lines, size, stroke, lh)
    return im


def bullet_row(txt, w, h, accent, fs):
    row = pill(w, h, (10, 8, 22, 150), r=10)
    d = ImageDraw.Draw(row)
    r = h * 0.17; cx = h * 0.5; cy = h / 2
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=accent)
    t = crop_alpha(text_img(txt, F(LILITA, fs), WHITE), 0)
    row.alpha_composite(t, (int(h * 0.95), (h - t.height) // 2))
    return row


def code_box(code, fs, accent):
    lab = crop_alpha(text_img('CODE:', F(LILITA, int(fs * 0.5)), WHITE), 0)
    t = crop_alpha(text_img(code, F(BEBAS, fs), accent, stroke=max(3, fs // 16)), 0)
    padx = int(fs * 0.35); h = int(fs * 1.25)
    w = lab.width + t.width + padx * 3
    box = pill(w, h, (10, 8, 22, 190), r=int(fs * 0.25), outline=accent, ow=max(3, fs // 22))
    box.alpha_composite(lab, (padx, (h - lab.height) // 2))
    box.alpha_composite(t, (padx * 2 + lab.width, (h - t.height) // 2 + 2))
    return box


def header(short):
    fs = 60 if short else 42
    dot_r = fs * 0.16
    t = crop_alpha(text_img('BREAKING', F(BEBAS, fs), WHITE), 0)
    h = int(fs * 1.05); padx = int(fs * 0.3)
    w = int(padx * 2 + dot_r * 2 + fs * 0.18 + t.width)
    b = pill(w, h, RED, r=int(fs * 0.18))
    d = ImageDraw.Draw(b)
    cy = h / 2; cx = padx + dot_r
    d.ellipse([cx - dot_r, cy - dot_r, cx + dot_r, cy + dot_r], fill=WHITE)
    b.alpha_composite(t, (int(padx + dot_r * 2 + fs * 0.18), (h - t.height) // 2 + 1))
    n = crop_alpha(text_img('SECRET SPAWN NEWS', F(LILITA, int(fs * 0.62)), WHITE, stroke=2, stroke_fill=(0, 0, 0)), 0)
    im = Image.new('RGBA', (b.width + 24 + n.width, max(b.height, n.height)), (0, 0, 0, 0))
    im.alpha_composite(b, (0, (im.height - b.height) // 2))
    im.alpha_composite(n, (b.width + 24, (im.height - n.height) // 2))
    return im


def calendar_icon(size, mon, day):
    S = 3; n = 300
    im = Image.new('RGBA', (n * S, n * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([20 * S, 40 * S, 280 * S, 280 * S], radius=26 * S, fill=WHITE, outline=OUT, width=10 * S)
    d.rounded_rectangle([20 * S, 40 * S, 280 * S, 110 * S], radius=26 * S, fill=(255, 120, 40), outline=OUT, width=10 * S)
    d.rectangle([25 * S, 85 * S, 275 * S, 110 * S], fill=(255, 120, 40))
    d.line([20 * S, 110 * S, 280 * S, 110 * S], fill=OUT, width=10 * S)
    im = im.resize((n, n), Image.LANCZOS)
    m = crop_alpha(text_img(mon, F(BEBAS, 62), WHITE), 0)
    im.alpha_composite(m, ((n - m.width) // 2, 75 - m.height // 2 + 2))
    dd = crop_alpha(text_img(day, F(BEBAS, 150), DARK), 0)
    im.alpha_composite(dd, ((n - dd.width) // 2, 195 - dd.height // 2))
    return im.resize((size, size), Image.LANCZOS)


# ---------- background ----------
def gradient(W, H, top, bot):
    g = Image.new('RGB', (1, H))
    for y in range(H):
        k = y / (H - 1)
        g.putpixel((0, y), tuple(int(top[i] * (1 - k) + bot[i] * k) for i in range(3)))
    return g.resize((W, H)).convert('RGBA')


PERIOD = 110


@lru_cache(None)
def stripes(W, H):
    im = Image.new('RGBA', (W + PERIOD * 2, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for x in range(-H, W + PERIOD * 3, PERIOD):
        d.polygon([(x, H), (x + 34, H), (x + 34 + H * 0.6, 0), (x + H * 0.6, 0)], fill=(255, 255, 255, 13))
    return im


@lru_cache(None)
def dot(r, a):
    S = 4
    im = Image.new('RGBA', (r * 2 * S + 4, r * 2 * S + 4), (0, 0, 0, 0))
    ImageDraw.Draw(im).ellipse([2, 2, r * 2 * S + 1, r * 2 * S + 1], fill=(255, 255, 255, a))
    return im.resize((r * 2 + 1, r * 2 + 1), Image.LANCZOS)


def particles(W, H, n=55, seed=7):
    rnd = random.Random(seed)
    return [dict(x=rnd.uniform(0, W), y=rnd.uniform(0, H), r=rnd.choice([2, 2, 3, 3, 4]), v=rnd.uniform(8, 26),
                 a=rnd.choice([70, 100, 140, 180]), ph=rnd.uniform(0, 6.28), dx=rnd.uniform(-6, 6)) for _ in range(n)]


# ---------- easing ----------
def ease_out_back(x):
    c1 = 1.70158; c3 = c1 + 1
    return 1 + c3 * (x - 1) ** 3 + c1 * (x - 1) ** 2


def clamp(x, a=0, b=1):
    return max(a, min(b, x))


class El:
    def __init__(self, img, cx, cy, t0=0.0, anim='pop', bob=0, pulse=0):
        self.img, self.cx, self.cy, self.t0, self.anim, self.bob, self.pulse = img, cx, cy, t0, anim, bob, pulse

    def draw(self, frame, t):
        lt = t - self.t0
        if lt < 0: return
        D = 0.32
        p = clamp(lt / D)
        img = self.img; cx, cy = self.cx, self.cy
        if self.bob: cy += math.sin(t * 2.2) * self.bob
        sc = 1.0
        if self.pulse: sc = 1 + 0.045 * math.sin(t * 5)
        if p < 1:
            if self.anim == 'pop': sc *= 0.55 + 0.45 * ease_out_back(p)
            elif self.anim == 'slide': cx += (1 - ease_out_back(p)) * 90
            elif self.anim == 'up': cy += (1 - ease_out_back(p)) * 60
        if sc != 1.0:
            img = img.resize((max(1, int(img.width * sc)), max(1, int(img.height * sc))), Image.BILINEAR)
        if p < 1:
            a = img.getchannel('A').point(lambda v: int(v * min(1, p * 2.2)))
            img = img.copy(); img.putalpha(a)
        frame.alpha_composite(img, (int(cx - img.width / 2), int(cy - img.height / 2)))


# ---------- scene builders ----------
def build_short_scene(sc, meta, W, H, items_acc):
    els = []; A = ACC[sc['acc']]
    if sc['type'] == 'intro':
        lines = fit_lines(meta['title_lines'], 200, 9, 980, lh=0.9)
        els.append(El(lines, W / 2, 760, 0.0))
        tag = label_box(meta['tag'], F(LILITA, 66), WHITE, RED, 34, 104, r=22, outline=DARK, ow=5)
        els.append(El(tag, W / 2, 760 + lines.height / 2 + 90, 0.25))
    elif sc['type'] == 'item':
        els.append(El(circle_num('#%d' % sc['n'], 95, A, 120), W / 2, 380, 0.0))
        els.append(El(label_box(sc['game'], F(LILITA, 50), WHITE, (12, 10, 24, 215), 30, 78, r=12), W / 2, 545, 0.1))
        ic = ICONS[sc['icon']](440)
        els.append(El(ic, W / 2, 880, 0.18, bob=10))
        if sc.get('badge'):
            els.append(El(tilt_badge(sc['badge'], 50, (255, 77, 109) if sc['acc'] != 'pink' else (255, 170, 30)), W / 2 + 230, 700, 0.35))
        tb = title_block(sc['title'], 132, 960, A, 8)
        ty = 1235 + tb.height / 2 - 60
        els.append(El(tb, W / 2, ty, 0.3, anim='up'))
        if sc.get('code'):
            els.append(El(code_box(sc['code'], 84, A), W / 2, ty + tb.height / 2 + 85, 0.45, anim='up'))
    elif sc['type'] == 'outro':
        q = fit_lines(sc['q'], 200, 9, 980, lh=0.9)
        els.append(El(q, W / 2, 720, 0.0))
        for i, c in enumerate(items_acc):
            els.append(El(circle_num(i + 1, 82, ACC[c], 120), W / 2 + (i - 1) * 215, 1020, 0.2 + i * 0.12, pulse=1))
    return els


def build_long_scene(sc, W, H, items_acc):
    els = []; A = ACC[sc['acc']]
    if sc['type'] == 'intro':
        lines = fit_lines(sc['lines'], 160, 8, 1700, lh=0.9)
        els.append(El(lines, W / 2, 400, 0.0))
        tag = label_box(sc['tag'], F(LILITA, 54), WHITE, RED, 30, 86, r=18, outline=DARK, ow=4)
        els.append(El(tag, W / 2, 400 + lines.height / 2 + 75, 0.25))
    elif sc['type'] == 'item':
        ic = ICONS[sc['icon']](400)
        els.append(El(ic, 470, 470, 0.15, bob=8))
        if sc.get('badge'):
            els.append(El(tilt_badge(sc['badge'], 40, (255, 77, 109) if sc['acc'] != 'pink' else (255, 170, 30)), 650, 290, 0.35))
        # right column stacked + vertically centred in [120, 870]
        cx = 1330; RW = 900
        parts = []
        parts.append(('c', circle_num('#%d' % sc['n'], 62, A, 80), 0.0, 18))
        parts.append(('l', label_box(sc['game'], F(LILITA, 36), WHITE, (12, 10, 24, 215), 22, 58, r=10), 0.1, 22))
        parts.append(('t', title_block(sc['title'], 98, RW, A, 6), 0.2, 26))
        if sc.get('code'):
            parts.append(('k', code_box(sc['code'], 64, A), 0.32, 22))
        for i, b in enumerate(sc.get('bullets', [])):
            parts.append(('b', bullet_row(b, RW, 62, A, 32), 0.45 + i * 0.35, 14))
        total = sum(p[1].height + p[3] for p in parts) - parts[-1][3]
        y = 120 + (750 - total) / 2
        for kind, im, t0, gap in parts:
            x = cx if kind != 'b' else cx
            els.append(El(im, x, y + im.height / 2, t0, anim='slide' if kind == 'b' else 'pop'))
            y += im.height + gap
    elif sc['type'] == 'list':
        hd = title_block(sc['head'], 130, 1500, A, 7)
        els.append(El(hd, W / 2, 190, 0.0))
        rows = sc['rows']; RW = 1240; RH = 74; gap = 18
        y0 = 300
        for i, (g, dte) in enumerate(rows):
            row = pill(RW, RH, (10, 8, 22, 165), r=12)
            t = crop_alpha(text_img(g, F(LILITA, 38), WHITE), 0)
            row.alpha_composite(t, (32, (RH - t.height) // 2))
            dt = crop_alpha(text_img(dte, F(LILITA, 38), ACC['yellow']), 0)
            row.alpha_composite(dt, (RW - 32 - dt.width, (RH - dt.height) // 2))
            els.append(El(row, W / 2, y0 + i * (RH + gap) + RH / 2, 0.3 + i * 0.45, anim='slide'))
    elif sc['type'] == 'outro':
        q = fit_lines(sc['q'], 170, 8, 1700, lh=0.9)
        els.append(El(q, W / 2, 360, 0.0))
        sub = label_box('SUBSCRIBE', F(LILITA, 76), WHITE, RED, 60, 130, r=26, outline=DARK, ow=6)
        els.append(El(sub, W / 2, 660, 0.4, pulse=1))
    return els


# ---------- captions ----------
def chunk_words(words, maxw, maxc):
    chunks = []; cur = []
    for w in words:
        cur.append(w)
        txt = ' '.join(x['w'] for x in cur)
        if len(cur) >= maxw or len(txt) >= maxc or w['w'][-1:] in '.?!,:':
            chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    return chunks


class Captions:
    def __init__(self, scenes_tl, short, W, H, accents):
        self.short = short; self.W, self.H = W, H
        self.items = []
        for sc, acc_name in zip(scenes_tl, accents):
            for ch in chunk_words(sc['words'], 3 if short else 5, 16 if short else 30):
                self.items.append((ch[0]['t'], ch, ACC[acc_name]))
        self.items.sort(key=lambda x: x[0])
        self.size = 104 if short else 74
        self.font = F(BEBAS, self.size)
        self.cache = {}

    def render(self, ch, n, A):
        key = (id(ch), n)
        if key in self.cache: return self.cache[key]
        st = 7 if self.short else 6
        sp = self.font.getlength(' ')
        imgs = [crop_alpha(text_img(w['w'].upper(), self.font, A if w['hi'] else WHITE, stroke=st), 0) for w in ch]
        tw = sum(i.width for i in imgs) + sp * (len(imgs) - 1)
        mh = max(i.height for i in imgs)
        if tw > self.W - 60:  # safety scale
            s = (self.W - 60) / tw
            imgs = [i.resize((int(i.width * s), int(i.height * s)), Image.LANCZOS) for i in imgs]
            sp *= s; tw = self.W - 60; mh = max(i.height for i in imgs)
        im = Image.new('RGBA', (int(tw) + 4, mh + 4), (0, 0, 0, 0))
        x = 2
        for i, wi in enumerate(imgs):
            if i < n: im.alpha_composite(wi, (int(x), 2 + mh - wi.height))
            x += wi.width + sp
        self.cache[key] = im
        return im

    def draw(self, frame, t):
        cur = None
        for i, (t0, ch, A) in enumerate(self.items):
            if t0 <= t: cur = (i, ch, A)
            else: break
        if cur is None: return
        i, ch, A = cur
        last = ch[-1]['t']
        nxt = self.items[i + 1][0] if i + 1 < len(self.items) else 1e9
        if t > max(last + 1.2, 0) and t < nxt and nxt - last > 1.6: return
        n = sum(1 for w in ch if w['t'] <= t + 0.02)
        im = self.render(ch, n, A)
        if self.short:
            cy = 1630
        else:
            cy = 990
        frame.alpha_composite(im, (int(self.W / 2 - im.width / 2), int(cy - im.height / 2)))


# ---------- main render ----------
def render(name, only=None):
    short = name.startswith('short')
    W, H = (1080, 1920) if short else (1920, 1080)
    tl = json.load(open(f'{OUTDIR}/{name}.json'))
    scenes = SHORTS[name]['scenes'] if short else LONG['scenes']
    meta = SHORTS[name] if short else None
    items_acc = [s['acc'] for s in scenes if s['type'] == 'item']
    total = tl[-1]['end']
    nframes = int(round(total * FPS))
    built = []
    for sc, st in zip(scenes, tl):
        els = build_short_scene(sc, meta, W, H, items_acc) if short else build_long_scene(sc, W, H, items_acc)
        built.append((st['start'], st['end'], gradient(W, H, *PAL[sc['bg']]), els, ACC[sc['acc']]))
    caps = Captions(tl, short, W, H, [s['acc'] for s in scenes])
    hdr = header(short)
    hdr_pos = (48, 120) if short else (36, 32)
    strip = None
    if not short:
        strip = Image.new('RGBA', (W, 150), (8, 6, 18, 150))
    parts = particles(W, H)
    stp = stripes(W, H)
    out = f'{OUTDIR}/{name}_video.mp4'
    cmd = ['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-pix_fmt', 'yuv420p', out]
    pr = None if only else subprocess.Popen(cmd, stdin=subprocess.PIPE)
    si = 0
    for f in (sorted(only) if only else range(nframes)):
        t = f / FPS
        si = 0
        while si + 1 < len(built) and t >= built[si + 1][0]: si += 1
        s0, s1, bg, els, A = built[si]
        lt = t - s0
        fr = bg.copy()
        off = int((t * 28) % PERIOD)
        fr.alpha_composite(stp.crop((PERIOD - off, 0, PERIOD - off + W, H)))
        for p in parts:
            y = (p['y'] - p['v'] * t) % (H + 20) - 10
            x = p['x'] + math.sin(t * 0.7 + p['ph']) * 12
            tw = 0.6 + 0.4 * math.sin(t * 2 + p['ph'])
            fr.alpha_composite(dot(p['r'], int(p['a'] * tw)), (int(x), int(y)))
        for e in els: e.draw(fr, lt)
        fr.alpha_composite(hdr, hdr_pos)
        if strip is not None: fr.alpha_composite(strip, (0, H - 150 - 14))
        caps.draw(fr, t)
        # progress bar
        d = ImageDraw.Draw(fr)
        bh = 12 if short else 10
        d.rectangle([0, H - bh, W, H], fill=(0, 0, 0, 255))
        d.rectangle([0, H - bh, int(W * (t / total)), H], fill=A + (255,))
        if only:
            fr.convert('RGB').save(f'{OUTDIR}/prev_{name}_{f:05d}.jpg', quality=85); continue
        pr.stdin.write(fr.convert('RGB').tobytes())
        if f % 300 == 0: print(name, f, '/', nframes, flush=True)
    if pr: pr.stdin.close(); pr.wait()
    return out, total


if __name__ == '__main__':
    if sys.argv[1] == 'preview':
        name = sys.argv[2]
        tl = json.load(open(f'{OUTDIR}/{name}.json'))
        fr = set()
        for st in tl:
            fr.add(int((st['start'] + 1.6) * FPS)); fr.add(int((st['end'] - 0.4) * FPS))
        render(name, fr)
    else:
        for n in sys.argv[1:]:
            render(n)

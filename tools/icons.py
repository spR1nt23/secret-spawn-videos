"""Simple flat icons with thick dark outlines, drawn at 4x then downsampled."""
from PIL import Image, ImageDraw
import math

OUT = (27, 24, 44)
S = 4  # supersample


def _canvas(n=512):
    im = Image.new('RGBA', (n * S, n * S), (0, 0, 0, 0))
    return im, ImageDraw.Draw(im)


def _fin(im, size):
    return im.resize((size, size), Image.LANCZOS)


def P(pts):
    return [(x * S, y * S) for x, y in pts]


def B(box):
    return [v * S for v in box]


W = 14  # outline width (in 512 space)


def poly(d, pts, fill, w=W):
    d.polygon(P(pts), fill=fill)
    d.line(P(pts + [pts[0]]), fill=OUT, width=w * S, joint='curve')
    for x, y in pts:
        r = w / 2
        d.ellipse(B([x - r, y - r, x + r, y + r]), fill=OUT)


def ell(d, box, fill, w=W):
    d.ellipse(B(box), fill=fill, outline=OUT, width=w * S)


def rrect(d, box, r, fill, w=W):
    d.rounded_rectangle(B(box), radius=r * S, fill=fill, outline=OUT, width=w * S)


def swords(size):
    im, d = _canvas()
    for flip in (1, -1):
        def T(x, y):
            return (256 + flip * (x - 256), y)
        blade = [T(118, 96), T(150, 80), T(370, 300), T(352, 336), T(330, 342)]
        blade = [T(110, 70), T(150, 78), T(372, 300), T(340, 332), T(118, 110)]
        poly(d, blade, (214, 226, 240))
        d.line(P([T(130, 90), T(350, 312)]), fill=(255, 255, 255), width=6 * S)
        guard = [T(318, 352), T(388, 282), T(408, 302), T(338, 372)]
        poly(d, guard, (255, 196, 46))
        grip = [T(372, 338), T(392, 318), T(440, 366), T(420, 386)]
        poly(d, grip, (140, 78, 40))
        ell(d, [T(424, 372)[0] - 26, 372, T(424, 372)[0] + 26, 424], (255, 196, 46))
    return _fin(im, size)


def flame(size):
    im, d = _canvas()
    outer = []
    for i in range(0, 361, 6):
        a = math.radians(i)
        r = 150
        x = 256 + r * math.sin(a) * (0.95)
        y = 330 - r * math.cos(a) * 1.0
        if math.cos(a) > 0:
            y = 330 - (r + 110 * math.cos(a) ** 3) * math.cos(a)
            x = 256 + r * math.sin(a) * (1 - 0.55 * math.cos(a) ** 2)
        outer.append((x, y))
    poly(d, outer, (255, 102, 36))
    inner = []
    for i in range(0, 361, 8):
        a = math.radians(i)
        r = 82
        x = 256 + r * math.sin(a) * (1 - 0.5 * max(0, math.cos(a)) ** 2)
        y = 372 - (r + (70 * math.cos(a) ** 3 if math.cos(a) > 0 else 0)) * math.cos(a)
        inner.append((x, y))
    poly(d, inner, (255, 214, 64), w=10)
    return _fin(im, size)


def moon(size):
    im, d = _canvas()
    ell(d, [86, 86, 426, 426], (244, 232, 190))
    for (x, y, r) in [(200, 190, 34), (300, 300, 26), (190, 320, 18), (320, 170, 16)]:
        d.ellipse(B([x - r, y - r, x + r, y + r]), fill=(214, 198, 150))
    # bat-like simple wing shape
    for (x, y, r) in [(70, 90, 16), (440, 120, 12), (450, 420, 14), (60, 400, 10)]:
        st = []
        for i in range(8):
            a = math.radians(-90 + 45 * i); rr = r if i % 2 == 0 else r * 0.4
            st.append((x + rr * math.cos(a), y + rr * math.sin(a)))
        d.polygon(P(st), fill=(255, 255, 255))
    return _fin(im, size)


def binoculars(size):
    im, d = _canvas()
    rrect(d, [196, 150, 316, 260], 26, (70, 76, 110))
    for cx in (166, 346):
        rrect(d, [cx - 80, 130, cx + 80, 330], 40, (86, 94, 140))
        ell(d, [cx - 92, 270, cx + 92, 454], (60, 66, 100))
        ell(d, [cx - 62, 300, cx + 62, 424], (120, 200, 255), w=10)
        d.ellipse(B([cx - 30, 318, cx + 4, 352]), fill=(255, 255, 255))
    return _fin(im, size)


def frame(size):
    im, d = _canvas()
    rrect(d, [60, 90, 452, 422], 30, (255, 196, 46))
    rrect(d, [104, 134, 408, 378], 12, (120, 200, 255), w=10)
    poly(d, [(110, 372), (210, 250), (290, 372)], (90, 200, 120), w=8)
    poly(d, [(220, 372), (310, 280), (402, 372)], (60, 160, 100), w=8)
    ell(d, [312, 160, 370, 218], (255, 236, 120), w=8)
    # avatar silhouette
    ell(d, [226, 178, 286, 238], (255, 255, 255), w=8)
    rrect(d, [212, 244, 300, 340], 20, (255, 255, 255), w=8)
    return _fin(im, size)


def trophy(size):
    im, d = _canvas()
    for cx in (130, 382):
        ell(d, [cx - 56, 120, cx + 56, 250], (0, 0, 0, 0))
    poly(d, [(140, 90), (372, 90), (352, 250), (306, 300), (206, 300), (160, 250)], (255, 196, 46))
    rrect(d, [228, 296, 284, 360], 8, (230, 160, 30))
    rrect(d, [160, 356, 352, 420], 14, (140, 78, 40))
    d.line(P([(180, 110), (196, 230)]), fill=(255, 240, 170), width=12 * S)
    # star
    st = []
    for i in range(10):
        a = math.radians(-90 + 36 * i); r = 46 if i % 2 == 0 else 20
        st.append((256 + r * math.cos(a), 185 + r * math.sin(a)))
    poly(d, st, (255, 255, 255), w=8)
    return _fin(im, size)


def gem(size):
    im, d = _canvas()
    top = [(150, 150), (362, 150), (430, 230), (82, 230)]
    poly(d, top, (130, 230, 255))
    poly(d, [(82, 230), (430, 230), (256, 440)], (60, 170, 240))
    d.line(P([(190, 150), (160, 230), (256, 440)]), fill=OUT, width=8 * S)
    d.line(P([(322, 150), (352, 230), (256, 440)]), fill=OUT, width=8 * S)
    d.line(P([(256, 150), (256, 230)]), fill=OUT, width=8 * S)
    d.polygon(P([(170, 165), (240, 165), (215, 215), (125, 215)]), fill=(220, 248, 255))
    return _fin(im, size)


def mystery(size):
    im, d = _canvas()
    rrect(d, [96, 96, 416, 416], 40, (255, 196, 46))
    rrect(d, [126, 126, 386, 386], 24, (255, 222, 110), w=0)
    # question mark
    d.arc(B([186, 150, 326, 290]), start=180, end=420, fill=OUT, width=44 * S)
    d.rounded_rectangle(B([234, 272, 278, 320]), radius=8 * S, fill=OUT)
    d.ellipse(B([234, 336, 278, 380]), fill=OUT)
    return _fin(im, size)


def fruit(size):
    im, d = _canvas()
    ell(d, [96, 130, 416, 446], (176, 92, 236))
    for i, cx in enumerate((176, 256, 336)):
        d.arc(B([cx - 60, 150, cx + 60, 430]), start=250, end=290, fill=(120, 50, 180), width=10 * S)
    swirl = [(150, 250), (200, 220), (250, 260), (300, 220), (350, 250)]
    d.line(P(swirl), fill=(120, 50, 180), width=12 * S, joint='curve')
    swirl2 = [(150, 330), (200, 300), (250, 340), (300, 300), (350, 330)]
    d.line(P(swirl2), fill=(120, 50, 180), width=12 * S, joint='curve')
    rrect(d, [244, 80, 270, 150], 10, (110, 70, 40), w=8)
    poly(d, [(268, 110), (340, 70), (380, 100), (310, 136)], (90, 200, 110), w=8)
    d.ellipse(B([150, 180, 196, 226]), fill=(235, 200, 255))
    return _fin(im, size)


def shield(size):
    im, d = _canvas()
    pts = [(256, 70), (420, 130), (406, 290), (256, 450), (106, 290), (92, 130)]
    poly(d, pts, (79, 179, 255))
    poly(d, [(256, 110), (380, 156), (370, 280), (256, 404)], (50, 140, 230), w=0)
    d.line(P([(180, 260), (238, 318), (340, 196)]), fill=(255, 255, 255), width=34 * S, joint='curve')
    return _fin(im, size)


def tag(size):
    im, d = _canvas()
    pts = [(90, 160), (330, 160), (430, 256), (330, 352), (90, 352)]
    poly(d, pts, (255, 154, 60))
    ell(d, [326, 232, 374, 280], (255, 255, 255), w=10)
    for y in (220, 256, 292):
        d.line(P([(130, y), (280 - (0 if y == 256 else 50), y)]), fill=OUT, width=14 * S)
    return _fin(im, size)


def calendar(size, mon='NOV', day='14'):
    return None  # drawn in renderer with fonts


ICONS = dict(swords=swords, flame=flame, moon=moon, binoculars=binoculars, frame=frame, trophy=trophy,
             gem=gem, mystery=mystery, fruit=fruit, shield=shield, tag=tag)


def pyramid(size):
    im, d = _canvas()
    poly(d, [(256, 80), (440, 400), (72, 400)], (240, 196, 90))
    poly(d, [(256, 80), (440, 400), (300, 400)], (205, 160, 60), w=0)
    for y in (200, 280, 350):
        x0 = 256 - (y - 80) * 0.575; x1 = 256 + (y - 80) * 0.575
        d.line(P([(x0 + 12, y), (x1 - 12, y)]), fill=OUT, width=8 * S)
    rrect(d, [226, 330, 286, 400], 8, (60, 40, 30), w=8)
    ell(d, [380, 60, 452, 132], (255, 220, 90), w=8)
    return _fin(im, size)


def bolt(size):
    im, d = _canvas()
    poly(d, [(300, 50), (130, 290), (240, 290), (200, 460), (390, 200), (275, 200), (330, 50)], (255, 214, 40))
    d.line(P([(290, 80), (175, 260)]), fill=(255, 250, 200), width=10 * S)
    return _fin(im, size)


def scroll(size):
    im, d = _canvas()
    rrect(d, [120, 90, 392, 420], 18, (250, 238, 205))
    ell(d, [96, 66, 176, 116], (230, 205, 160), w=10)
    ell(d, [336, 394, 416, 444], (230, 205, 160), w=10)
    for i, y in enumerate((160, 205, 250, 295)):
        d.line(P([(165, y), (350 - (60 if i == 3 else 0), y)]), fill=OUT, width=12 * S)
    ell(d, [290, 300, 370, 380], (230, 50, 60), w=10)
    return _fin(im, size)


def car(size):
    im, d = _canvas()
    poly(d, [(60, 330), (80, 250), (170, 240), (220, 170), (340, 170), (400, 240), (452, 260), (452, 330)], (230, 60, 60))
    poly(d, [(235, 185), (330, 185), (375, 240), (205, 240)], (150, 220, 255), w=8)
    d.line(P([(285, 185), (285, 240)]), fill=OUT, width=8 * S)
    for cx in (150, 370):
        ell(d, [cx - 52, 290, cx + 52, 394], (50, 50, 60))
        ell(d, [cx - 22, 320, cx + 22, 364], (200, 200, 210), w=8)
    d.text((0, 0), '')
    return _fin(im, size)


def drill(size):
    im, d = _canvas()
    rrect(d, [80, 150, 330, 270], 30, (255, 196, 46))
    rrect(d, [150, 250, 240, 430], 20, (60, 60, 80))
    poly(d, [(330, 170), (400, 190), (400, 230), (330, 250)], (160, 160, 175))
    poly(d, [(400, 195), (470, 210), (400, 225)], (200, 200, 215), w=8)
    for x in (110, 150):
        d.line(P([(x, 180), (x, 240)]), fill=OUT, width=8 * S)
    return _fin(im, size)


def bucket(size):
    im, d = _canvas()
    poly(d, [(110, 170), (402, 170), (370, 430), (142, 430)], (79, 179, 255))
    ell(d, [104, 140, 408, 200], (60, 140, 230))
    poly(d, [(150, 175), (210, 175), (205, 300), (175, 330), (150, 300)], (255, 90, 160), w=8)
    d.arc(B([130, 40, 382, 250]), start=200, end=340, fill=OUT, width=14 * S)
    return _fin(im, size)


def pause(size):
    im, d = _canvas()
    ell(d, [66, 66, 446, 446], (230, 70, 90))
    rrect(d, [180, 160, 236, 352], 12, (255, 255, 255), w=8)
    rrect(d, [276, 160, 332, 352], 12, (255, 255, 255), w=8)
    return _fin(im, size)


def fish(size):
    im, d = _canvas()
    ell(d, [90, 160, 370, 352], (255, 170, 60))
    poly(d, [(350, 256), (452, 170), (452, 342)], (255, 130, 40))
    poly(d, [(200, 165), (250, 110), (290, 170)], (255, 130, 40), w=10)
    ell(d, [140, 220, 184, 264], (255, 255, 255), w=8)
    d.ellipse(B([156, 234, 176, 254]), fill=OUT)
    d.arc(B([200, 190, 300, 320]), start=300, end=60, fill=OUT, width=8 * S)
    return _fin(im, size)


def hammer(size):
    im, d = _canvas()
    poly(d, [(250, 210), (290, 190), (420, 440), (380, 460)], (140, 78, 40))
    poly(d, [(120, 160), (300, 70), (350, 170), (170, 260)], (170, 175, 190))
    poly(d, [(300, 70), (330, 55), (380, 155), (350, 170)], (130, 135, 150), w=10)
    return _fin(im, size)


def ball(size):
    im, d = _canvas()
    ell(d, [70, 70, 442, 442], (255, 255, 255))
    pent = []
    for i in range(5):
        a = math.radians(-90 + 72 * i)
        pent.append((256 + 62 * math.cos(a), 256 + 62 * math.sin(a)))
    d.polygon(P(pent), fill=OUT)
    for i in range(5):
        a = math.radians(-90 + 72 * i)
        x0, y0 = 256 + 62 * math.cos(a), 256 + 62 * math.sin(a)
        x1, y1 = 256 + 160 * math.cos(a), 256 + 160 * math.sin(a)
        d.line(P([(x0, y0), (x1, y1)]), fill=OUT, width=10 * S)
        r = 34
        d.ellipse(B([x1 - r, y1 - r, x1 + r, y1 + r]), fill=OUT)
    return _fin(im, size)


ICONS.update(pyramid=pyramid, bolt=bolt, scroll=scroll, car=car, drill=drill, bucket=bucket,
             pause=pause, fish=fish, hammer=hammer, ball=ball)


def camera(size):
    im, d = _canvas()
    rrect(d, [70, 150, 442, 400], 40, (90, 96, 140))
    rrect(d, [180, 110, 300, 170], 16, (70, 76, 110))
    ell(d, [176, 190, 336, 350], (40, 44, 70))
    ell(d, [206, 220, 306, 320], (120, 200, 255), w=10)
    d.ellipse(B([226, 236, 256, 266]), fill=(255, 255, 255))
    rrect(d, [360, 180, 410, 215], 8, (255, 210, 63), w=8)
    return _fin(im, size)


def gamepad(size):
    im, d = _canvas()
    poly(d, [(110, 180), (402, 180), (452, 330), (420, 380), (360, 370), (320, 310), (192, 310), (152, 370), (92, 380), (60, 330)], (120, 90, 220))
    rrect(d, [130, 236, 210, 260], 6, (255, 255, 255), w=0)
    rrect(d, [158, 208, 182, 288], 6, (255, 255, 255), w=0)
    for (x, y, c) in [(350, 225, (91, 227, 125)), (390, 255, (255, 90, 110)), (350, 285, (79, 179, 255)), (310, 255, (255, 210, 63))]:
        ell(d, [x - 18, y - 18, x + 18, y + 18], c, w=6)
    return _fin(im, size)


def phone(size):
    im, d = _canvas()
    rrect(d, [150, 60, 362, 452], 36, (50, 54, 80))
    rrect(d, [172, 100, 340, 400], 12, (91, 227, 125), w=8)
    for i, h in enumerate((60, 110, 170, 230)):
        x = 196 + i * 36
        d.rectangle(B([x, 380 - h, x + 24, 380]), fill=OUT)
    rrect(d, [226, 418, 286, 430], 6, (200, 200, 210), w=0)
    return _fin(im, size)


def taco(size):
    im, d = _canvas()
    d.pieslice(B([60, 140, 452, 520]), start=180, end=360, fill=(255, 196, 70), outline=OUT, width=W * S)
    for i, (x, c) in enumerate([(130, (91, 200, 90)), (200, (230, 60, 60)), (270, (91, 200, 90)), (340, (230, 60, 60))]):
        ell(d, [x - 36, 170, x + 36, 240], c, w=8)
    d.pieslice(B([96, 176, 416, 520]), start=180, end=360, fill=(255, 214, 110), outline=OUT, width=10 * S)
    d.line(P([(60, 330), (452, 330)]), fill=OUT, width=W * S)
    return _fin(im, size)


def cake(size):
    im, d = _canvas()
    rrect(d, [90, 260, 422, 420], 20, (255, 160, 200))
    rrect(d, [130, 180, 382, 270], 18, (255, 220, 235))
    d.line(P([(100, 330), (412, 330)]), fill=(255, 255, 255), width=14 * S)
    for x in (190, 256, 322):
        rrect(d, [x - 10, 110, x + 10, 185], 4, (120, 200, 255), w=6)
        poly(d, [(x, 70), (x + 14, 100), (x, 112), (x - 14, 100)], (255, 196, 46), w=6)
    return _fin(im, size)


def top(size):
    im, d = _canvas()
    poly(d, [(256, 450), (90, 260), (130, 200), (382, 200), (422, 260)], (79, 179, 255))
    poly(d, [(130, 200), (382, 200), (340, 150), (172, 150)], (255, 90, 110))
    rrect(d, [236, 70, 276, 160], 10, (255, 210, 63), w=10)
    for a in (0, 1):
        d.arc(B([40 + a * 30, 300, 180 + a * 30, 420]), start=200, end=300, fill=(255, 255, 255), width=8 * S)
    return _fin(im, size)


def soap(size):
    im, d = _canvas()
    rrect(d, [80, 230, 400, 400], 50, (190, 140, 255))
    d.line(P([(130, 280), (230, 280)]), fill=(240, 220, 255), width=14 * S)
    for (x, y, r) in [(330, 160, 50), (420, 100, 34), (220, 120, 30), (450, 210, 22)]:
        ell(d, [x - r, y - r, x + r, y + r], (210, 240, 255), w=8)
        d.ellipse(B([x - r * 0.5, y - r * 0.6, x - r * 0.1, y - r * 0.2]), fill=(255, 255, 255))
    return _fin(im, size)


ICONS.update(camera=camera, gamepad=gamepad, phone=phone, taco=taco, cake=cake, top=top, soap=soap)

if __name__ == '__main__':
    rows = (len(ICONS) + 6) // 7
    sheet = Image.new('RGBA', (300 * 7, 300 * rows), (60, 40, 90, 255))
    for i, (k, f) in enumerate(ICONS.items()):
        sheet.alpha_composite(f(280), ((i % 7) * 300 + 10, (i // 7) * 300 + 10))
    import os, sys
    dst = sys.argv[1] if len(sys.argv) > 1 else 'icons.png'
    sheet.save(dst); print(dst)

"""The profile bunny, as a tiny curtain-call animation (self-hosted GIF).

Beat sheet (28 frames, 80 ms each):
  0-4   curtain closed
  5-9   curtain draws open
  10-12 bunny hops out into the light
  13-17 bunny waves bye-bye
  18-22 bunny hops off stage, a heart left behind
  23-27 curtain closes
"""
from PIL import Image, ImageDraw

W = H = 56
SCALE = 4
FRAMES = 28
DUR = 80

WHITE = (255, 255, 255)
SHADE = (231, 224, 241)
PINK = (247, 186, 203)
DEEP = (58, 44, 70)
DUST = (176, 166, 188)
CURTAIN = (198, 118, 150)
CURTAIN_DARK = (150, 80, 110)
CURTAIN_LIGHT = (228, 160, 186)
FLOOR = (238, 232, 244)


def curtain_open(i):
    if i <= 4:
        return 0.0
    if i <= 9:
        return (i - 4) / 5.0
    if i <= 22:
        return 1.0
    return max(0.0, 1.0 - (i - 22) / 5.0)


def bunny_pose(i):
    """Return (dx, lift, squash, wave) for the visible part of the show."""
    if i < 10 or i > 22:
        return None
    dx, wave = 0, False
    if i in (10, 11):
        lift = -int(round(6 * (1 if i == 11 else 0.4)))
        sq = 1.06
    elif 12 <= i <= 16:
        lift, sq = 0, 1.0
        wave = i >= 12
    else:
        step = i - 16
        lift = -3 if step % 2 else 0
        sq = 1.04 if step % 2 else 0.92
        dx = min(20, step * 4)
    return dx, lift, sq, wave


def draw_curtain(d, t, i=0):
    """Sliding velvet panels; they also hide the bunny when shut."""
    edge = W // 2 - t * 30
    sway = (i % 3)  # keeps even the closed beats from being identical
    d.rectangle([0, 0, W, 9], fill=CURTAIN_DARK)
    d.rectangle([0, 7, W, 9], fill=CURTAIN_LIGHT)
    for x0, x1 in ((0, edge), (W - edge, W)):
        if x1 - x0 <= 0:
            continue
        d.rectangle([x0, 9, x1, H], fill=CURTAIN)
        for fold in range(int(x0), int(x1), 6):
            d.rectangle([fold + 3 + sway, 9, fold + 4 + sway, H], fill=CURTAIN_DARK)
    if t < 0.15:
        d.rectangle([W // 2 - 1, 9, W // 2 + 1, H], fill=CURTAIN_DARK)


def draw_bunny(d, dx, lift, sq, wave, i):
    cx, ground = W // 2 + dx, 44
    body_h = int(13 * (2 - sq))
    body_w = int(14 * sq)
    bottom = ground + lift
    top = bottom - body_h
    d.ellipse([4, ground + 3, W - 4, ground + 8], fill=FLOOR)
    sw = max(6.0, 15 - abs(lift) * 0.5)
    d.ellipse([cx - sw / 2, ground + 2, cx + sw / 2, ground + 7], fill=(206, 196, 216))
    d.ellipse([cx + body_w // 2 - 3, top + body_h - 7, cx + body_w // 2 + 3, top + body_h - 1], fill=WHITE)
    d.ellipse([cx - body_w // 2, top, cx + body_w // 2, bottom], fill=WHITE)
    hr = int(8 * sq)
    hx, hy = cx - 1, top + 3
    d.ellipse([hx - hr, hy - hr, hx + hr, hy + hr], fill=WHITE)
    tilt = 1 if i in (13, 15, 17) else 0
    for side in (-1, 1):
        ex = hx + side * 4 + tilt * side
        d.ellipse([ex - 2, hy - hr - 11, ex + 2, hy - hr + 2], fill=WHITE)
        d.ellipse([ex - 1, hy - hr - 9, ex + 1, hy - hr - 1], fill=PINK)
    ey = hy - 1
    if i in (10, 16):
        d.line([hx - 4, ey, hx - 2, ey], fill=DEEP)
        d.line([hx + 2, ey, hx + 4, ey], fill=DEEP)
    else:
        d.point([hx - 3, ey], fill=DEEP)
        d.point([hx + 3, ey], fill=DEEP)
    d.point([hx, hy + 2], fill=PINK)
    d.point([hx - 5, hy + 1], fill=PINK)
    d.point([hx + 5, hy + 1], fill=PINK)
    if wave:
        wig = (0, 2, 1)[i % 3]
        d.ellipse([cx + body_w // 2 + 1, top - 2 - wig, cx + body_w // 2 + 5, top + 2 - wig], fill=WHITE)


def heart(d, x, y):
    d.point([x, y], fill=PINK)
    d.point([x + 2, y], fill=PINK)
    d.point([x, y + 1], fill=PINK)
    d.point([x + 2, y + 1], fill=PINK)
    d.point([x + 1, y + 2], fill=PINK)


def frame(i):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, H], fill=(252, 248, 252))
    d.rectangle([0, 44, W, H], fill=FLOOR)
    pose = bunny_pose(i)
    if pose:
        dx, lift, sq, wave = pose
        draw_bunny(d, dx, lift, sq, wave, i)
        if i >= 18:
            heart(d, W // 2 + dx - 12, 26 - (i - 18))
    draw_curtain(d, curtain_open(i), i)
    # a travelling glint on the valance: every frame differs, nothing flickers
    d.point([(i * 5) % (W - 1), 5], fill=CURTAIN_LIGHT)
    d.point([(i * 5) % (W - 1) + 1, 5], fill=(255, 235, 245))
    return img.resize((W * SCALE, H * SCALE), Image.NEAREST)


PALETTE = [WHITE, SHADE, PINK, DEEP, DUST, CURTAIN, CURTAIN_DARK, CURTAIN_LIGHT, FLOOR, (206, 196, 216)]


def to_palette(img):
    pal = Image.new("P", (1, 1))
    flat = []
    for colour in PALETTE:
        flat.extend(colour)
    flat.extend([0, 0, 0] * (256 - len(PALETTE)))
    pal.putpalette(flat)
    alpha = img.getchannel("A")
    quant = img.convert("RGB").quantize(palette=pal, dither=Image.NONE)
    quant.paste(0, mask=alpha.point(lambda a: 255 if a < 128 else 0))
    return quant


frames = [to_palette(frame(i)) for i in range(FRAMES)]
frames[0].save("profile-readme/assets/bunny.gif", save_all=True, append_images=frames[1:],
               duration=DUR, loop=0, disposal=2, transparency=0, optimize=False)
print("wrote", len(frames), "frames")

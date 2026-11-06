"""Generate the profile bunny: a 20 frame pixel hop, self-hosted as a GIF."""
from PIL import Image, ImageDraw

W = H = 56
SCALE = 4
FRAMES = 20
DUR = 70

WHITE = (255, 255, 255, 255)
SHADE = (231, 224, 241, 255)
PINK = (247, 186, 203, 255)
DEEP = (58, 44, 70, 255)
DUST = (156, 146, 168, 190)


def hop(i):
    """Parabola across frames 2..14, flat while grounded."""
    if 2 <= i <= 14:
        t = (i - 2) / 12.0
        return -int(round(13 * 4 * t * (1 - t)))
    return 0


def squash(i):
    """Every key pose gets its own value so no two frames are identical."""
    table = {0: 0.72, 1: 0.82, 2: 1.16, 3: 1.08, 4: 1.03, 13: 0.96,
             14: 0.70, 15: 0.86, 16: 0.94, 17: 1.0, 18: 0.9, 19: 0.78}
    return table.get(i, 1.0)


def ear_tilt(i):
    """Ears lean back on the way up and flip forward on the way down."""
    if 3 <= i <= 6:
        return 2
    if 7 <= i <= 10:
        return 1
    if 11 <= i <= 14:
        return -1
    return 0


def blink(i):
    return i in (5, 17)


def frame(i):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    lift, sq, tilt = hop(i), squash(i), ear_tilt(i)
    cx, ground = W // 2, 46

    sw = max(7.0, 16 - abs(lift) * 0.55)
    d.ellipse([cx - sw, ground + 3, cx + sw, ground + 8], fill=(122, 106, 134, 80))

    body_h = int(12 * (2 - sq))
    body_w = int(13 * sq)
    bottom = ground + lift
    top = bottom - body_h

    if i in (0, 1, 15, 19):
        d.ellipse([cx - 7, bottom - 2, cx - 1, bottom + 2], fill=WHITE)
        d.ellipse([cx + 1, bottom - 2, cx + 7, bottom + 2], fill=WHITE)
    d.ellipse([cx + body_w // 2 - 3, top + body_h - 6, cx + body_w // 2 + 3, top + body_h], fill=WHITE)
    d.ellipse([cx - body_w // 2, top, cx + body_w // 2, bottom], fill=WHITE)
    d.ellipse([cx - body_w // 4, top + 3, cx + body_w // 4, bottom - 1], fill=SHADE)

    head_r = int(8 * sq)
    hx, hy = cx - 1, top + 2
    d.ellipse([hx - head_r, hy - head_r, hx + head_r, hy + head_r], fill=WHITE)

    for side in (-1, 1):
        ex = hx + side * 4 + tilt * side
        d.ellipse([ex - 2, hy - head_r - 11, ex + 2, hy - head_r + 2], fill=WHITE)
        d.ellipse([ex - 1, hy - head_r - 9, ex + 1, hy - head_r - 2], fill=PINK)

    ey = hy - 1
    gaze = (i % 3) - 1          # the bunny looks around, and no two frames tie
    if blink(i):
        d.line([hx - 4 + gaze, ey, hx - 2 + gaze, ey], fill=DEEP)
        d.line([hx + 2 + gaze, ey, hx + 4 + gaze, ey], fill=DEEP)
    else:
        d.point([hx - 3 + gaze, ey], fill=DEEP)
        d.point([hx + 3 + gaze, ey], fill=DEEP)
    d.ellipse([hx - 1, ey + 2, hx + 1, ey + 4], fill=PINK)
    d.point([hx - 6, ey + 3], fill=(250, 205, 216, 255))
    d.point([hx + 6, ey + 3], fill=(250, 205, 216, 255))

    if i in (14, 15):
        for dx in (-11, 11):
            d.ellipse([cx + dx - 2, ground - 1, cx + dx, ground + 1], fill=DUST)

    if i in (18, 19):
        hy2 = top - 8 - (i - 18) * 2
        d.polygon([(cx + 10, hy2), (cx + 13, hy2 - 3), (cx + 16, hy2),
                   (cx + 13, hy2 + 4)], fill=(240, 150, 180, 230))

    return img.resize((W * SCALE, H * SCALE), Image.NEAREST)



PALETTE = [(0, 0, 0), (255, 255, 255), (231, 224, 241), (247, 186, 203),
           (58, 44, 70), (156, 146, 168), (250, 205, 216), (240, 150, 180)]


def to_palette(img):
    """Quantise to a fixed palette so frame identity is exact and small."""
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
print("wrote", len(frames), "palette frames")

"""Profile curtain-call animation, drawn pixel by pixel (no external assets).

32 frames, 80 ms each. The bunny is white with a soft outline, a bow, whiskers
and a wink; the stage has a scalloped valance, tassels, folds and a spotlight.
"""
from PIL import Image, ImageDraw

W = H = 72
SCALE = 4
FRAMES = 32
DUR = 80

WHITE = (255, 255, 255)
FUR_SH = (240, 236, 249)
PINK = (247, 186, 203)
DEEP = (52, 40, 64)
OUTLINE = (158, 148, 176)
CURTAIN = (198, 118, 150)
CURTAIN_DK = (146, 76, 106)
CURTAIN_LT = (232, 168, 192)
FLOOR = (243, 236, 249)
GOLD = (236, 202, 132)
HEART = (238, 146, 178)

PALETTE = [DEEP, WHITE, FUR_SH, PINK, DEEP, OUTLINE, CURTAIN, CURTAIN_DK,
           CURTAIN_LT, FLOOR, GOLD, HEART]


def curtain_open(i):
    if i <= 5:
        return 0.0
    if i <= 11:
        return (i - 5) / 6.0
    if i <= 25:
        return 1.0
    return max(0.0, 1.0 - (i - 25) / 6.0)


def bunny_pose(i):
    """(dx, lift, squash, wave, exit) for the beats where the bunny is on stage."""
    if i < 12 or i > 25:
        return None
    if i in (12, 13):
        return 0, (-7 if i == 13 else -3), 1.08, False, False
    if i == 14:
        return 0, 0, 0.88, False, False
    if 15 <= i <= 20:
        return 0, 0, 1.0, True, False
    step = i - 20
    return min(22, step * 5), (-4 if step % 2 else 0), (1.04 if step % 2 else 0.9), True, True


def draw_stage(d, t):
    d.rectangle([0, 0, W, H], fill=FLOOR)
    d.rectangle([0, 56, W, H], fill=(232, 224, 242))
    if t > 0.5:
        d.ellipse([W // 2 - 16, 52, W // 2 + 16, 62], fill=(250, 246, 253))


def draw_curtain(d, t, i):
    edge = W // 2 - t * 32
    sway = i % 3
    for x0, x1 in ((0, edge), (W - edge, W)):
        if x1 - x0 <= 0:
            continue
        d.rectangle([x0, 10, x1, H], fill=CURTAIN)
        for fold in range(int(x0), int(x1), 7):
            d.rectangle([fold + 3 + sway, 10, fold + 5 + sway, H], fill=CURTAIN_DK)
            d.rectangle([fold + 5 + sway, 10, fold + 6 + sway, H], fill=CURTAIN_LT)
    d.rectangle([0, 0, W, 12], fill=CURTAIN_DK)
    for x in range(0, W, 8):
        d.ellipse([x, 6, x + 8, 16], fill=CURTAIN)
    d.rectangle([0, 0, W, 7], fill=CURTAIN_DK)
    for x in range(2, W, 8):
        d.point([x + 2, 15], fill=GOLD)
    if t < 0.2:
        d.rectangle([W // 2 - 1, 10, W // 2 + 1, H], fill=CURTAIN_DK)


def draw_bunny(d, pose, i, dx=0, lift=0, sq=1.0, wave=False):
    cx, ground = W // 2 + dx, 56
    body_h = int(17 * (2 - sq))
    body_w = int(18 * sq)
    bottom = ground + lift
    top = bottom - body_h
    d.ellipse([cx - body_w // 2 + 2, bottom - 3, cx + body_w // 2 - 2, bottom + 4], fill=FUR_SH)
    d.ellipse([cx - 10, bottom - 3, cx - 2, bottom + 2], fill=WHITE, outline=OUTLINE)
    d.ellipse([cx + 2, bottom - 3, cx + 10, bottom + 2], fill=WHITE, outline=OUTLINE)
    d.ellipse([cx + body_w // 2 - 6, top + body_h - 9, cx + body_w // 2 + 3, top + body_h - 1],
              fill=WHITE, outline=OUTLINE)
    d.ellipse([cx - body_w // 2, top, cx + body_w // 2, bottom], fill=WHITE, outline=OUTLINE)
    d.arc([cx - body_w // 2 + 3, top + body_h // 2, cx + body_w // 2 - 3, bottom - 2], 20, 160, fill=FUR_SH)
    hr = int(10 * sq)
    hx, hy = cx - 1, top - 1
    d.ellipse([hx - hr, hy - hr, hx + hr, hy + hr], fill=WHITE, outline=OUTLINE)

    bounce = 1 if i in (16, 18, 20) else 0
    for side in (-1, 1):
        ex = hx + side * 5 + side * bounce
        d.ellipse([ex - 3, hy - hr - 15, ex + 3, hy - hr + 3], fill=WHITE, outline=OUTLINE)
        d.ellipse([ex - 2, hy - hr - 12, ex + 2, hy - hr - 1], fill=PINK)
    bx, by = hx - hr - 4, hy - hr - 12
    d.ellipse([bx - 3, by - 2, bx + 1, by + 2], fill=PINK, outline=CURTAIN_DK)
    d.ellipse([bx + 1, by - 2, bx + 5, by + 2], fill=PINK, outline=CURTAIN_DK)
    d.point([bx, by], fill=CURTAIN_DK)
    d.point([bx + 1, by], fill=CURTAIN_DK)
    ey = hy - 1
    for side in (-1, 1):
        x = hx + side * 4
        if (i in (15, 21) and side == 1) or i in (13, 24):
            d.line([x - 2, ey, x + 1, ey], fill=DEEP)
        else:
            d.rectangle([x - 1, ey - 1, x + 1, ey + 1], fill=DEEP)
            d.point([x - 1, ey - 1], fill=WHITE)
    d.rectangle([hx - 1, hy + 3, hx + 1, hy + 4], fill=PINK)
    d.line([hx - 3, hy + 5, hx - 1, hy + 7], fill=OUTLINE)
    d.line([hx - 1, hy + 7, hx, hy + 5], fill=OUTLINE)
    d.line([hx, hy + 5, hx + 1, hy + 7], fill=OUTLINE)
    d.line([hx + 1, hy + 7, hx + 3, hy + 5], fill=OUTLINE)
    for side in (-1, 1):
        d.line([hx + side * 7, hy + 3, hx + side * 11, hy + 1], fill=OUTLINE)
        d.line([hx + side * 7, hy + 5, hx + side * 11, hy + 6], fill=OUTLINE)
    d.rectangle([hx - 9, hy + 2, hx - 7, hy + 3], fill=PINK)
    d.rectangle([hx + 7, hy + 2, hx + 9, hy + 3], fill=PINK)
    if wave:
        wig = (0, 3, 1)[i % 3]
        sx, sy = cx + body_w // 2 - 3, top + body_h // 2
        px, py = cx + body_w // 2 + 7, top + 1 - wig
        d.line([sx, sy, px, py], fill=WHITE, width=3)
        d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=WHITE, outline=OUTLINE)
        d.point([px - 1, py - 1], fill=PINK)
        d.point([px + 1, py - 1], fill=PINK)
        d.point([px, py + 2], fill=PINK)


def sparkle(d, x, y, big=False):
    d.point([x, y], fill=WHITE)
    d.point([x - 1, y], fill=GOLD)
    d.point([x + 1, y], fill=GOLD)
    d.point([x, y - 1], fill=GOLD)
    d.point([x, y + 1], fill=GOLD)
    if big:
        d.point([x, y + 2], fill=GOLD)
        d.point([x, y - 2], fill=GOLD)


def heart(d, x, y):
    for px, py in ((0, 0), (2, 0), (0, 1), (1, 1), (2, 1), (1, 2)):
        d.point([x + px, y + py], fill=HEART)


def build(i):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    t = curtain_open(i)
    draw_stage(d, t)
    pose = bunny_pose(i)
    if pose:
        draw_bunny(d, pose, i, *pose[:4])
    draw_curtain(d, t, i)
    d.point([(i * 5) % (W - 1), 4], fill=CURTAIN_LT)
    if 15 <= i <= 20 and i % 2:
        sparkle(d, 16, 26, big=True)
        sparkle(d, 56, 22)
    if pose and pose[4]:
        heart(d, W // 2 + 14, 22 - (i - 20))
    return img


def to_palette(img):
    pal = Image.new("P", (1, 1))
    flat = []
    for colour in PALETTE:
        flat.extend(colour)
    flat.extend([0, 0, 0] * (256 - len(PALETTE)))
    pal.putpalette(flat)
    quant = img.convert("RGB").quantize(palette=pal, dither=Image.NONE)
    quant.paste(0, mask=img.getchannel("A").point(lambda a: 255 if a < 128 else 0))
    return quant


frames = [to_palette(build(i)).resize((W * SCALE, H * SCALE), Image.NEAREST) for i in range(FRAMES)]
# resize after quantise keeps the palette, so scaling stays crisp
frames[0].save("profile-readme/assets/bunny.gif", save_all=True, append_images=frames[1:],
               duration=DUR, loop=0, disposal=2, transparency=0, optimize=False)
print("wrote", len(frames), "frames")

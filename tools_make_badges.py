"""Generate three animated (shimmering) SVG badges, self-hosted in the repo."""
from pathlib import Path

TPL = '''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="36" viewBox="0 0 {W} 36" role="img" aria-label="{label}: {value}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{c1}"/>
      <stop offset="1" stop-color="{c2}"/>
    </linearGradient>
    <linearGradient id="shine" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#ffffff" stop-opacity="0"/>
      <stop offset="0.5" stop-color="#ffffff" stop-opacity="0.85"/>
      <stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="pill"><rect x="1" y="1" width="{W2}" height="34" rx="17"/></clipPath>
  </defs>
  <rect x="1" y="1" width="{W2}" height="34" rx="17" fill="url(#bg)"/>
  <rect x="1" y="1" width="{W2}" height="34" rx="17" fill="none" stroke="#ffffff" stroke-opacity="0.7"/>
  <g clip-path="url(#pill)">
    <rect x="-80" y="-4" width="46" height="44" fill="url(#shine)" transform="skewX(-20)">
      <animate attributeName="x" values="-80;{W}" dur="2.8s" repeatCount="indefinite"/>
    </rect>
  </g>
  <path d="{ICON}" fill="{INK}" opacity="0.55"/>
  <text x="30" y="24" font-family="'Segoe UI',Helvetica,Arial,sans-serif" font-size="14" font-weight="700" fill="#3a2c44">{label}</text>
  <text x="{VX}" y="24" font-family="'Segoe UI',Helvetica,Arial,sans-serif" font-size="14" font-weight="600" fill="#4b3a58">{value}</text>
  <path d="M{X} 9 l1.2 3.4 3.4 1.2 -3.4 1.2 -1.2 3.4 -1.2 -3.4 -3.4 -1.2 3.4 -1.2 z" fill="#ffffff" opacity="0.9">
    <animate attributeName="opacity" values="0.25;0.95;0.25" dur="2.2s" repeatCount="indefinite"/>
  </path>
</svg>
'''



HEART = "M12 21c-3.4-2.3-5.6-4.5-5.6-7A3 3 0 0 1 12 12a3 3 0 0 1 5.6 2c0 2.5-2.2 4.7-5.6 7z"
STAR = "M12 10l1.7 3.6 3.9.4-2.9 2.6.8 3.8-3.5-2-3.5 2 .8-3.8-2.9-2.6 3.9-.4z"
LEAF = "M8 20c0-6 4-10 10-10 0 6-4 10-10 10z"
SPARK = "M12 10l1.6 4.4 4.4 1.6-4.4 1.6-1.6 4.4-1.6-4.4-4.4-1.6 4.4-1.6z"
EAR = "M9 20c-1.6-3-1.2-7 1.2-8.4 1.6-1 2.6.8 2 2.8-.5 1.7-1.2 4-3.2 5.6zM15 20c1.6-3 1.2-7-1.2-8.4-1.6-1-2.6.8-2 2.8.5 1.7 1.2 4 3.2 5.6z"


def badge(label, value, c1, c2, icon=HEART, ink='#3a2c44'):
    width = int(48 + len(label) * 8.4 + len(value) * 7.9)
    vx = int(38 + len(label) * 8.4)
    return TPL.format(W=width, W2=width - 2, VX=vx, X=width - 14,
                      label=label, value=value, c1=c1, c2=c2, ICON=icon, INK=ink)


out = Path("profile-readme/assets/badges")
out.mkdir(parents=True, exist_ok=True)
specs = {
    "pypi.svg": badge("PyPI", "51k+ since June", "#f9c6d0", "#f3d7f0", HEART),
    "irlxleet.svg": badge("irlxleet", "5.4k downloads", "#e0c3fc", "#cfe0ff", STAR),
    "npm.svg": badge("npm", "irlxleet 1.1k", "#c9e4de", "#d9eef6", LEAF),
    "py3dgame.svg": badge("py3dgame", "3D engine in Python", "#c9e4de", "#e2f0fb", SPARK),
    "irl.svg": badge("IRL-", "package installer", "#fdf0c8", "#fbe6d4", HEART),
    "transpower.svg": badge("TransPower", "offline AI companion", "#f7d6e0", "#f3d7f0", HEART),
    "cutie-os.svg": badge("cutie-os", "gentle terminal", "#d6e4f0", "#e6e1fb", EAR),
}
for name, svg in specs.items():
    (out / name).write_text(svg, encoding="utf-8")
    print(name, len(svg), "bytes")

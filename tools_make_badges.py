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
  <text x="15" y="24" font-family="'Segoe UI',Helvetica,Arial,sans-serif" font-size="14" font-weight="700" fill="#3a2c44">{label}</text>
  <text x="{VX}" y="24" font-family="'Segoe UI',Helvetica,Arial,sans-serif" font-size="14" font-weight="600" fill="#4b3a58">{value}</text>
  <path d="M{X} 9 l1.2 3.4 3.4 1.2 -3.4 1.2 -1.2 3.4 -1.2 -3.4 -3.4 -1.2 3.4 -1.2 z" fill="#ffffff" opacity="0.9">
    <animate attributeName="opacity" values="0.25;0.95;0.25" dur="2.2s" repeatCount="indefinite"/>
  </path>
</svg>
'''


def badge(label, value, c1, c2):
    width = int(34 + len(label) * 8.4 + len(value) * 7.9)
    vx = int(24 + len(label) * 8.4)
    return TPL.format(W=width, W2=width - 2, VX=vx, X=width - 14,
                      label=label, value=value, c1=c1, c2=c2)


out = Path("profile-readme/assets/badges")
out.mkdir(parents=True, exist_ok=True)
specs = {
    "pypi.svg": badge("PyPI", "51k+ since June", "#f9c6d0", "#f3d7f0"),
    "irlxleet.svg": badge("irlxleet", "5.4k downloads", "#e0c3fc", "#cfe0ff"),
    "npm.svg": badge("npm", "irlxleet 1.1k", "#c9e4de", "#d9eef6"),
}
for name, svg in specs.items():
    (out / name).write_text(svg, encoding="utf-8")
    print(name, len(svg), "bytes")

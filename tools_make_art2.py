"""Apple-ish, soft and quiet art set for the profile README."""
from pathlib import Path

OUT = Path("profile-readme/assets/art")
SANS = "system-ui,-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"

HERO = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300" role="img" aria-label="Dev2Creator">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#fffdfe"/>
      <stop offset="0.55" stop-color="#fdf6fb"/>
      <stop offset="1" stop-color="#f4f1fd"/>
    </linearGradient>
    <radialGradient id="glow1" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#ffd7e6" stop-opacity="0.85"/>
      <stop offset="1" stop-color="#ffd7e6" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow2" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#d9d3ff" stop-opacity="0.75"/>
      <stop offset="1" stop-color="#d9d3ff" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="ink" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#3a2c44"/>
      <stop offset="1" stop-color="#5b4a63"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="300" fill="url(#sky)"/>
  <circle cx="240" cy="70" r="200" fill="url(#glow1)">
    <animate attributeName="cx" values="240;300;240" dur="14s" repeatCount="indefinite"/>
  </circle>
  <circle cx="980" cy="240" r="240" fill="url(#glow2)">
    <animate attributeName="cx" values="980;910;980" dur="18s" repeatCount="indefinite"/>
  </circle>
  <text x="600" y="140" text-anchor="middle" font-family="Georgia,serif" font-size="66" font-weight="400" letter-spacing="1" fill="url(#ink)">Dev2Creator</text>
  <text x="600" y="180" text-anchor="middle" font-family="{SANS}" font-size="13" letter-spacing="7" fill="#a291a8">LITTLE IDEAS, REAL CREATIONS</text>
  <line x1="430" y1="215" x2="770" y2="215" stroke="#eddfe9" stroke-width="1"/>
  <text x="600" y="236" text-anchor="middle" font-family="{SANS}" font-size="13" fill="#8b7a95">quiet craft · honest software · offline first</text>
</svg>
'''

STAT = '''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="118" viewBox="0 0 1000 118" role="img" aria-label="numbers that are true">
  <rect x="0.5" y="0.5" width="999" height="117" rx="18" fill="#fffdfe" stroke="#f2e6ef"/>
  <g font-family="Georgia,serif" font-size="30" fill="#3a2c44" text-anchor="middle">
    <text x="180" y="56">{a}</text>
    <text x="500" y="56">{b}</text>
    <text x="820" y="56">{c}</text>
  </g>
  <g font-family="{SANS}" font-size="11" letter-spacing="2" fill="#a291a8" text-anchor="middle">
    <text x="180" y="80">{al}</text>
    <text x="500" y="80">{bl}</text>
    <text x="820" y="80">{cl}</text>
  </g>
  <g stroke="#f0e4ec" stroke-width="1">
    <line x1="340" y1="28" x2="340" y2="90"/>
    <line x1="660" y1="28" x2="660" y2="90"/>
  </g>
  <rect x="1" y="1" width="998" height="116" rx="18" fill="none" stroke="#f6dceb" stroke-width="0">
    <animate attributeName="stroke-width" values="0;0" dur="1s"/>
  </rect>
</svg>
'''

HAIR = '''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="26" viewBox="0 0 1000 26" role="img" aria-label="separator">
  <line x1="0" y1="13" x2="452" y2="13" stroke="#efe3ec" stroke-width="1"/>
  <line x1="548" y1="13" x2="1000" y2="13" stroke="#efe3ec" stroke-width="1"/>
  <g transform="translate(492 6)">
    <circle cx="8" cy="7" r="2.2" fill="#e6a9c4"/>
    <circle cx="8" cy="7" r="5.5" fill="none" stroke="#f4dae7" stroke-width="1">
      <animate attributeName="r" values="5.5;7.5;5.5" dur="3.4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.9;0.2;0.9" dur="3.4s" repeatCount="indefinite"/>
    </circle>
  </g>
</svg>
'''
Path(OUT / "hero.svg").write_text(HERO, encoding="utf-8")
Path(OUT / "stats.svg").write_text(STAT.format(SANS=SANS, a="51k+", al="PYPI DOWNLOADS SINCE JUNE", b="6", bl="PUBLIC PROJECTS", c="0", cl="ACCOUNTS REQUIRED"), encoding="utf-8")
Path(OUT / "hairline.svg").write_text(HAIR, encoding="utf-8")
print("hero + stats + hairline written")

BARS = [("py3dgame 0.6", 62, "#e9a8c4"), ("editor &amp; docs", 18, "#b6a6ea"), ("next engine steps", 8, "#9ecfc2")]
rows, y = [], 52
for label, pct, colour in BARS:
    rows.append(f'  <text x="60" y="{y}" font-family="{SANS}" font-size="13" fill="#5d4c68">{label}</text>')
    rows.append(f'  <rect x="230" y="{y - 10}" width="700" height="6" rx="3" fill="#f3ecf3"/>')
    rows.append(f'  <rect x="230" y="{y - 10}" width="0" height="6" rx="3" fill="{colour}">'
                f'<animate attributeName="width" values="0;{int(700 * pct / 100)}" dur="1.8s" fill="freeze"/></rect>')
    rows.append(f'  <text x="944" y="{y}" font-family="{SANS}" font-size="11" fill="#b3a5bd">{pct}%</text>')
    y += 30

ROADMAP = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="152" viewBox="0 0 1000 152" role="img" aria-label="where the work stands">
  <rect x="0.5" y="0.5" width="999" height="151" rx="18" fill="#fffdfe" stroke="#f2e6ef"/>
  <text x="60" y="26" font-family="{SANS}" font-size="11" letter-spacing="2" fill="#a291a8">WHERE THE WORK STANDS</text>
{chr(10).join(rows)}
  <text x="60" y="140" font-family="{SANS}" font-size="11" fill="#b3a5bd">measured against the 1.0 roadmap, not against vibes</text>
</svg>
'''
Path(OUT / "roadmap.svg").write_text(ROADMAP, encoding="utf-8")
print("roadmap written")

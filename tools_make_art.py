"""Generate the animated set pieces for the profile README."""
from pathlib import Path

OUT = Path("profile-readme/assets/art")
OUT.mkdir(parents=True, exist_ok=True)

WORDMARK = '''<svg xmlns="http://www.w3.org/2000/svg" width="560" height="118" viewBox="0 0 560 118" role="img" aria-label="Dev2Creator">
  <defs>
    <linearGradient id="w" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#d9608c"><animate attributeName="offset" values="-0.2;1.2" dur="6s" repeatCount="indefinite"/></stop>
      <stop offset="0.5" stop-color="#8b6cd9"><animate attributeName="offset" values="0.3;1.7" dur="6s" repeatCount="indefinite"/></stop>
      <stop offset="1" stop-color="#d9608c"><animate attributeName="offset" values="0.8;2.2" dur="6s" repeatCount="indefinite"/></stop>
    </linearGradient>
    <clipPath id="clip"><text x="280" y="76" text-anchor="middle" font-family="Georgia,'Times New Roman',serif" font-size="62" font-weight="700">Dev2Creator</text></clipPath>
  </defs>
  <text x="280" y="76" text-anchor="middle" font-family="Georgia,'Times New Roman',serif" font-size="62" font-weight="700" fill="url(#w)">Dev2Creator</text>
  <g clip-path="url(#clip)">
    <rect x="-140" y="10" width="90" height="80" fill="#ffffff" opacity="0.55" transform="skewX(-18)">
      <animate attributeName="x" values="-140;620" dur="4.6s" repeatCount="indefinite"/>
    </rect>
  </g>
  <text x="280" y="104" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="13" fill="#a291a8" letter-spacing="3">LITTLE IDEAS · REAL CREATIONS</text>
  <g fill="#f3a5c0">
    <path d="M96 44c0-6 9-6 9 0 0 6-9 10-9 10s-9-4-9-10c0-6 9-6 9 0z"><animate attributeName="opacity" values="0.2;1;0.2" dur="3.1s" repeatCount="indefinite"/></path>
    <path d="M470 62c0-6 9-6 9 0 0 6-9 10-9 10s-9-4-9-10c0-6 9-6 9 0z"><animate attributeName="opacity" values="1;0.25;1" dur="3.6s" repeatCount="indefinite"/></path>
  </g>
  <path d="M452 30l1.8 4.6 4.6 1.8-4.6 1.8-1.8 4.6-1.8-4.6-4.6-1.8 4.6-1.8z" fill="#c3b5f0">
    <animate attributeName="opacity" values="0.3;1;0.3" dur="2.6s" repeatCount="indefinite"/>
  </path>
</svg>
'''

LINES = [
    ("$ whoami", "dev2creator — small tools, honest docs", 0),
    ("$ ls projects/", "IRL-  cutie-os  py3dgame  IRL-WISDOM  irl-besty  TransPower", 1.1),
    ("$ cat motto.txt", '"Imagine. Build. Experiment."', 2.3),
]

rows = []
y = 74
for cmd, out, delay in LINES:
    rows.append(f'  <text x="26" y="{y}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="13" fill="#8fe3c8" opacity="0">{cmd}'
                f'<animate attributeName="opacity" values="0;1" begin="{delay}s" dur="0.25s" fill="freeze"/></text>')
    rows.append(f'  <text x="26" y="{y + 20}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="13" fill="#e8e0f2" opacity="0">{out}'
                f'<animate attributeName="opacity" values="0;1" begin="{delay + 0.35}s" dur="0.3s" fill="freeze"/></text>')
    y += 48

TERMINAL = f'''<svg xmlns="http://www.w3.org/2000/svg" width="620" height="196" viewBox="0 0 620 196" role="img" aria-label="a terminal showing whoami">
  <rect x="1" y="1" width="618" height="194" rx="14" fill="#2b2233" stroke="#4a3a56"/>
  <rect x="1" y="1" width="618" height="30" rx="14" fill="#3a2f45"/>
  <rect x="1" y="20" width="618" height="11" fill="#3a2f45"/>
  <circle cx="24" cy="16" r="5" fill="#f38ba0"/><circle cx="42" cy="16" r="5" fill="#f9d7a0"/><circle cx="60" cy="16" r="5" fill="#9ee6c8"/>
  <text x="309" y="20" text-anchor="middle" font-family="ui-monospace,Menlo,monospace" font-size="11" fill="#b9a9c6">dev2creator@github: ~</text>
{chr(10).join(rows)}
  <rect x="26" y="162" width="8" height="14" fill="#8fe3c8">
    <animate attributeName="opacity" values="1;0;1" dur="1.1s" repeatCount="indefinite"/>
  </rect>
</svg>
'''
(OUT / "wordmark.svg").write_text(WORDMARK, encoding="utf-8")
(OUT / "terminal.svg").write_text(TERMINAL, encoding="utf-8")
print("wordmark + terminal written")

STATUS = '''<svg xmlns="http://www.w3.org/2000/svg" width="460" height="112" viewBox="0 0 460 112" role="img" aria-label="status card">
  <defs>
    <linearGradient id="c" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#fffafc"/><stop offset="1" stop-color="#f7f1fb"/>
    </linearGradient>
  </defs>
  <rect x="1" y="1" width="458" height="110" rx="16" fill="url(#c)" stroke="#f0cede" stroke-width="2"/>
  <circle cx="54" cy="56" r="30" fill="#fbe3ee" stroke="#f2b8d0" stroke-width="2"/>
  <text x="54" y="66" text-anchor="middle" font-size="26">🐰</text>
  <circle cx="76" cy="76" r="7" fill="#7fd9a8" stroke="#ffffff" stroke-width="2">
    <animate attributeName="r" values="6;8;6" dur="2s" repeatCount="indefinite"/>
  </circle>
  <text x="102" y="42" font-family="Helvetica,Arial,sans-serif" font-size="16" font-weight="700" fill="#3a2c44">Dev2Creator</text>
  <text x="102" y="66" font-family="Helvetica,Arial,sans-serif" font-size="13" fill="#7b6a86">building py3dgame 0.6 · offline first</text>
  <text x="102" y="88" font-family="Helvetica,Arial,sans-serif" font-size="12" fill="#a291a8">Python · AI · game engines · developer tools</text>
  <g>
    <rect x="366" y="34" width="70" height="8" rx="4" fill="#f4d9e6"/>
    <rect x="366" y="34" width="0" height="8" rx="4" fill="#e88bb0"><animate attributeName="width" values="0;58" dur="2.4s" repeatCount="indefinite"/></rect>
    <rect x="366" y="52" width="70" height="8" rx="4" fill="#e2dcf6"/>
    <rect x="366" y="52" width="0" height="8" rx="4" fill="#9b86dd"><animate attributeName="width" values="0;40" dur="3.1s" repeatCount="indefinite"/></rect>
    <rect x="366" y="70" width="70" height="8" rx="4" fill="#d8ece6"/>
    <rect x="366" y="70" width="0" height="8" rx="4" fill="#6fc7ab"><animate attributeName="width" values="0;26" dur="2.7s" repeatCount="indefinite"/></rect>
  </g>
</svg>
'''

BARS = [("py3dgame 0.6", 62, "#e88bb0"), ("editor + docs", 18, "#9b86dd"), ("next engine steps", 8, "#6fc7ab")]
rows, y = [], 40
for label, pct, colour in BARS:
    rows.append(f'  <text x="24" y="{y}" font-family="Helvetica,Arial,sans-serif" font-size="13" fill="#5d4c68">{label}</text>')
    rows.append(f'  <rect x="200" y="{y - 10}" width="300" height="10" rx="5" fill="#f1e8f4"/>')
    rows.append(f'  <rect x="200" y="{y - 10}" width="0" height="10" rx="5" fill="{colour}">'
                f'<animate attributeName="width" values="0;{int(300 * pct / 100)}" dur="1.6s" fill="freeze"/></rect>')
    y += 26

PROGRESS = f'''<svg xmlns="http://www.w3.org/2000/svg" width="540" height="128" viewBox="0 0 540 128" role="img" aria-label="where the work stands">
  <rect x="1" y="1" width="538" height="126" rx="14" fill="#fffdfe" stroke="#f0cede" stroke-width="2"/>
  <text x="24" y="24" font-family="Helvetica,Arial,sans-serif" font-size="12" fill="#a291a8" letter-spacing="1">WHERE THE WORK STANDS</text>
{chr(10).join(rows)}
</svg>
'''

SIGNATURE = '''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="90" viewBox="0 0 300 90" role="img" aria-label="signed Dev2Creator">
  <path d="M18 62c14-26 22-38 30-38 7 0 6 12-2 24-9 13-22 22-28 22-5 0-4-7 2-13 8-9 22-16 34-16"
        fill="none" stroke="#d9608c" stroke-width="3" stroke-linecap="round"
        stroke-dasharray="240" stroke-dashoffset="240">
    <animate attributeName="stroke-dashoffset" values="240;0" dur="2.6s" fill="freeze"/>
  </path>
  <path d="M96 58c10-22 20-32 27-32 6 0 5 10-1 20" fill="none" stroke="#8b6cd9" stroke-width="3" stroke-linecap="round"
        stroke-dasharray="120" stroke-dashoffset="120">
    <animate attributeName="stroke-dashoffset" values="120;0" dur="2.6s" begin="0.8s" fill="freeze"/>
  </path>
  <text x="132" y="62" font-family="Georgia,serif" font-size="22" fill="#7b5f7f" opacity="0">
    Dev2Creator
    <animate attributeName="opacity" values="0;1" begin="1.6s" dur="1s" fill="freeze"/>
  </text>
  <path d="M240 34l1.8 4.6 4.6 1.8-4.6 1.8-1.8 4.6-1.8-4.6-4.6-1.8 4.6-1.8z" fill="#f3a5c0">
    <animate attributeName="opacity" values="0.3;1;0.3" dur="2.4s" repeatCount="indefinite"/>
  </path>
</svg>
'''

(OUT / "status.svg").write_text(STATUS, encoding="utf-8")
(OUT / "progress.svg").write_text(PROGRESS, encoding="utf-8")
(OUT / "signature.svg").write_text(SIGNATURE, encoding="utf-8")
print("status + progress + signature written")

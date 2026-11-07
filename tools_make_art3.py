"""Two more interactive-feeling pieces: a hopping bunny rule and a quote carousel."""
from pathlib import Path

OUT = Path("profile-readme/assets/art")
SANS = "system-ui,-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"

# a thin rule with a tiny bunny that hops from left to right, forever
HOP = '''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="44" viewBox="0 0 1000 44" role="img" aria-label="a bunny hopping along a line">
  <line x1="0" y1="34" x2="1000" y2="34" stroke="#f0e4ec" stroke-width="1" stroke-dasharray="3 5"/>
  <g>
    <g>
      <ellipse cx="0" cy="0" rx="7" ry="6" fill="#ffffff" stroke="#d9c9d8" stroke-width="1"/>
      <ellipse cx="-3" cy="-9" rx="2" ry="6" fill="#ffffff" stroke="#d9c9d8" stroke-width="1"/>
      <ellipse cx="3" cy="-10" rx="2" ry="6" fill="#ffffff" stroke="#d9c9d8" stroke-width="1"/>
      <circle cx="-2" cy="-1" r="1" fill="#5f4f68"/>
      <circle cx="2" cy="-1" r="1" fill="#5f4f68"/>
      <circle cx="0" cy="2" r="1" fill="#f0a8c2"/>
    </g>
    <animateMotion dur="9s" repeatCount="indefinite" keyPoints="0;1" keyTimes="0;1" calcMode="linear"
                   path="M-20 30 Q120 -4 250 30 Q380 64 510 30 Q640 -4 770 30 Q900 64 1020 30"/>
  </g>
  <circle cx="20" cy="34" r="2" fill="#f2cfe0"/>
  <circle cx="980" cy="34" r="2" fill="#d6e9e2"/>
</svg>
'''

QUOTES = [
    "small steps still make a lovely journey",
    "if it is not documented, it is a rumour",
    "one thing, built well, beats ten half-built",
    "test first, then the happy dance",
    "offline first, always kind to your data",
    "the bunny believes in you",
]
parts = []
total = 13.2
for idx, line in enumerate(QUOTES):
    begin = round(idx * total / len(QUOTES), 2)
    parts.append(
        f'  <text x="500" y="62" text-anchor="middle" font-family="Georgia,serif" font-size="19" font-style="italic" fill="#6b5875" opacity="0">'
        f'{line}'
        f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.06;0.9;1" begin="{begin}s" dur="{total}s" repeatCount="indefinite"/></text>'
    )

CAROUSEL = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="118" viewBox="0 0 1000 118" role="img" aria-label="little notes from the bunny">
  <defs>
    <linearGradient id="card" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#fffdfe"/><stop offset="1" stop-color="#fbf5fb"/>
    </linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="999" height="117" rx="20" fill="url(#card)" stroke="#f2e2ee"/>
  <text x="500" y="30" text-anchor="middle" font-family="{SANS}" font-size="10" letter-spacing="3" fill="#bda9c6">A LITTLE BUNNY REMINDER</text>
{chr(10).join(parts)}
  <g fill="#f3c3d4">
    <path d="M472 102c0-4 6-4 6 0 0 4-6 7-6 7s-6-3-6-7c0-4 6-4 6 0z">
      <animate attributeName="opacity" values="0.25;1;0.25" dur="3.2s" repeatCount="indefinite"/>
    </path>
    <path d="M522 102c0-4 6-4 6 0 0 4-6 7-6 7s-6-3-6-7c0-4 6-4 6 0z">
      <animate attributeName="opacity" values="1;0.3;1" dur="3.2s" repeatCount="indefinite"/>
    </path>
  </g>
</svg>
'''
Path(OUT / "bunny-rule.svg").write_text(HOP, encoding="utf-8")
Path(OUT / "bunny-notes.svg").write_text(CAROUSEL, encoding="utf-8")
print("bunny-rule + bunny-notes written")

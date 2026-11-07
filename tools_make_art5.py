"""Second pass art: an expressive hero and a flagship card."""
from pathlib import Path

OUT = Path("profile-readme/assets/art")
SER = "Georgia,'Iowan Old Style','Times New Roman',serif"
SAN = "system-ui,-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"

HERO = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="420" viewBox="0 0 1120 420" role="img" aria-label="Dev2Creator, a quiet corner of thoughtful software">
  <defs>
    <linearGradient id="paper" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#fffdfa"/><stop offset="0.45" stop-color="#fdf7f8"/><stop offset="1" stop-color="#f7f4fc"/>
    </linearGradient>
    <radialGradient id="blush" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#fbe0e9" stop-opacity="0.85"/><stop offset="1" stop-color="#fbe0e9" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="orchid" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#e9e0fb" stop-opacity="0.8"/><stop offset="1" stop-color="#e9e0fb" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="sage" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#e6f0e8" stop-opacity="0.75"/><stop offset="1" stop-color="#e6f0e8" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="1120" height="420" fill="url(#paper)"/>
  <circle cx="180" cy="90" r="210" fill="url(#blush)">
    <animate attributeName="cx" values="180;214;180" dur="17s" repeatCount="indefinite"/>
  </circle>
  <circle cx="960" cy="330" r="230" fill="url(#orchid)">
    <animate attributeName="cx" values="960;920;960" dur="21s" repeatCount="indefinite"/>
  </circle>
  <circle cx="880" cy="60" r="150" fill="url(#sage)">
    <animate attributeName="cy" values="60;84;60" dur="19s" repeatCount="indefinite"/>
  </circle>

  <g stroke="#d7c3d2" stroke-width="1.1" fill="none" stroke-linecap="round">
    <path d="M74 330c40-6 62-28 66-62"/>
    <path d="M108 296c14-4 24-16 26-30"/>
    <path d="M92 314c-16-2-28-12-32-26"/>
  </g>
  <g fill="#f7d3e0" stroke="#e9b9cb" stroke-width="0.8">
    <circle cx="140" cy="268" r="9"/><circle cx="152" cy="280" r="7"/><circle cx="128" cy="284" r="6"/>
    <circle cx="60" cy="288" r="7"/><circle cx="46" cy="302" r="5.5"/>
  </g>
  <g fill="#f3e6f9" stroke="#e3cfe8" stroke-width="0.8">
    <circle cx="146" cy="252" r="5"/><circle cx="100" cy="270" r="4.5"/>
  </g>

  <g transform="translate(1030 96)" fill="#d9a7bd">
    <path d="M0 -12l3.4 8.6 8.6 3.4-8.6 3.4-3.4 8.6-3.4-8.6-8.6-3.4 8.6-3.4z"><animate attributeName="opacity" values="0.35;1;0.35" dur="6.5s" repeatCount="indefinite"/></path>
  </g>
  <g transform="translate(986 316)" fill="#c9bce8">
    <path d="M0 -8l2.4 5.6 5.6 2.4-5.6 2.4-2.4 5.6-2.4-5.6-5.6-2.4 5.6-2.4z"><animate attributeName="opacity" values="1;0.3;1" dur="7.4s" repeatCount="indefinite"/></path>
  </g>

  <g transform="translate(560 118)" stroke="#5b4a63" stroke-width="1.7" fill="none" stroke-linecap="round">
    <path d="M-13 -8c-1-9-2-14-2-19"/><path d="M11 -8c1-9 2-14 2-19"/>
    <path d="M-17 4a17 16 0 0 0 34 0 17 16 0 0 0 -34 0z" fill="#fffdfa"/>
    <path d="M-17 4a17 16 0 0 0 34 0" fill="none"/>
    <circle cx="-6" cy="2" r="1.7" fill="#5b4a63" stroke="none"/>
    <circle cx="6" cy="2" r="1.7" fill="#5b4a63" stroke="none"/>
    <circle cx="0" cy="9" r="1.6" fill="#d98aa8" stroke="none"/>
    <circle cx="-13" cy="10" r="2.6" fill="#f9dbe6" stroke="none"/>
    <circle cx="13" cy="10" r="2.6" fill="#f9dbe6" stroke="none"/>
  </g>

  <text x="560" y="196" text-anchor="middle" font-family="{SER}" font-size="64" font-weight="400" letter-spacing="1.2" fill="#3b2e42">Dev2Creator</text>
  <line x1="300" y1="228" x2="452" y2="228" stroke="#e8d9e2"/>
  <text x="560" y="233" text-anchor="middle" font-family="{SAN}" font-size="11" letter-spacing="4.6" fill="#9a8aa3">POLITE TO MACHINES · KIND TO PEOPLE</text>
  <line x1="668" y1="228" x2="820" y2="228" stroke="#e8d9e2"/>
  <text x="560" y="268" text-anchor="middle" font-family="{SER}" font-size="19" font-style="italic" fill="#6d5b76">small tools, made carefully</text>
  <text x="560" y="298" text-anchor="middle" font-family="{SAN}" font-size="13" fill="#8b7a95">Python · AI · game engines · developer tools</text>
  <g stroke="#ecdfe8" stroke-width="1">
    <line x1="470" y1="330" x2="650" y2="330"/>
  </g>
  <text x="560" y="356" text-anchor="middle" font-family="{SAN}" font-size="11.5" letter-spacing="2.4" fill="#a798ae">DOCUMENTED HONESTLY · OFFLINE FIRST</text>
</svg>
'''

FLAG = f'''<svg xmlns="http://www.w3.org/2000/svg" width="680" height="250" viewBox="0 0 680 250" role="img" aria-label="py3dgame, the flagship project">
  <defs>
    <linearGradient id="card" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#fdfaff"/><stop offset="0.55" stop-color="#f8f4fe"/><stop offset="1" stop-color="#f6f0fb"/>
    </linearGradient>
    <radialGradient id="halo" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#e6d8fa" stop-opacity="0.9"/><stop offset="1" stop-color="#e6d8fa" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect x="1" y="1" width="678" height="248" rx="20" fill="url(#card)" stroke="#e8dcf0"/>
  <rect x="9" y="9" width="662" height="232" rx="14" fill="none" stroke="#f0e6f4"/>
  <circle cx="560" cy="70" r="110" fill="url(#halo)"/>
  <text x="42" y="52" font-family="{SAN}" font-size="10" letter-spacing="3.4" fill="#b08bc4">FLAGSHIP</text>
  <text x="42" y="100" font-family="{SER}" font-size="38" font-weight="400" fill="#3b2e42">py3dgame</text>
  <text x="42" y="128" font-family="{SER}" font-size="15.5" font-style="italic" fill="#6d5b76">a Python-native game library, built to be understood</text>
  <text x="42" y="156" font-family="{SAN}" font-size="12.5" fill="#8b7a95">window · fixed-timestep loop · input · scene graph · software 2D renderer</text>
  <g stroke="#d9cbe4" stroke-width="1"><line x1="42" y1="176" x2="630" y2="176"/></g>
  <text x="42" y="200" font-family="{SAN}" font-size="12" fill="#7d6b86">55 tests</text>
  <text x="120" y="200" font-family="{SAN}" font-size="12" fill="#c3b3c9">·</text>
  <text x="136" y="200" font-family="{SAN}" font-size="12" fill="#7d6b86">no GPU required</text>
  <text x="252" y="200" font-family="{SAN}" font-size="12" fill="#c3b3c9">·</text>
  <text x="268" y="200" font-family="{SAN}" font-size="12" fill="#7d6b86">3D pipeline in development</text>
  <g transform="translate(560 128)" stroke="#a98cc4" stroke-width="1.4" fill="none" opacity="0.85">
    <path d="M0 -42l46 24-46 24-46-24z" fill="#efe4fb"/>
    <path d="M-46 -18v36l46 24 46-24v-36"/>
    <path d="M0 6v36"/>
  </g>
</svg>
'''
(OUT / "hero-v2.svg").write_text(HERO, encoding="utf-8")
(OUT / "flagship.svg").write_text(FLAG, encoding="utf-8")
print("hero-v2 + flagship written")

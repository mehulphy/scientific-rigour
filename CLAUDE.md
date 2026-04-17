# Scientific Rigour — Claude Briefing

Physics and mathematics explainer videos built with ManimCE. Public GitHub repo. Quality-focused.

---

## Repository Layout

```
scientific-rigour/
├── CLAUDE.md              ← you are here; update this at the end of each session
├── TOC.md                 ← table of contents by domain; add entries as videos ship
├── config/
│   └── theme.py           ← SRScene base class + shared palette/fonts
├── templates/
│   ├── script.md          ← script template
│   └── scene.py           ← scene template
├── assets/                ← shared images, SVGs, etc.
└── YYYY/MM/video-slug/
    ├── script.md
    └── scenes/
        ├── scene_01.py
        ├── scene_02.py
        └── ...
```

Rendered `.mp4` files are gitignored. Renders live in a local `media/` directory.

---

## Starting a New Video

1. Create `YYYY/MM/video-slug/script.md` from `templates/script.md`
2. Discuss and finalize the script before touching any code
3. Build scenes one at a time in `scenes/scene_NN.py`
4. Add an entry to `TOC.md` when the video ships
5. Update this file with the new video's status

---

## Script Format

Each scene section follows this pattern:

```markdown
## Scene NN — Title

### Beat N — Beat title

**VOICEOVER**
Narration text here.

**VISUAL**
Description of what appears on screen.
```

- Scenes are broken into **beats** — each beat is a 2–4 line voiceover chunk paired with a matching visual description.
- No `>` blockquote markers on voiceover lines.
- Voiceover text must NOT be modified without explicit discussion with the user.

---

## Scene Code Conventions

- Every scene class inherits from `SRScene` (not bare `Scene`)
- Import path boilerplate at the top of every scene file:
  ```python
  import sys
  import os
  sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "config"))
  from manim import *
  from theme import SRScene, PRIMARY, ACCENT_BLUE, ACCENT_GOLD, ACCENT_RED, ACCENT_GREEN, MUTED
  ```
- One scene class per file, named `SceneNN` (e.g. `Scene01`)
- End every scene with `self.play(FadeOut(*self.mobjects))` + a short wait

## Color Palette (`config/theme.py`)

| Name          | Hex       | Use                                  |
|---------------|-----------|--------------------------------------|
| `PRIMARY`     | `#FFFFFF` | Main text, labels, default elements  |
| `ACCENT_BLUE` | `#58A6FF` | Key quantities, highlights           |
| `ACCENT_GOLD` | `#F0C040` | Secondary emphasis (e.g. r vector)   |
| `ACCENT_RED`  | `#FF6B6B` | Warnings, contrast, angles (θ)       |
| `ACCENT_GREEN`| `#3DDC84` | Positive results, y-axis elements    |
| `MUTED`       | `#6E7681` | Axes, grid lines, auxiliary elements |
| `BACKGROUND`  | `#0D1117` | Scene background (deep near-black)   |

## Rendering

```bash
cd YYYY/MM/video-slug
manim -pql scenes/scene_01.py Scene01   # preview, 15fps — too choppy for motion review
manim -pqm scenes/scene_01.py Scene01   # preview, 30fps — use this for motion review
manim -pqh scenes/scene_01.py Scene01   # preview, high quality
manim -qk  scenes/scene_01.py Scene01   # 4K render
```

Use `-pqm` (30fps) as the default preview quality — `-pql` at 15fps makes circular motion look choppy/dragging.

Post-production (voiceover merge) in DaVinci Resolve.

---

## Videos in Progress

### `2026/04/polar-coordinates-circular-motion` — Why Polar Coordinates?

**Status**: Script finalized. Scene 01 coded. Render with pure white theme not yet confirmed by user — verify at next session start.

| Scene | Title                              | Code status             |
|-------|------------------------------------|-------------------------|
| 01    | Two Ways to Describe a Point       | Coded, render unverified|
| 02    | Describing the Circle in Cartesian | Not started             |
| 03    | Both Coordinates Change. Always.   | Not started             |
| 04    | A Different Perspective: Polar     | Not started             |
| 05    | The Key Insight: r Does Not Change | Not started             |
| 06    | Velocity in Polar Coordinates      | Not started             |
| 07    | Side-by-Side: The Contrast         | Not started             |
| 08    | Closing: Symmetry & Coord Choice   | Not started             |

**Scene 01 beat structure** (6 beats):
1. Title card fades in/out
2. Particle P appears → circle draws → particle moves (first half of revolution)
3. `v = ?` appears mid-revolution via `self.add()` (no pause) → particle completes revolution and stops
4. "Freeze time" — particle color changes to PRIMARY, short wait
5. X and Y axes appear
6. Dashed perpendiculars to axes, foot labels x/y, `P = (x, y)` label

**Open questions from script:**
- Scene 03: include x(t)/y(t) side graphs, or too much at once?
- Scene 07: true split-screen, or back-and-forth transition?
- Scene 06: introduce r̂ and θ̂ unit vectors here, or save for a follow-up video?

---

## Shipped Videos

_(none yet)_

---

## Session Hygiene

At the end of each session, update the table above (scenes completed, open questions resolved) so the next session starts with accurate state.

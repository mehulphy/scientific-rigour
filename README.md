# Scientific Rigour

Explanation videos for physics and mathematics, built with [ManimCE](https://www.manim.community/).

## Repository Structure

```
scientific-rigour/
├── config/
│   └── theme.py          # Shared visual identity (colors, fonts, styles)
├── templates/
│   ├── script.md         # Script template (voiceover + visual blocks)
│   └── scene.py          # Manim scene template
├── TOC.md                # Table of contents by domain
└── YYYY/
    └── MM/
        └── video-slug/
            ├── script.md          # Script for this video
            └── scenes/
                ├── scene_01.py
                ├── scene_02.py
                └── ...
```

Rendered outputs (`.mp4`) are excluded from version control and can always be recreated.

## Rendering a Scene

```bash
manim -pql scenes/scene_01.py SceneName      # preview, low quality
manim -pqh scenes/scene_01.py SceneName      # preview, high quality
manim -qk  scenes/scene_01.py SceneName      # 4K render
```

Renders are saved to a local `renders/` directory (gitignored).

## Setup

```bash
pip install manim
```

## Visual Style

All scenes inherit from `SRScene` in `config/theme.py` for a consistent look.

---
name: Scientific Rigour project setup
description: Project structure, conventions, and tooling for the Manim physics/math video channel
type: project
---

Using ManimCE (community edition) with option to move to manimgl if capability limits are hit.

Directory layout: `YYYY/MM/video-slug/` with a `script.md` and `scenes/` subdirectory per video.

All scenes inherit from `SRScene` in `config/theme.py` which sets background color and provides convenience methods.

Script format: Markdown with alternating `> VOICEOVER` blockquotes and `**VISUAL**` prose blocks, one `## Scene NN` per section.

Renders are local only — gitignored. Separate clips per scene for flexible post-production.

Editing software: DaVinci Resolve recommended for voiceover merge.

**Why:** User wants scalable content creation pipeline, public GitHub repo, quality-focused.

**How to apply:** When creating new videos, always create the script first in this format, discuss and finalize it, then build scenes. Keep theme consistent via SRScene.

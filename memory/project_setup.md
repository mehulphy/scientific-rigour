---
name: Scientific Rigour project setup
description: Project structure, conventions, and tooling for the Manim physics/math video channel
type: project
---

Using ManimCE (community edition) v0.19.0. ManimGL was tried and abandoned — macOS rendering issues, interactive window didn't work reliably.

Directory layout: `YYYY/MM/video-slug/` with a `script.md` and `scenes/` subdirectory per video.

All scenes inherit from `SRScene` in `config/theme.py` which sets background color and provides convenience methods.

Script format: Beat-based Markdown. Each scene has numbered beats (`### Beat N — Title`). Each beat has a plain `**VOICEOVER**` block (no `>` blockquotes) and a `**VISUAL**` block. Voiceover text must never be modified without explicit user approval.

Render quality: use `-pqm` (30fps) for motion review — `-pql` at 15fps makes circular motion look choppy.

Renders are local only — gitignored. Separate clips per scene for flexible post-production.

Editing software: DaVinci Resolve for voiceover merge.

**Why:** User wants scalable content creation pipeline, public GitHub repo, quality-focused.

**How to apply:** Script first, discuss and finalize all beats, then build scenes one at a time. Keep theme consistent via SRScene. Never touch voiceover text without discussion.

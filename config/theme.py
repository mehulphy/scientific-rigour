from manim import *

# ── Palette ──────────────────────────────────────────────────────────────────
BACKGROUND   = "#0D1117"   # deep near-black
PRIMARY      = "#E8E8E8"   # off-white for main text / labels
ACCENT_BLUE  = "#58A6FF"   # highlights, key quantities
ACCENT_GOLD  = "#F0C040"   # secondary highlights, emphasis
ACCENT_RED   = "#FF6B6B"   # warnings, negatives, contrast
ACCENT_GREEN = "#3DDC84"   # positives, results
MUTED        = "#6E7681"   # grid lines, auxiliary elements

# ── Typography ────────────────────────────────────────────────────────────────
# ManimCE uses LaTeX for math and Pango/Cairo for text.
# Override default font here; keep it clean and legible on screen.
DEFAULT_FONT = "Helvetica Neue"   # fallback: "sans-serif"

# ── Base Scene ────────────────────────────────────────────────────────────────
class SRScene(Scene):
    """Base scene for all Scientific Rigour videos.
    Inherit from this instead of Scene to get consistent styling."""

    def setup(self):
        self.camera.background_color = BACKGROUND

    # Convenience: styled text label
    def label(self, text, color=PRIMARY, scale=0.6, **kwargs):
        return Text(text, color=color, font=DEFAULT_FONT, **kwargs).scale(scale)

    # Convenience: styled math
    def math(self, tex, color=PRIMARY, **kwargs):
        return MathTex(tex, color=color, **kwargs)

    # Convenience: section title that fades in at top
    def show_title(self, text, duration=1.0):
        t = self.label(text, scale=0.8).to_edge(UP)
        self.play(FadeIn(t), run_time=duration)
        return t

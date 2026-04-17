from manim import *

# ── Palette ──────────────────────────────────────────────────────────────────
BACKGROUND   = "#0D1117"   # deep near-black
PRIMARY      = "#FFFFFF"   # pure white for main text / labels
ACCENT_BLUE  = "#58A6FF"   # highlights, key quantities
ACCENT_GOLD  = "#F0C040"   # secondary highlights, emphasis
ACCENT_RED   = "#FF6B6B"   # warnings, negatives, contrast
ACCENT_GREEN = "#3DDC84"   # positives, results
MUTED        = "#6E7681"   # grid lines, auxiliary elements

# ── Typography ────────────────────────────────────────────────────────────────
DEFAULT_FONT = "Helvetica Neue"

# ── Base Scene ────────────────────────────────────────────────────────────────
class SRScene(Scene):

    def setup(self):
        self.camera.background_color = BACKGROUND

    def label(self, text, color=PRIMARY, scale=0.6, **kwargs):
        return Text(text, color=color, font=DEFAULT_FONT, **kwargs).scale(scale)

    def math(self, tex, color=PRIMARY, **kwargs):
        return Tex(tex, color=color, **kwargs)

    def show_title(self, text, duration=1.0):
        t = self.label(text, scale=0.8).to_edge(UP)
        self.play(FadeIn(t), run_time=duration)
        return t

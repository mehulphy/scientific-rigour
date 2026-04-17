import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "config"))

from manim import *
from theme import SRScene, ACCENT_BLUE, ACCENT_GOLD, ACCENT_GREEN, ACCENT_RED, MUTED, PRIMARY


class Scene01(SRScene):
    """Scene 01 — [Scene Name]

    VISUAL: [Paste visual description from script.md here for reference]
    """

    def construct(self):
        # ── build objects ──────────────────────────────────────────────
        title = self.show_title("Scene Title")

        eq = self.math(r"E = mc^2").scale(1.4)

        # ── animate ───────────────────────────────────────────────────
        self.play(Write(eq))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(eq))
        self.wait(0.5)

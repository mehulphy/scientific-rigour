import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "config"))

from manim import *
from theme import SRScene, PRIMARY, ACCENT_BLUE, ACCENT_RED, ACCENT_GREEN, MUTED


class Scene01(SRScene):

    def construct(self):

        # ── Beat 1: Title card ─────────────────────────────────────────
        title = Text("Why Polar Coordinates?", color=PRIMARY, font="Palatino").scale(0.85)
        self.play(FadeIn(title, run_time=0.8))
        self.wait(2.0)
        self.play(FadeOut(title, run_time=0.6))
        self.wait(0.4)

        # ── Beat 2: Particle P appears, circle draws, P moves ──────────
        RADIUS = 2.0
        START_ANGLE = PI / 4  # 45° in first quadrant

        def pos_on_circle(angle):
            return np.array([RADIUS * np.cos(angle), RADIUS * np.sin(angle), 0])

        p_dot = Dot(pos_on_circle(START_ANGLE), color=ACCENT_BLUE, radius=0.1, z_index=1)
        p_label = MathTex("P", color=PRIMARY).scale(0.7).next_to(p_dot, UR, buff=0.12)

        self.play(FadeIn(p_dot), FadeIn(p_label))
        self.wait(0.5)

        circle = Circle(radius=RADIUS, color=MUTED, stroke_width=2)
        self.play(Create(circle), run_time=1.2)
        self.wait(0.2)

        # Hide label during motion — avoids one-frame lag drag
        self.play(FadeOut(p_label), run_time=0.2)

        # ValueTracker for smooth circular motion
        angle_tracker = ValueTracker(START_ANGLE)
        p_dot.add_updater(lambda d: d.move_to(pos_on_circle(angle_tracker.get_value())))

        # First half of revolution
        self.play(angle_tracker.animate.set_value(START_ANGLE + PI), run_time=5.0, rate_func=linear)

        # ── Beat 3: Goal — v = ? (particle is mid-revolution, no pause) ─
        v_question = MathTex("v = ?", color=ACCENT_RED).scale(0.9)
        v_question.to_corner(UR).shift(LEFT * 0.6 + DOWN * 0.5)
        self.add(v_question)

        # Second half of revolution — completes back at START_ANGLE
        self.play(angle_tracker.animate.set_value(START_ANGLE + TAU), run_time=5.0, rate_func=linear)
        p_dot.clear_updaters()

        # Restore label at frozen position
        p_label = MathTex("P", color=PRIMARY).scale(0.7).next_to(p_dot, UR, buff=0.12)
        self.play(FadeIn(p_label), run_time=0.3)

        # ── Beat 4: Freeze the particle ────────────────────────────────
        self.play(p_dot.animate.set_color(PRIMARY), run_time=0.4)
        self.wait(0.8)

        # ── Beat 5: X and Y axes appear ────────────────────────────────
        x_axis = Arrow(LEFT * 5.0, RIGHT * 5.0, color=PRIMARY, buff=0, stroke_width=2, tip_length=0.2)
        y_axis = Arrow(DOWN * 3.2, UP * 3.2, color=PRIMARY, buff=0, stroke_width=2, tip_length=0.2)
        x_axis_label = MathTex("X", color=PRIMARY).scale(0.6).next_to(x_axis, RIGHT, buff=0.15)
        y_axis_label = MathTex("Y", color=PRIMARY).scale(0.6).next_to(y_axis, UP, buff=0.15)

        self.play(
            Create(x_axis), Create(y_axis),
            FadeIn(x_axis_label), FadeIn(y_axis_label),
            run_time=0.8
        )
        self.wait(1.0)

        # ── Beat 6: Dashed perpendiculars, foot labels, P = (x, y) ────
        P = pos_on_circle(START_ANGLE)
        P_on_x = np.array([P[0], 0, 0])
        P_on_y = np.array([0, P[1], 0])

        dash_to_x = DashedLine(P, P_on_x, color=ACCENT_BLUE, dash_length=0.12, stroke_width=2)
        dash_to_y = DashedLine(P, P_on_y, color=ACCENT_GREEN, dash_length=0.12, stroke_width=2)

        x_foot_label = MathTex("x", color=ACCENT_BLUE).scale(0.6).next_to(P_on_x, DOWN, buff=0.18)
        y_foot_label = MathTex("y", color=ACCENT_GREEN).scale(0.6).next_to(P_on_y, LEFT, buff=0.18)

        self.play(Create(dash_to_x), FadeIn(x_foot_label), run_time=0.7)
        self.play(Create(dash_to_y), FadeIn(y_foot_label), run_time=0.7)

        cartesian_eq = MathTex("P = (x,\\ y)", color=PRIMARY).scale(0.75)
        cartesian_eq.to_corner(UL).shift(RIGHT * 0.4 + DOWN * 0.4)
        self.play(Write(cartesian_eq))
        self.wait(2.5)

        # ── Fade out ───────────────────────────────────────────────────
        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(0.5)

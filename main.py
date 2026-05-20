from manim import *
import numpy as np

class UnitCircle(Scene):
    def construct(self):

        plane = NumberPlane(
            x_range=[-.5, .5, 1],
            y_range=[-.5, .5, 1],
            x_length=7,
            y_length=7,
            background_line_style={
                "stroke_opacity": 1
            },
            axis_config={
                "stroke_opacity": 0
            }
        )

        self.play(Create(plane))
        self.wait()

        circle = Circle(radius=2, color=BLUE)
        self.play(Create(circle))
        self.wait()

        theta = ValueTracker(0)

        dot = always_redraw(
            lambda: Dot(
                point=[
                    2 * np.cos(theta.get_value()),
                    2 * np.sin(theta.get_value()),
                    0
                ],
                color=YELLOW
            )
        )

        self.play(FadeIn(dot))

        self.play(
            theta.animate.set_value(2 * PI),
            run_time=5,
            rate_func=linear
        )

        self.wait()
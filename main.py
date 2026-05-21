from manim import *
import numpy as np


class UnitCircle(Scene):
    def construct(self):

        # CREATE BACKGROUND PLANE
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

        # CREATE UNIT CIRCLE
        circle_radius = 3

        circle = Circle(
            radius=circle_radius,
            color=TEAL
        )

        # CREATE ANIMATED VARIABLES
        theta = ValueTracker(0)

        # CREATE MOVING POINT ON CIRCLE
        dot = always_redraw(
            lambda: Dot(
                point=[
                    circle_radius * np.cos(theta.get_value()),
                    circle_radius * np.sin(theta.get_value()),
                    0
                ],
                color=YELLOW
            )
        )

        # CREATE RADIUS LINE
        radius_line = always_redraw(
            lambda: DashedLine(
                start=ORIGIN,
                end=dot.get_center(),
                color=WHITE
            )
        )

        # CREATE COORDINATE TEXT
        coordinate_text = always_redraw(
            lambda: Text(
                f"({np.cos(theta.get_value()):.2f}, "
                f"{np.sin(theta.get_value()):.2f})",
                font_size=32
            ).to_corner(UR)
        )

        # CREATE PROJECTION LINE
        x_projection_line = always_redraw(
            lambda: DashedLine(
                start=dot.get_center(),
                end=[dot.get_center()[0], 0, 0],
                color=RED
            )
        )

        # CREATE THETA ARC
        theta_arc = always_redraw(
            lambda: Arc(
                radius=1,
                start_angle=90 * DEGREES,
                angle=theta.get_value(),
                arc_center=ORIGIN
            )
        )

        # CREATE ARC LABEL
        theta_label = always_redraw(
            lambda: Text(
                f"{theta.get_value() * (180 / PI):.0f}",
                font_size=24
            ).move_to([
                1.4 * np.cos(theta.get_value() - (PI / 12)),
                1.4 * np.sin(theta.get_value() - (PI / 12)),
                0
            ])
        )

        # DRAW STATIC OBJECTS
        self.add(plane)
        self.play(Create(circle))

        # DRAW DYNAMIC OBJECTS
        self.play(Create(dot))
        self.play(Create(radius_line))
        self.play(Create(coordinate_text))
        self.play(Create(x_projection_line))
        # self.play(Create(theta_arc))
        # self.play(Create(theta_label))

        # ANIMATE DOT AROUND CIRCLE
        self.play(
            theta.animate.set_value(PI / 2),
            run_time=5,
            rate_func=there_and_back
        )

        # END SCENE
        self.wait()
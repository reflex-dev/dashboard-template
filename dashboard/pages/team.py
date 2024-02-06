import reflex as rx

from dashboard.navigation import dashboard_sidebar, navbar
from dashboard.styles import BACKGROUND_COLOR, FONT_FAMILY


def team() -> rx.Component:
    return rx.box(
        dashboard_sidebar,
        rx.box(
            navbar(heading="Team"),
            rx.box(
                rx.text("placeholder"),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            padding_left="250px",
        ),
        background_color=BACKGROUND_COLOR,
        font_family=FONT_FAMILY,
        padding_bottom="4em",
    )

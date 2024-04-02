"""The main index page."""

import reflex as rx
from dashboard.data import (
    line_chart_data,
    lines,
    pie_chart_data,
    area_chart_data,
    areas,
    stat_card_data,
    tabular_data,
)
from dashboard.graphs import (
    area_chart,
    line_chart,
    pie_chart,
    stat_card,
    table,
)
from dashboard.navigation import dashboard_sidebar, navbar
from dashboard.styles import BACKGROUND_COLOR, FONT_FAMILY


# Content in a grid layout.


def content_grid():
    return rx.chakra.grid(
        *[rx.chakra.grid_item(stat_card(*c), col_span=1, row_span=1) for c in stat_card_data],
        rx.chakra.grid_item(
            line_chart(data=line_chart_data, data_key="name", lines=lines),
            col_span=3,
            row_span=2,
        ),
        rx.chakra.grid_item(
            pie_chart(data=pie_chart_data, data_key="value", name_key="name"),
            row_span=2,
            col_span=1,
        ),
        rx.chakra.grid_item(table(tabular_data=tabular_data), col_span=4, row_span=2),
        rx.chakra.grid_item(
            area_chart(data=area_chart_data, data_key="name", areas=areas),
            col_span=3,
            row_span=2,
        ),
        rx.chakra.grid_item(col_span=2, bg="lightgreen"),
        rx.chakra.grid_item(col_span=2, bg="yellow"),
        rx.chakra.grid_item(col_span=4, bg="orange"),
        template_columns="repeat(4, 1fr)",
        width="100%",
        gap=4,
        row_gap=8,
    )


def index() -> rx.Component:
    return rx.box(
        dashboard_sidebar,
        rx.box(
            navbar(heading="Dashboard"),
            rx.box(
                content_grid(),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            padding_left="250px",
        ),
        background_color=BACKGROUND_COLOR,
        font_family=FONT_FAMILY,
        padding_bottom="4em",
    )

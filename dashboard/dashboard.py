"""The main Dashboard App."""
from rxconfig import config

import reflex as rx
from reflex.components.radix import themes as rdxt

from dashboard.navigation import dashboard_sidebar, navbar
from dashboard.graphs import (
    Area,
    Line,
    area_chart,
    line_chart,
    pie_chart,
    stat_card,
    table,
)
from dashboard.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

from dashboard.pages.tools import tools
from dashboard.pages.team import team

# Mock data to populate the dashboard charts and tables.

stat_card_data = [
    [
        "Today's Money",
        "$53,000",
        "+2%",
    ],
    [
        "Today's Users",
        "2,300",
        "+5%",
    ],
    [
        "Today's Orders",
        "1,400",
        "-3%",
    ],
    [
        "Today's Sales",
        "$23,000",
        "+2%",
    ],
]

line_chart_data = [
    {"name": "Page A", "uv": 4000, "pv": 2400, "amt": 2400},
    {"name": "Page B", "uv": 3000, "pv": 1398, "amt": 2210},
    {"name": "Page C", "uv": 2000, "pv": 9800, "amt": 2290},
    {"name": "Page D", "uv": 2780, "pv": 3908, "amt": 2000},
    {"name": "Page E", "uv": 1890, "pv": 4800, "amt": 2181},
    {"name": "Page F", "uv": 2390, "pv": 3800, "amt": 2500},
    {"name": "Page G", "uv": 3490, "pv": 4300, "amt": 2100},
]


lines = [
    Line(data_key="pv", stroke="#8884d8"),
    Line(data_key="uv", stroke="var(--accent-8)"),
]


pie_chart_data = [
    {"name": "Group A", "value": 400, "fill": "var(--red-7)"},
    {"name": "Group B", "value": 300, "fill": "var(--green-7)"},
    {"name": "Group C", "value": 300, "fill": "var(--purple-7)"},
    {"name": "Group D", "value": 200, "fill": "var(--blue-7)"},
    {"name": "Group E", "value": 278, "fill": "var(--yellow-7)"},
    {"name": "Group F", "value": 189, "fill": "var(--pink-7)"},
]

area_chart_data = line_chart_data

areas = [
    Area(data_key="pv", stroke="#8884d8", fill="#8884d8"),
    Area(data_key="uv", stroke="var(--accent-8)", fill="var(--accent-8)"),
]


tabular_data = [
    ["Full name", "Email", "Group"],
    ["Danilo Sousa", "danilo@example.com", rdxt.badge("Developer")],
    ["Zahra Ambessa", "zahra@example.com", rdxt.badge("Admin", variant="surface")],
    ["Jasper Eriksson", "jasper@example.com", rdxt.badge("Developer")],
]


# Content in a grid layout.


def content_grid():
    return rx.grid(
        *[rx.grid_item(stat_card(*c), col_span=1, row_span=1) for c in stat_card_data],
        rx.grid_item(
            line_chart(data=line_chart_data, data_key="name", lines=lines),
            col_span=3,
            row_span=2,
        ),
        rx.grid_item(
            pie_chart(data=pie_chart_data, data_key="value", name_key="name"),
            row_span=2,
            col_span=1,
        ),
        rx.grid_item(table(tabular_data=tabular_data), col_span=4, row_span=2),
        rx.grid_item(
            area_chart(data=area_chart_data, data_key="name", areas=areas),
            col_span=3,
            row_span=2,
        ),
        rx.grid_item(col_span=2, bg="lightgreen"),
        rx.grid_item(col_span=2, bg="yellow"),
        rx.grid_item(col_span=4, bg="orange"),
        template_columns="repeat(4, 1fr)",
        width="100%",
        gap=4,
        row_gap=8,
    )


# The main index page.


def index() -> rx.Component:
    return rdxt.box(
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


# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/")
app.add_page(tools, route="/tools")
app.add_page(team, route="/team")

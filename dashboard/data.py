"""Mock data to populate the dashboard charts and tables."""

from dashboard.graphs import Area, Line
from reflex.components.radix import themes as rdxt

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

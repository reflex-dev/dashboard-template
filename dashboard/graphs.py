"""Library of customized graphs and tables for the dashboard."""
import reflex as rx


def card(*children, **props):
    return rx.card(
        *children,
        box_shadow="rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px;",
        **props,
    )


def stat_card(title: str, stat, delta) -> rx.Component:
    color = "var(--red-9)" if delta[0] == "-" else "var(--green-9)"
    arrow = "decrease" if delta[0] == "-" else "increase"
    return card(
        rx.hstack(
            rx.vstack(
                rx.text(title),
                rx.chakra.stat(
                    rx.hstack(
                        rx.chakra.stat_number(stat, color=color),
                        rx.chakra.stat_help_text(
                            rx.chakra.stat_arrow(type_=arrow), delta[1:]
                        ),
                    ),
                ),
            ),
        ),
    )


def table(tabular_data: list[list]):
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                *[rx.table.column_header_cell(cell) for cell in tabular_data[0]],
            ),
        ),
        rx.table.body(
            *[
                rx.table.row(
                    *[
                        rx.table.row_header_cell(cell)
                        if i == 0
                        else rx.table.cell(cell)
                        for i, cell in enumerate(row)
                    ],
                )
                for row in tabular_data[1:]
            ],
        ),
    )


class Line(rx.Base):
    data_key: str
    stroke: str


def line_chart(data: rx.Var | list[dict], data_key: str, lines: list[Line]):
    return card(
        rx.recharts.line_chart(
            *[
                rx.recharts.line(data_key=line.data_key, stroke=line.stroke)
                for line in lines
            ],
            rx.recharts.x_axis(data_key=data_key),
            rx.recharts.y_axis(),
            rx.recharts.legend(),
            data=data,
            height=300,
        )
    )


def pie_chart(data: rx.Var | list[dict], data_key: str, name_key: str):
    return card(
        rx.recharts.pie_chart(
            rx.recharts.pie(
                data=data,
                data_key=data_key,
                name_key=name_key,
                cx="50%",
                cy="50%",
                label=True,
            ),
            rx.recharts.legend(),
            height=300,
        )
    )


class Area(rx.Base):
    data_key: str
    stroke: str
    fill: str


def area_chart(data: rx.Var | list[dict], data_key: str, areas: list[Area]):
    return card(
        rx.recharts.area_chart(
            *[
                rx.recharts.area(
                    data_key=area.data_key, stroke=area.stroke, fill=area.fill
                )
                for area in areas
            ],
            rx.recharts.x_axis(data_key=data_key),
            rx.recharts.y_axis(),
            rx.recharts.legend(),
            data=data,
            height=400,
        )
    )

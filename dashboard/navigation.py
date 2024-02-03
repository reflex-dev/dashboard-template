import reflex as rx
from reflex.components.radix import themes as rdxt
from reflex.components import lucide

from dashboard.styles import FONT_FAMILY


def sidebar_link(text: str, href: str, icon: str) -> rdxt.Link:
    return rdxt.link(
        rdxt.flex(
            rdxt.icon_button(
                lucide.icon(tag=icon, weight=16, height=16),
                variant="soft",
            ),
            text,
            py="2",
            px="4",
            gap="4",
            align="baseline",
            direction="row",
            font_family=FONT_FAMILY,
        ),
        href=href,
        width="100%",
        border_radius="8px",
        _hover={
            "background": "rgba(255, 255, 255, 0.1)",
            "backdrop_filter": "blur(10px)",
        },
    )


def sidebar(
    *sidebar_links,
    **props,
) -> rx.Component:
    logo_src = props.get("logo_src", "/logo.jpg")
    heading = props.get("heading", "NOT SET")
    return rx.vstack(
        rx.hstack(
            rx.image(src=logo_src, height="28px", border_radius="8px"),
            rdxt.heading(
                heading,
                font_family=FONT_FAMILY,
                size="7",
            ),
            width="100%",
            spacing="1em",
        ),
        rdxt.separator(my="3"),
        rx.vstack(
            *sidebar_links,
            padding_y="1em",
        ),
        width="250px",
        position="fixed",
        height="100%",
        left="0px",
        top="0px",
        align_items="left",
        z_index="10",
        backdrop_filter="blur(10px)",
        padding="2em",
    )


dashboard_sidebar = sidebar(
    sidebar_link(text="Dashboard", href="/", icon="bar_chart_3"),
    sidebar_link(text="Tools", href="/tools", icon="settings"),
    sidebar_link(text="Team", href="/team", icon="users"),
    logo_src="/logo.jpg",
    heading="REFLEX",
)


def navbar(heading: str) -> rx.Component:
    return rx.hstack(
        rdxt.heading(heading, font_family=FONT_FAMILY, size="7"),
        rx.spacer(),
        rdxt.dropdownmenu_root(
            rdxt.dropdownmenu_trigger(
                rdxt.button(
                    "Menu",
                    lucide.icon(tag="chevron_down", weight=16, height=16),
                    font_family=FONT_FAMILY,
                    variant="soft",
                ),
            ),
            rdxt.dropdownmenu_content(
                rdxt.dropdownmenu_item("Settings"),
                rdxt.dropdownmenu_item("Profile"),
                rdxt.dropdownmenu_item("Logout"),
                font_family=FONT_FAMILY,
                variant="soft",
            ),
            variant="soft",
            font_family=FONT_FAMILY,
        ),
        position="fixed",
        width="calc(100% - 250px)",
        top="0px",
        z_index="1000",
        padding_x="2em",
        padding_top="2em",
        padding_bottom="1em",
        backdrop_filter="blur(10px)",
    )

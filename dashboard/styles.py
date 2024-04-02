"""The style classes and constants for the Dashboard App."""

from reflex.components.radix import themes as rx

THEME = rx.theme(
    appearance="light",
    has_background=True,
    radius="large",
    accent_color="iris",
    scaling="100%",
    panel_background="solid",
)

STYLESHEETS = ["https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap"]

FONT_FAMILY = "Share Tech Mono"
BACKGROUND_COLOR = "var(--accent-2)"

from rich.console import Console
from rich.style import Style

console = Console()

general_style = Style(color="green")
error_style = Style(color="#ebcb15")


def custom_print(message, error=False):
    style = error_style if error else general_style
    console.print(message, style=style)

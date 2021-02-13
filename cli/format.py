from .const import RSLV_TITLE
from rich.console import Console
from rich.table import Table

console = Console()


def print_msg(*text) -> None:
    console.print(RSLV_TITLE, *text, style="green")


def print_error(*text) -> None:
    console.print(RSLV_TITLE, *text, style="red")


def print_alias_map(alias_map: dict) -> None:
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("rslv alias")
    table.add_column("mapped path")

    for alias, path in alias_map.items():
        table.add_row(alias, path)

    console.print(table)

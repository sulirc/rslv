from rich.console import Console
from rich.table import Table

console = Console()
RSLV_TITLE = "rslv:"

def print_msg(*text) -> None:
    console.print(RSLV_TITLE, *text, style="cyan3")


def print_error(*text) -> None:
    console.print(RSLV_TITLE, *text, style="bright_red")


def print_alias_map(alias_map: dict) -> None:
    table = Table(show_header=True, header_style="bold cornflower_blue")
    table.add_column("rslv alias")
    table.add_column("mapped Path")

    for alias, path in alias_map.items():
        table.add_row(alias, path)


    console.print(table)

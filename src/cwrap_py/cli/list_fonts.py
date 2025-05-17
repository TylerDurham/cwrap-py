from typing import Annotated

import rich
import typer

from cwrap_py.core import fonts as fnt

app = typer.Typer()


def opt_list():
    return Annotated[
        bool,
        typer.Option(
            "--list",
            "-l",
            help="List the available fonts as a plain list instead of a table.",
        ),
    ]


def execute(list: bool = False):
    # print(f"FONTS! -l {list}")

    fonts = sorted(fnt.get_fonts())

    count = len(fonts)

    if list:
        for font in fonts:
            print(font)
        return
    i = 0
    cols = 6

    tbl = rich.table.Table("", "", "", "", "", "", box=None, show_header=False)

    while i < count:
        # print(*fonts[i:3])
        tbl.add_row(*fonts[i : i + cols])
        # print(f"i: {i}")
        i += cols

    rich.print(
        rich.panel.Panel(
            title="Figlet Fonts", renderable=tbl, border_style="bright_black"
        )
    )

from typing import Annotated

import rich
import typer

from cwrap_py.core import languages as lng

app = typer.Typer()


def opt_list():
    return Annotated[
        bool,
        typer.Option(
            "--list",
            "-l",
            help="List the available languages as a plain list instead of a table.",
        ),
    ]


def execute(list: bool = False):
    # print(f"LANGUAGES! -l {list}")
    languages = sorted(lng.get_languages())

    if list:
        for key in languages:
            print(key)
    else:

        table = rich.table.Table("Language", "Multiline Comments?", box=None)

        for key in languages:
            hmcc = languages[key].has_multiline_comment_chars
            row_style = "green" if hmcc else "yellow"
            table.add_row(key, str(hmcc), style=row_style)

        rich.print(
            rich.panel.Panel(
                title="Languages", renderable=table, border_style="bright_black"
            )
        )

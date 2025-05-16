# ____ _    _  ___  _   _
# |    |    |  |__]  \_/
# |___ |___ | .|      |
#

from typing import Annotated

import rich
import typer
from rich.panel import Panel
from rich.table import Table

from cwrap_py.core import do_figlet, get_languages  # do_figlet, get_languages

app = typer.Typer()


def opt_font():
    """
    Get the settings for the font option.
    """
    return typer.Option(
        "--font",
        "-f",
        help="The figlet font to use.",
        autocompletion=opt_font_completion,
    )


# TODO: Get shell completion working.
def opt_font_completion() -> []:
    """
    Get a list of fonts for completion.

    Returns:
        A list of figlet fonts.
    """
    return ["cybermedium", "cyberlarge", "cybersmall"]


def opt_language():
    """
    Get the settings for the language option.
    """
    return typer.Option(
        "--language",
        "-l",
        help="The language for the comments.",
        autocompletion=opt_language_completion,
    )


# TODO: Get shell completion working.
def opt_language_completion():
    """
    Get a list of programming languages for completion.

    Returns:
        A list of programming languages.
    """
    return ["python", "javascript", "typescript", "go", "golang", "lua"]


def opt_multiline():
    return typer.Option(
        "--multiline",
        "-m",
        help="Use a multiline comment block. Not supported for some languages.",
    )


def opt_copy_to_clipboard():
    return typer.Option("--clipboard", "-c", help="Copy output to the clipboard.")


@app.command()
def list_languages():
    languages = get_languages()

    table = Table("Language", "Multiline Comments?", box=None)

    for key in languages:
        hmcc = languages[key].has_multiline_comment_chars
        row_style = "green" if hmcc else "yellow"
        table.add_row(key, str(hmcc), style=row_style)

    rich.print(Panel(title="Languages", renderable=table, border_style="bright_black"))


@app.command()
def figlet(
    text: str,
    font: Annotated[str, opt_font()] = "cybermedium",
    language: Annotated[str, opt_language()] = "python",
    multiline: Annotated[bool, opt_multiline()] = False,
    copy_to_clipboard: Annotated[bool, opt_copy_to_clipboard()] = False,
):

    output = do_figlet(text, font, language, multiline, copy_to_clipboard)
    typer.echo(output)


def run():
    app()


if __name__ == "__main__":
    run()

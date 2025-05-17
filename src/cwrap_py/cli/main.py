# =========================================================================
# ____ _    _   / _  _ ____ _ _  _
# |    |    |  /  |\/| |__| | |\ |
# |___ |___ | /   |  | |  | | | \|
#
# =========================================================================
import typer

from cwrap_py.cli import figlet as fig
from cwrap_py.cli import list_fonts as fnt
from cwrap_py.cli import list_languages as lng

app = typer.Typer()


@app.command()
def figlet(
    text: str,
    font: fig.opt_font() = "cybermedium",
    language: fig.opt_language() = "python",
    multiline: fig.opt_multiline() = False,
    clipboard: fig.opt_clipboard() = False,
):
    """
    Generates a simple comment wrapped figlet header.
    """
    fig.execute(text, font, language, multiline, clipboard)


@app.command("list-fonts")
def fonts(list: fnt.opt_list() = False):
    """
    List all available figlet fonts.
    """
    fnt.execute(list)


@app.command("list-languages")
def list_languages(list: lng.opt_list() = False):
    """
    Lists all available languages.
    """
    lng.execute(list)


def main():
    app()


if __name__ == "__main__":
    main()

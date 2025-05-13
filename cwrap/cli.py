from typing import Annotated

import typer
from core import do_figlet


def opt_font():
    return typer.Option(
        help="The figlet font to use.", autocompletion=opt_font_completion
    )


def opt_font_completion() -> []:
    """
    Get a list of fonts for completion.

    Returns:
        A list of figlet fonts.
    """
    return ["cybermedium", "cyberlarge", "cybersmall"]


def main(
    text: str,
    font: Annotated[str, opt_font()] = "cybermedium",
    language: Annotated[str] = "python",
):

    output = do_figlet(text, font, language)
    typer.echo(output)


if __name__ == "__main__":
    typer.run(main)

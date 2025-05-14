from typing import Annotated

import typer
from core import do_figlet


def opt_font():
    """
    Get the settings for the font option.
    """
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


def opt_language():
    """
    Get the settings for the language option.
    """
    return typer.Option(
        help="The language for the comments.", autocompletion=opt_language_completion
    )


def opt_language_completion():
    """
    Get a list of programming languages for completion.

    Returns:
        A list of programming languages.
    """
    return ["python", "javascript", "typescript", "go", "golang", "lua"]


def main(
    text: str,
    font: Annotated[str, opt_font()] = "cybermedium",
    language: Annotated[str, opt_language()] = "python",
):

    output = do_figlet(text, font, language)
    typer.echo(output)


if __name__ == "__main__":
    typer.run(main)

from typing import Annotated

import typer

from cwrap_py.core import figlet as fig

app = typer.Typer()


def opt_font():
    """
    Get the settings for the font option.
    """
    return Annotated[
        str,
        typer.Option(
            "--font",
            "-f",
            help="The figlet font to use.",
            # autocompletion=opt_font_completion,
        ),
    ]


def opt_language():
    """
    Gets the settings for the language option.
    """
    return Annotated[
        str,
        typer.Option(
            "--language",
            "-l",
            help="The language for the comments.",
            # autocompletion=opt_language_completion,
        ),
    ]


def opt_multiline():
    """
    Gets the settings for the multiline option.
    """
    return Annotated[
        bool,
        typer.Option(
            "--multiline",
            "-m",
            help="Use a multiline comment block. Not supported for some languages.",
        ),
    ]


def opt_clipboard():
    """
    Gets the settings for the copy to clipboard option.
    """
    return Annotated[
        bool,
        typer.Option("--clipboard", "-c", help="Copy the output to the clipboard."),
    ]


def execute(text, font, language, multiline, clipboard):
    # print(f"FIGLET! {text} -f {font} -l {language} -m {multiline} -c {clipboard}")
    output = fig.get_figlet(text, font, language, multiline, clipboard)
    print("\n".join(output))

from typing import Annotated

import typer

from cwrap_py.core import figlet as fig
from cwrap_py.core import fonts as fnt
from cwrap_py.core import languages as lng

app = typer.Typer()


def opt_font_completion():
    return fnt.get_fonts()


opt_font = Annotated[
    str,
    typer.Option(
        "--font",
        "-f",
        help="The figlet font to use.",
        autocompletion=opt_font_completion,
    ),
]


def opt_language_completion():
    languages = sorted(lng.get_languages())
    return languages


opt_language = Annotated[
    str,
    typer.Option(
        "--language",
        "-l",
        help="The language for the comments.",
        autocompletion=opt_language_completion,
    ),
]


opt_multiline = Annotated[
    bool,
    typer.Option(
        "--multiline",
        "-m",
        help="Use a multiline comment block. Not supported for some languages.",
    ),
]


opt_clipboard = Annotated[
    bool,
    typer.Option("--clipboard", "-c", help="Copy the output to the clipboard."),
]


def opt_rule_completion():
    return ["regular", "thick", "thin"]


opt_hr_style = Annotated[
    str,
    typer.Option(
        "-r",
        "--hr-style",
        help="Add a horizontal rule to the top and bottom of the output. [ thin | thick | regular ].",
        autocompletion=opt_rule_completion,
    ),
]


def execute(text, font, language, multiline, clipboard, hr_style):
    # print(f"FIGLET! {text} -f {font} -l {language} -m {multiline} -c {clipboard}")
    output = fig.get_figlet(text, font, language, multiline, clipboard, hr_style)
    print("\n".join(output))

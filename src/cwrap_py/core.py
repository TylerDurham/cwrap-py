# ____ ____ ____ ____  ___  _   _
# |    |  | |__/ |___  |__]  \_/
# |___ |__| |  \ |___ .|      |
#

from pyfiglet import Figlet
from pyperclip import copy

from cwrap_py.languages import LANGUAGES, get_comment_chars


def do_figlet(
    text: str,
    font: str,
    language,
    multiline: bool = False,
    copy_to_clipboard: bool = False,
):

    # Force to lowercase
    language = str.lower(language)
    font = str.lower(font)

    # HTML doesn't have single-line comments!
    if language == "html":
        multiline = True

    comment_chars, has_multiline_comment_chars = get_comment_chars(language, multiline)
    start_comment_chars = ""
    last_comment_chars = ""

    fig = Figlet(font=font)
    lines = fig.renderText(text).splitlines()

    output = []

    if has_multiline_comment_chars == True and multiline == True:
        start_comment_chars = comment_chars[0]
        last_comment_chars = comment_chars[1]
        output.append(start_comment_chars)
        comment_chars = ""

    for line in lines:
        output.append(f"{comment_chars} {line}")

    if has_multiline_comment_chars == True and multiline == True:
        output.append(last_comment_chars)

    print("\n".join(output))

    if copy_to_clipboard == True:
        copy("\n".join(output))


def get_languages():
    return LANGUAGES

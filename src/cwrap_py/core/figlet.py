# =========================================================================
# ____ ____ ____ ____   / ____ _ ____ _    ____ ___
# |    |  | |__/ |___  /  |___ | | __ |    |___  |
# |___ |__| |  \ |___ /   |    | |__] |___ |___  |
#
# =========================================================================

from pyfiglet import Figlet
from pyperclip import copy

from cwrap_py.core.languages import get_comment_chars


def get_figlet(
    text: str,
    font: str,
    language: str,
    multiline: bool = False,
    clipboard: bool = False,
):
    # Force to lowercase
    language = str.lower(language)
    font = str.lower(font)

    # HTML doesn't have single-line comments!
    if language == "html":
        multiline = True

    comment_chars, has_multiline_comment_chars = get_comment_chars(language, multiline)
    opening_comment_chars = ""
    closing_comment_chars = ""  # | Start with  a blank slate.

    fig = Figlet(font=font)
    lines = fig.renderText(text).splitlines()

    output = []

    if has_multiline_comment_chars == True and multiline == True:
        # Caller has requested a multiline comment.
        # Use the opening and closing comment chars to wrap the output.
        opening_comment_chars = comment_chars[0]  # Example: /*
        closing_comment_chars = comment_chars[1]  # Example: */
        output.append(opening_comment_chars)  # Go ahead and write to ouput buffer
        comment_chars = ""  # We no longer will use this.

    for line in lines:
        output.append(f"{comment_chars} {line}")

    if has_multiline_comment_chars == True and multiline == True:
        # Close off the output with the closing comment char
        output.append(closing_comment_chars)

    # TODO: I feel like this should be moved to the CLI package.
    if clipboard == True:
        copy("\n".join(output))

    return output

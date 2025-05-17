# =========================================================================
# ____ ____ ____ ____   / ____ _ ____ _    ____ ___
# |    |  | |__/ |___  /  |___ | | __ |    |___  |
# |___ |__| |  \ |___ /   |    | |__] |___ |___  |
#
# =========================================================================

from pyfiglet import Figlet
from pyperclip import copy

from cwrap_py.core.languages import get_comment_chars

HR_STYLES = {}
HR_STYLES["regular"] = "="
HR_STYLES["thick"] = "#"
HR_STYLES["thin"] = "-"


def print_rule(buffer, comment_chars: str, style: str, width: int):
    r = HR_STYLES.get(style)
    if r == None:
        style = "regular"

    buffer.append(f"{comment_chars} {HR_STYLES[style] * width}")


def get_figlet(
    text: str,
    font: str,
    language: str,
    multiline: bool = False,
    clipboard: bool = False,
    hr_style: str = None,
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

    hr_width = len(lines[0])  # How wide will the output be?

    output = []  # "Buffer" to hold each line of output.

    if has_multiline_comment_chars == True and multiline == True:
        # Caller has requested a multiline comment.
        # Use the opening and closing comment chars to wrap the output.
        opening_comment_chars = comment_chars[0]  # Example: /*
        closing_comment_chars = comment_chars[1]  # Example: */
        output.append(opening_comment_chars)  # Go ahead and write to ouput buffer
        comment_chars = ""  # We no longer will use this.

    if not hr_style == None:
        print_rule(output, comment_chars, hr_style, hr_width)

    for line in lines:
        output.append(f"{comment_chars} {line}")

    if not hr_style == None:
        print_rule(output, comment_chars, hr_style, hr_width)

    if has_multiline_comment_chars == True and multiline == True:
        # Close off the output with the closing comment char
        output.append(closing_comment_chars)

    # TODO: I feel like this should be moved to the CLI package.
    if clipboard == True:
        copy("\n".join(output))

    return output

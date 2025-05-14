from languages import get_comment_chars
from pyfiglet import Figlet


def do_figlet(text: str, font: str, language, multiline: bool = False):

    comment_chars, has_multiline_comment_chars = get_comment_chars(language, multiline)
    start_comment_chars = ""
    last_comment_chars = ""

    fig = Figlet(font=font)
    lines = fig.renderText(text).splitlines()

    if has_multiline_comment_chars == True and multiline == True:
        start_comment_chars = comment_chars[0]
        last_comment_chars = comment_chars[1]
        print(start_comment_chars)
        comment_chars = ""

    for line in lines:
        print(f"{comment_chars} {line}")

    if has_multiline_comment_chars == True and multiline == True:
        print(last_comment_chars)

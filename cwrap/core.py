from pyfiglet import Figlet

languages = {"javascript": "//", "js": "//", "lua": "--", "python": "#"}


def get_comment_char(lang):
    return languages.get(lang)


def do_figlet(text: str, font: str, language):
    comment_char = get_comment_char(language)
    if comment_char == None:
        raise KeyError(f"Language {language} not supported")

    fig = Figlet(font=font)
    lines = fig.renderText(text).splitlines()
    for line in lines:
        print(f"{comment_char} {line}")

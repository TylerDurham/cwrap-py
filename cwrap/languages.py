from collections import namedtuple

MULTILINE_COMMENT_CHARS_C = ["/*", "*/"]
MULTILINE_COMMENT_CHARS_LUA = ["--[[", "]]"]
COMMENT_CHARS_C = "//"
COMMENT_CHARS_POUND = "#"
COMMENT_CHARS_DASH = "--"

LANGUAGES = {}

LanguageInfo = namedtuple(
    "LanguageInfo",
    ["has_multiline_comment_chars", "comment_chars", "multiline_comment_chars"],
)

# "C" STYLE LANGUAGES
li_c = LanguageInfo(
    has_multiline_comment_chars=True,
    comment_chars="//",
    multiline_comment_chars=MULTILINE_COMMENT_CHARS_C,
)

LANGUAGES["javascript"] = li_c
LANGUAGES["js"] = li_c
LANGUAGES["typescript"] = li_c
LANGUAGES["ts"] = li_c
LANGUAGES["java"] = li_c
LANGUAGES["c"] = li_c
LANGUAGES["c++"] = li_c

# PYTHON
LANGUAGES["python"] = LanguageInfo(
    has_multiline_comment_chars=False,
    comment_chars=COMMENT_CHARS_POUND,
    multiline_comment_chars=None,
)

# SHELL LANGUAGES
li_shell = LanguageInfo(
    has_multiline_comment_chars=False,
    comment_chars=COMMENT_CHARS_POUND,
    multiline_comment_chars=None,
)

LANGUAGES["bash"] = li_shell
LANGUAGES["zsh"] = li_shell

# LUA
LANGUAGES["lua"] = LanguageInfo(
    has_multiline_comment_chars=True,
    comment_chars=COMMENT_CHARS_DASH,
    multiline_comment_chars=MULTILINE_COMMENT_CHARS_LUA,
)
# SQL
LANGUAGES["sql"] = LanguageInfo(
    has_multiline_comment_chars=True,
    comment_chars=COMMENT_CHARS_POUND,
    multiline_comment_chars=MULTILINE_COMMENT_CHARS_C,
)


def get_comment_chars(language: str, multiline: bool = False):
    if multiline == True:
        print("Multiline is set.")

    lang_info = LANGUAGES.get(language)

    if lang_info == None:
        raise KeyError(f"Language {language} not supported")

    if multiline == True and lang_info.has_multiline_comment_chars == True:
        return lang_info.multiline_comment_chars, True
    else:
        return lang_info.comment_chars, False

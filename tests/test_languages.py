import unittest

from cwrap_py.core import languages as core_languages

C_LANGUAGES = ["js", "javascript", "typescript", "c", "c++"]
SH_LANGUAGES = ["sh", "bash", "zsh"]


class TestCoreLanguages(unittest.TestCase):

    def test_get_languages(self):
        langs = core_languages.get_languages()
        self.assertIsNotNone(langs, "Returned dictionary should NOT be None.")

        for key in C_LANGUAGES:

            self.assert_lang(langs[key], key, "//", True, ["/*", "*/"])

        for key in SH_LANGUAGES:

            self.assert_lang(langs[key], key, "#", False, None)

    def assert_lang(
        self,
        obj: object,
        key: str,
        comment_chars: str,
        has_multiline_comment_chars: bool,
        multiline_comment_chars: list,
    ):

        # Did we get anything back?
        self.assertIsNotNone(obj, f"'{key}' info should NOT be None.")

        self.assertEqual(
            obj.comment_chars,
            comment_chars,
            f"'{key}' comment characters - expected: {comment_chars} actual {obj.comment_chars}.",
        )

        # Interrogate each field
        self.assertEqual(
            obj.has_multiline_comment_chars,
            has_multiline_comment_chars,
            f"'{key}' multiline comments - expected: {has_multiline_comment_chars} actual: {obj.has_multiline_comment_chars}.",
        )

        if has_multiline_comment_chars:
            self.assertEqual(obj.multiline_comment_chars[0], multiline_comment_chars[0])
            self.assertEqual(obj.multiline_comment_chars[1], multiline_comment_chars[1])


if __name__ == "__main__":
    unittest.main()

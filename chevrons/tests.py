import unittest
from .text import Chevrons


class TestChevronize(unittest.TestCase):

    def test_chevronize_regular_string(self):
        """
        Testing on regular string with single
        substring with double quotes around

        """
        original_string = 'This is "quoted"'
        self.assertEquals(
            'This is «quoted»', Chevrons(original_string).apply()
        )

    def test_chevronize_two_quotes(self):
        """
        Testing on regular string with two
        substrings with double quotes around

        """
        original_string = 'These are "first" and "second" quotes'
        self.assertEquals(
            'These are «first» and «second» quotes', Chevrons(original_string).apply()
        )

    def test_chevronize_regular_string_with_single_quotes(self):
        """
        Testing on regular string with single
        substring with single quotes around

        """
        original_string = "This is 'quoted'"
        self.assertEquals(
            "This is «quoted»", Chevrons(original_string).apply()
        )

    def test_chevronize_two_quotes_with_single_quotes(self):
        """
        Testing on regular string with two
        substrings with single quotes around

        """
        original_string = "These are 'first' and 'second' quotes"
        self.assertEquals(
            "These are «first» and «second» quotes", Chevrons(original_string).apply()
        )

    def test_unquote_regular_string_with_single_quote_unpaired(self):
        """
        Testing on regular string with single
        substring with single quotes around

        """
        original_string = "This is 'quoted"
        self.assertEquals(
            "This is quoted", Chevrons(original_string).apply()
        )

    def test_unquote_regular_string_with_double_quote_unpaired(self):
        """
        Testing on regular string with single
        substring with single quotes around

        """
        original_string = 'This is "quoted'
        self.assertEquals(
            "This is quoted", Chevrons(original_string).apply()
        )


if __name__ == '__main__':
    unittest.main()

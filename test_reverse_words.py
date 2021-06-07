import unittest
from reverse_words import reverse_words


class CaseReverseWords(unittest.TestCase):

    def test_given(self):
        self.assertEqual("Tadimeti V is name My", reverse_words("My name is V Tadimeti"))

    def test_extra(self):
        self.assertEqual("James is name my Hello", reverse_words("Hello my name is James"))


if __name__ == "__main__":
    unittest.main()

import unittest
from handlers.filter_handler import FilterHandler


class TestFilterWord(unittest.TestCase):
    def setUp(self):
        self.filter_word = FilterHandler('hello')

    def test_filter_word_found(self):
        message = "hello world"
        result = self.filter_word.run_action(message)
        self.assertEqual(result, "<FOUND: hello world>")

    def test_filter_word_not_found(self):
        message = "goodbye world"
        result = self.filter_word.run_action(message)
        self.assertEqual(result, "<NOT FOUND goodbye world>")

if __name__ == '__main__':
    unittest.main()

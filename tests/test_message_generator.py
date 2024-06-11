# import unittest
# from behaviours.simple_message_generator import MessageGenerator

# class TestMessageGenerator(unittest.TestCase):
#     def setUp(self):
#         self.alphabet = ['hello', 'sun', 'world', 'space', 'moon', 'crypto', 'sky', 'ocean', 'universe']
#         self.message_generator = MessageGenerator(self.alphabet)

#     def test_print_phrase(self):
#         phrase = self.message_generator.print_phrase()
#         self.assertIsInstance(phrase, str)
#         self.assertIn(' ', phrase)
#         words = phrase.split()
#         self.assertIn(words[0], self.alphabet)
#         self.assertIn(words[1], self.alphabet)

# if __name__ == '__main__':
#     unittest.main()

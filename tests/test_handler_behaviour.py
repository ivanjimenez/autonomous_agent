import unittest
from unittest.mock import MagicMock
from handlers.filter_handler import FilterHandler
from behaviours.simple_message_generator import SimpleMessageGenerator
from helpers.logging_config import setup_logging
import logging

setup_logging()

class TestHandlersAndBehaviours(unittest.TestCase):
    
    print("######### Starting Unit Tests for handler and behaviour")

    def test_filter_handler(self):
        # Handle instance
        handler = FilterHandler("hello")

        # Check if handle is created
        self.assertIsInstance(handler, FilterHandler)
        self.assertEqual(handler.content, "hello")

        # Check if handle works
        self.assertEqual(handler.run_handle("hello world"), "<FOUND: hello world>")
        self.assertEqual(handler.run_handle("sun sky"), "<NOT FOUND: sun sky>")
        print("Handle Filter Handler OK")

    def test_simple_message_generator(self):
        # Behaviour instance
        behaviour = SimpleMessageGenerator(["hello", "sun", "world", "sky"])

        # Check if behaviour is created correctly
        self.assertIsInstance(behaviour, SimpleMessageGenerator)
        self.assertEqual(behaviour.alphabet, ["hello", "sun", "world", "sky"])

        # Check behaviour works
        msg = behaviour.process_message()
        self.assertEqual(len(msg.split()), 2)

        alphabet = ["hello", "sun", "world", "sky"]
        word1, word2 = msg.split()
        self.assertIn(word1, alphabet)
        self.assertIn(word2, alphabet)
        print("Behaviour OK")


if __name__ == '__main__':
    unittest.main()

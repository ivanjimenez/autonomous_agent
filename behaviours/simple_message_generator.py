from typing import List
import random
from behaviours.abstract_message_generator import AbstractMessageGenerator
from datetime import datetime
class SimpleMessageGenerator(AbstractMessageGenerator):
    """
    A simple message generator that randomly selects two words from a provided list.

    :param alphabet: List of words to select from.
    :type alphabet: List[str]
    """

    def __init__(self, alphabet: List[str]):
        """
        Initialize the message generator with a list of words.

        :param alphabet: List of words to select from.
        :type alphabet: List[str]
        """
        super().__init__()
        self.alphabet = alphabet
        self.message_generated: str = None


    def process_message(self) -> str:
        """
        Generate and return a phrase consisting of two randomly selected words.

        :return: A phrase formed by two randomly selected words.
        :rtype: str
        """
        msg_result = f'{random.choice(self.alphabet)} {random.choice(self.alphabet)}'
        self.message_generated = None  # If intended to reset, add explanation in doc
        return msg_result

        
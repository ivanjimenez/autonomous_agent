# dataclasses
import asyncio
from typing import List
import random


class MessageGenerator:
    """
        Random Two Words
    """
    def __init__(self, alphabet):
        self.alphabet = alphabet 
        self.message_generated = None

    def print_phrase(self):
        "print  phrase"
        msg_result = str(random.choice(self.alphabet)) + " " + str(random.choice(self.alphabet))
        self.message_generated = None
        return msg_result
        
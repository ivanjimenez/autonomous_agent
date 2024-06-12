"""This module contains the implementation of behaviour interface."""
from datetime import datetime
from typing import Any, List
import random
from behaviours.abstract_behaviour import AbstractBehaviour

class SimpleMessageGenerator(AbstractBehaviour):
    """
    A simple message generator that randomly selects two words from a provided list.

    :param alphabet: List of words to select from.
    :type alphabet: List[str]
    """
    def __init__(self,  input_data: List[str])->None:
        super().__init__(input_data=input_data)
        self._datetime = datetime.now()

    def use_behaviour(self) -> str:
        """
        Generate and return a phrase consisting of two randomly selected words.

        :return: A phrase formed by two randomly selected words.
        :rtype: str
        """
        msg_result = f'{random.choice(self.input_data)} {random.choice(self.input_data)}'
        return msg_result

    def select_behaviour(self, input_data: List[str]) -> Any:
        self.input_data = input_data
"""Module with the interface definition of the abstract behaviour."""
from abc import ABC, abstractmethod
from typing import Any

class AbstractBehaviour(ABC):
    """
    This class provides an interface for Behaviours
    """

    def __init__(self, input_data: Any):
        self.input_data = input_data

    @abstractmethod
    def use_behaviour(self) -> Any:
        """
        Abstract method to generate a message from the provided input.

        :param input_data: The data used to generate the message.
        :type input_data: Any
        :return: The generated message.
        :rtype: str
        """
    @abstractmethod
    def select_behaviour(self, input_data: Any)-> Any:
        """
        Method to update behaviour if it is necessary. 
        Also a new handler instance could be created.
        """
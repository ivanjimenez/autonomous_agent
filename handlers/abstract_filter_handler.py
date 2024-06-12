from abc import ABC, abstractmethod
from typing import Any

class AbstractFilterHandler(ABC):
    """
        AbstractFilterHandler
    """
   
    @abstractmethod
    def run_handle(self, message: Any) -> Any:
        """
        Print a message indicating whether the word is in the given message.

        :param message: The message to search within.
        :type message: str
        :return: A formatted string indicating if the word was found or not.
        :rtype: str
        """
        pass
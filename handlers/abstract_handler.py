"""Module with the interface definition of the abstract handler."""
from abc import ABC, abstractmethod
from typing import Any

class AbstractHandler(ABC):
    """
    This class provides an interface for a Handler
    """
    @abstractmethod
    def run_handle(self, message: Any) -> Any:
        """
        Handle a message
        :param message: The message to be processed. This could be of any type, 
                    depending on the implementation.
        :return: The result of the processing. The return type is flexible and 
             can vary based on the specific implementation of the method.
        """

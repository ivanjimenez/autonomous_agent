from abc import ABC, abstractmethod

class AbstractFilterHandler(ABC):
    """
        AbstractFilterHandler
    """
   
    @abstractmethod
    def find_word(self, message: str) -> str:
        """
        Print a message indicating whether the word is in the given message.

        :param message: The message to search within.
        :type message: str
        :return: A formatted string indicating if the word was found or not.
        :rtype: str
        """
        pass
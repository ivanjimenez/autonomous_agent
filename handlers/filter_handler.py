import dataclasses

from handlers.abstract_filter_handler import AbstractFilterHandler

@dataclasses.dataclass
class FilterHandler(AbstractFilterHandler):
    """
    Docstring
    """
    def __init__(self, message, _type):
        self._type = _type
        self.content = message
           
    def run_handle(self, message: str) -> str:
        """
        Print a message indicating whether the word is in the given message.

        :param message: The message to search within.
        :type message: str
        :return: A formatted string indicating if the word was found or not.
        :rtype: str
        """
        if self.content in message:
            return f'<FOUND: {message}>'
        return f'<NOT FOUND: {message}>'
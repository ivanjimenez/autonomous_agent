import dataclasses

from handlers.abstract_filter_handler import AbstractFilterHandler

@dataclasses.dataclass
class FilterHandler(AbstractFilterHandler):
    word_to_filter: str

    def find_word(self, message: str) -> str:
        """
        Print a message indicating whether the word is in the given message.

        :param message: The message to search within.
        :type message: str
        :return: A formatted string indicating if the word was found or not.
        :rtype: str
        """
        if self.word_to_filter in message.lower():
            return f'<FOUND: {message}>'
        return f'<NOT FOUND: {message}>'
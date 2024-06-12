"""This module contains the implementation of handle interface."""
import dataclasses

from handlers.abstract_handler import AbstractHandler

@dataclasses.dataclass
class FilterHandler(AbstractHandler):
    """
    A handler that filters messages based on a specified content.
    """
    def __init__(self, message):
        """Content setting"""
        self.content = message

    def run_handle(self, message: str) -> str:
        """
        This handler filters messages for the keyword (e.g.: 'hello') and prints the whole
        message to stdout. 

        For test purposes the message is formatted as <FOUND message> if exists the keyboard and
        <NOT FOUND message> if not.

        Every message has a 5 characters unique id to see clearly every message as has sent as has 
        received. No messages lost.

        :param message: The message to search within.
        :type message: str
        :return: A formatted string indicating if the word was found or not.
        :rtype: str
        """
        if self.content in message:
            return f'<FOUND: {message}>'
        return f'<NOT FOUND: {message}>'
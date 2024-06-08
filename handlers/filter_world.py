# For dataclasses
import dataclasses

@dataclasses.dataclass
class FilterWord:
    "handler"
    def __init__(self, word):
        self.word = word

    def filter_word(self, message) -> str:
        """ 
            Print str if message is filtered by word
        """
        if self.word in message.lower():
            return f'<FOUND: {message}>'
        return f'<NOT FOUND> {message}'

# message_generator.py

from abc import ABC, abstractmethod
from datetime import datetime

class AbstractMessageGenerator(ABC):
    """
    Abstract base class for generating messages based on input parameters.

    :cvar ABC: Marks the class as an abstract base class.
    """
    def __init__(self):
        """
        Init attributes
        """
        self._state = None
        self._datetime = datetime.now()

    @property
    def current_time(self):
        """
        Get time
        """
        return self._datetime
    
    @current_time.setter
    def current_time(self, new_time)->None:
        """
        Set time
        """
        self.current_time = new_time

    @property
    def state(self)->str:
        """
        Get the current state of behaviour
        """
        return self._state
    
    @state.setter
    def state(self, new_state) -> None:
        self._state = new_state

    @property
    def datetime(self)->None:
        """
        Datatime
        """
    @abstractmethod
    def process_message(self) -> str:
        """
        Abstract method to generate a message from the provided input.

        :param input_data: The data used to generate the message.
        :type input_data: Any
        :return: The generated message.
        :rtype: str
        """


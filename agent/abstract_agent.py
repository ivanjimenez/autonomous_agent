"""Module with the interface definition of the abstract behaviour."""
from datetime import datetime
from abc import ABC, abstractmethod

from agent.agent_states import AgentStates
class AbstractAgent(ABC):
    """
    Abstract class defining the basic capabilities of an agent.
    """
    def __init__(self):
        """
        Init attributes
        """
        self.state = AgentStates.INIT
        self.datetime = datetime.now()

    @property
    def current_time(self):
        """
        Get time if it is necessario to change some states
        """
        return self.datetime
    
    @current_time.setter
    def current_time(self, new_time)->None:
        """
        Set time
        """
        self.current_time = new_time
    @abstractmethod
    async def process_messages(self):
        """
        Process messages received by the agent.
        """
    @abstractmethod
    async def generate_messages(self):
        """
        Generate and send messages from the agent.
        """
    @abstractmethod
    async def run(self):
        """
        Run the main loop for the agent's operation.
        """

'''
Abstract Agent
''' 

from abc import ABC, abstractmethod

class AbstractAgent(ABC):
    """
    Abstract class defining the basic capabilities of an agent.
    """
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

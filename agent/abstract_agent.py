from abc import ABC, abstractmethod
import asyncio

class AbstractAgent(ABC):
    """
    Abstract class defining the basic capabilities of an agent.
    """

    @abstractmethod
    async def process_messages(self):
        """
        Process messages received by the agent.
        """
        pass

    @abstractmethod
    async def generate_messages(self):
        """
        Generate and send messages from the agent.
        """
        pass

    @abstractmethod
    async def run(self):
        """
        Run the main loop for the agent's operation.
        """
        pass

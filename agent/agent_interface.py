from abc import ABC, abstractmethod

class AgentBase(ABC):
    @abstractmethod
    def InBox(self):
        pass

    @abstractmethod
    def OutBox(self):
        pass

    
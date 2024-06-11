from enum import Enum


class AgentStates(Enum):
    """Internal agent loop states."""

    INIT = None
    STARTED = "running"
    STOPPED = "stopped"
    ERROR = "error"
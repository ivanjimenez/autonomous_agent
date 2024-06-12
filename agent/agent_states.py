""" 
TODO: Implement this functionality in future versions 

This module contains the states of an agent to update 
handles or/and behaviours if state changes
"""

from enum import Enum

class AgentStates(Enum):
    """Internal agent loop states."""

    INIT = None
    STARTED = "running"
    STOPPED = "stopped"
    ERROR = "error"
"""This module contains the implementation of agent interface."""
import logging
import asyncio
import secrets
from agent.abstract_agent import AbstractAgent
from helpers.color_text_line import color_line

from behaviours.simple_message_generator import AbstractMessageGenerator
from handlers.filter_handler import AbstractHandler
from helpers.logging_config import setup_logging

# Logging setup
setup_logging()
class SimpleAgent(AbstractAgent):
    """
    This class provides an interface for an Agent
    """
    def __init__(self, name) -> None:
        # Init arguments
        super().__init__()
        self.name = name
        self.outboxqueue = asyncio.Queue()
        self.inboxqueue = asyncio.Queue()
        self.other_agent = None
        self.handle = None
        self.behaviour = None
        self.iterations = 0

    def set_other_agent(self, 
        other_agent: AbstractAgent
    )-> None:
        """
        :param: other_agent
        """
        self.other_agent = other_agent

    def register_handle(self, 
        handle: AbstractHandler
    )->None:
        """
         Registering handle
        """
        self.handle = handle

    def register_behaviour(self, 
        behaviour: AbstractMessageGenerator
    )-> None:
        """
        Registering behaviour
        """
        self.behaviour = behaviour

    async def process_messages(self):
        """Process incoming messages."""
        while True: 
            try:
                message = await self.inboxqueue.get()
                filtered_message = self.handle.run_handle(message)
                logging.info("%s receiving: %s", self.name, filtered_message)
                self.iterations += 1
            except asyncio.QueueEmpty:
                await asyncio.sleep(0.1) 

    async def generate_messages(self):
        """Generate and send messages to the other agent."""
        while True: 
            message = f"{self.behaviour.process_message()} id {secrets.token_hex(5)}"
            message = color_line(message)
            logging.info("%s sending: %s", self.name, message)
            self.iterations += 100
            try:
                await self.other_agent.inboxqueue.put(message)
                await asyncio.sleep(2)
            except asyncio.QueueFull:
                logging.exception('%s could not send: queue is full')
                

    async def run(self):
        """Main loop to generate and process messages."""
        task1 = asyncio.create_task(self.generate_messages())
        task2 = asyncio.create_task(self.process_messages())
        await asyncio.gather(task1, task2)

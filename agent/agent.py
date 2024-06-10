# General modules
import asyncio
import random
import secrets
from datetime import datetime
from agent.abstract_agent import AbstractAgent
from helpers.color_text_line import color_line
import logging

# For modules
from behaviours.simple_message_generator import AbstractMessageGenerator
from handlers.filter_handler import AbstractFilterHandler
class Agent(AbstractAgent):

    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    def __init__(self, name) -> None:
        # Init arguments
        self.name = name
        self.outboxqueue = asyncio.Queue()
        self.inboxqueue = asyncio.Queue()
        self.other_agent = None
        self.handle = None
        self.behaviour = None
        self.iterations = 0

    def set_other_agent(self, other_agent):
        # Set Agent
        self.other_agent = other_agent

    def register_handle(self, handle: AbstractFilterHandler):
        # Registering handle
        self.handle = handle

    def register_behaviour(self, behaviour: AbstractMessageGenerator):
        # Registering behaviour
        self.behaviour = behaviour

    async def process_messages(self):
        """Process incoming messages."""
        while True: # self.iterations < 700:
            try:
                message = await self.inboxqueue.get()
                filtered_message = self.handle.run_action(message)
                # current_time = datetime.now().strftime('%H:%M:%S.%f')[:-4]
                # print(f"{current_time} {self.name} received: {filtered_message}")
                logging.info("%s sending: %s", self.name, filtered_message)
                self.iterations += 1
            except asyncio.QueueEmpty:
                await asyncio.sleep(0.1) 

    async def generate_messages(self):
        """Generate and send messages to the other agent."""
        while True: #self.iterations < 700:
            message = f"{self.behaviour.process_message()} id {secrets.token_hex(5)}"
            message = color_line(message)
            # current_time = datetime.now().strftime('%H:%M:%S.%f')[:-4]
            # print(f"{current_time} {self.name} sending: {message}")
            logging.info("%s sending: %s", self.name, message)
            self.iterations += 100
            try:
                await self.other_agent.inboxqueue.put(message)
                await asyncio.sleep(2)
            except asyncio.QueueFull:
                logging.exception('%s could not send: queue is full', self.name)
                

    async def run(self):
        """Main loop to generate and process messages."""
        task1 = asyncio.create_task(self.generate_messages())
        task2 = asyncio.create_task(self.process_messages())
        await asyncio.gather(task1, task2)

# General modules
import asyncio
import random
import secrets
from datetime import datetime
from agent.abstract_agent import AbstractAgent
from helpers.color_text_line import color_line

# For modules
from behaviours.simple_message_generator import SimpleMessageGenerator
from handlers.filter_handler import FilterHandler
class Agent(AbstractAgent):
    def __init__(self, name):
        # Init arguments
        self.name = name
        self.outboxqueue = asyncio.Queue()
        self.inboxqueue = asyncio.Queue()
        self.other_agent = None
        self.handle = None
        self.behaviour = None

    def set_other_agent(self, other_agent):
        # Set Agent
        self.other_agent = other_agent

    def register_handle(self, handle: FilterHandler):
        # Registiring handle
        self.handle = handle

    def register_behaviour(self, behaviour: SimpleMessageGenerator):
        # Registiring behaviour
        self.behaviour = behaviour

    async def process_messages(self):
        """Process incoming messages."""
        message = await self.inboxqueue.get()
        filtered_message = self.handle.find_word(message)
        current_time = datetime.now().strftime('%H:%M:%S.%f')[:-4]
        print(f"{current_time} {self.name} received: {filtered_message}")

    async def generate_messages(self):
        """Generate and send messages to the other agent."""
        message = f"{self.behaviour.process_message()} id {secrets.token_hex(5)}"
        message = color_line(message)
        current_time = datetime.now().strftime('%H:%M:%S.%f')[:-4]
        print(f"{current_time} {self.name} sending: {message}")
        await self.other_agent.inboxqueue.put(message)
        await asyncio.sleep(2)

    async def run(self):
        """Main loop to generate and process messages."""
        while True:
            await self.generate_messages()
            await self.process_messages()

# for asynchronous purposes
import asyncio
import random
import time
from datetime import datetime
from asyncio import Queue
from typing import List
from behaviours.message_generator import MessageGenerator
from handlers.filter_world import FilterWord
from datetime import datetime
import secrets

class Agent:
    
   
    def __init__(self, name):
        self.name = name
        self.outboxqueue = asyncio.Queue()
        self.inboxqueue = asyncio.Queue()
        self.other_agent = None
        self.handle = None
        self.behaviour = None
        self.reset = "\033[0m"

    def random_color(self):
        # Generar valores RGB aleatorios
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return f"\033[38;2;{r};{g};{b}m"
    
    def color_line(self, text):
        color = self.random_color()
        return f"{color}{text}{self.reset}"

    def set_other_agent(self, other_agent):
        self.other_agent = other_agent

    def register_handle(self, handle: FilterWord):
        self.handle = handle

    def register_behaviour(self, behaviour : MessageGenerator):
        self.behaviour = behaviour

    async def process_messages(self):
        """
            process
        """
        message = await self.inboxqueue.get()
        filtered_message = self.handle.filter_word(message)
        print(f'{datetime.now().strftime('%H:%M:%S.%f')[:-4]} {self.name} received: {filtered_message}')          
    
    async def generate_messages(self):
        message = f'{self.behaviour.print_phrase()} id {secrets.token_hex(5)}'
        message = self.color_line(message)
        print(f'{datetime.now().strftime('%H:%M:%S.%f')[:-4]} {self.name} sending: {message}')
        await self.other_agent.inboxqueue.put(message)
        await asyncio.sleep(2)  

    async def run(self):
        while True:
            await self.generate_messages()
            await self.process_messages()
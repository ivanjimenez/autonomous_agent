import unittest
import asyncio
from agent.agent import Agent
from handlers.filter_handler import FilterHandler
from behaviours.simple_message_generator import MessageGenerator

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.alphabet = [
            'hello', 'sun', 'world', 'space', 'moon', 
            'crypto', 'sky', 'ocean', 'universe'
        ]
        self.word = 'hello'
        self.agent1 = Agent('Agent 1')
        self.agent2 = Agent('Agent 2')
        self.filter_word = FilterHandler(self.word)
        self.message_generator = MessageGenerator(self.alphabet)

        self.agent1.register_handle(self.filter_word)
        self.agent1.register_behaviour(self.message_generator)
        self.agent2.register_handle(self.filter_word)
        self.agent2.register_behaviour(self.message_generator)
        self.agent1.set_other_agent(self.agent2)
        self.agent2.set_other_agent(self.agent1)

    async def test_agent_interaction(self):
        # Create and start tasks
        task1 = asyncio.create_task(self.agent1.run())
        task2 = asyncio.create_task(self.agent2.run())

        try:
            await asyncio.sleep(5)  # Run the agents for 4 seconds
        finally:
            task1.cancel()
            task2.cancel()

            # Await cancellation of tasks
            try:
                await task1
            except asyncio.CancelledError:
                print("Agent 1 task was cancelled")

            try:
                await task2
            except asyncio.CancelledError:
                print("Agent 2 task was cancelled")

    def test_async(self):
        asyncio.run(self.test_agent_interaction())

if __name__ == '__main__':
    unittest.main()

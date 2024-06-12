import unittest
import logging
from unittest.mock import MagicMock
import asyncio
from agent.simple_agent import SimpleAgent
from behaviours.simple_message_generator import SimpleMessageGenerator
from handlers.filter_handler import FilterHandler

class TestAgent(unittest.TestCase):

    def setUp(self):
        self.agent = SimpleAgent('TestAgent')
        self.other_agent = MagicMock()
        self.message_generator = MagicMock(spec=SimpleMessageGenerator)
        self.filter_handler = MagicMock(spec=FilterHandler)

    def test_set_other_agent(self):
        self.agent.set_other_agent(self.other_agent)
        self.assertEqual(self.agent.other_agent, self.other_agent)
        print("Se ha configurado correctamente el otro agente.")

    def test_register_handle(self):
        self.agent.register_handle(self.filter_handler)
        self.assertEqual(self.agent.handle, self.filter_handler)
        logging.info("Se ha registrado correctamente el manejador.")

    def test_register_behaviour(self):
        self.agent.register_behaviour(self.message_generator)
        self.assertEqual(self.agent.behaviour, self.message_generator)
        print("Se ha registrado correctamente el comportamiento.")

    # Add more unit tests as needed

if __name__ == '__main__':
    unittest.main(verbosity=2)

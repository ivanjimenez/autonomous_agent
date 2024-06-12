# import unittest
# import logging
# from unittest.mock import MagicMock
# import asyncio
# from agent.simple_agent import SimpleAgent
# from behaviours.simple_message_generator import SimpleMessageGenerator
# from handlers.filter_handler import FilterHandler

# class TestAgent(unittest.TestCase):

#     def setUp(self):
#         self.agent = SimpleAgent('TestAgent1')
#         self.other_agent = SimpleAgent('TestAgent2')
#         self.message_generator = MagicMock(spec=SimpleMessageGenerator)
#         self.filter_handler = MagicMock(spec=FilterHandler)

#     def test_connect_both_agents(self):
#         self.agent.set_other_agent(self.other_agent)
#         self.assertEqual(self.agent.other_agent, self.other_agent)
#         logging.info("Configured Agent1 and Agent2.")

#     def test_register_handle_agent1(self):
#         self.agent.register_handle(self.filter_handler)
#         self.assertEqual(self.agent.handle, self.filter_handler)
#         logging.info("Agent1 handle configured")

#     def test_register_behaviour_agent1(self):
#         self.agent.register_behaviour(self.message_generator)
#         self.assertEqual(self.agent.behaviour, self.message_generator)
#         logging.info("Agent1 behaviour configured")

#     def test_register_handle_agent2(self):
#         self.other_agent.register_handle(self.filter_handler)
#         self.assertEqual(self.other_agent.handle, self.filter_handler)
#         logging.info("Agent1 handle configured")

#     def test_register_behaviour_agent2(self):
#         self.other_agent.register_behaviour(self.message_generator)
#         self.assertEqual(self.other_agent.behaviour, self.message_generator)
#         logging.info("Agent2 behaviour configured")
    

# if __name__ == '__main__':
#     unittest.main(verbosity=2)

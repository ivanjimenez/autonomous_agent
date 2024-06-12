# # Este test no funciona

# import unittest
# from agent.agent import Agent
# from handlers.filter_handler import FilterHandler
# from behaviours.simple_message_generator import SimpleMessageGenerator

# class TestAgent(unittest.TestCase):
#     def setUp(self):
#         self.alphabet = ['hello', 'sun', 'world', 'space', 'moon', 'crypto', 'sky', 'ocean', 'universe']
#         self.word = 'hello'
#         self.agent1 = Agent('Agent 1')
#         self.agent2 = Agent('Agent 2')
#         self.filter_word = FilterHandler(self.word, _type='Word')
#         self.message_generator = SimpleMessageGenerator(self.alphabet)
        
#         self.agent1.register_handle(self.filter_word)
#         self.agent1.register_behaviour(self.message_generator)
#         self.agent2.register_handle(self.filter_word)
#         self.agent2.register_behaviour(self.message_generator)
#         self.agent1.set_other_agent(self.agent2)
#         self.agent2.set_other_agent(self.agent1)

#     def test_register_handle(self):
#         self.assertEqual(self.agent1.handle, self.filter_word)

#     def test_register_behaviour(self):
#         self.assertEqual(self.agent1.behaviour, self.message_generator)

#     def test_set_other_agent(self):
#         self.assertEqual(self.agent1.other_agent, self.agent2)
    
#     async def test_generate_and_process_messages(self):
#         await self.agent1.generate_messages()
#         self.assertFalse(self.agent1.inboxqueue.empty())
#         self.assertFalse(self.agent2.inboxqueue.empty())

# if __name__ == '__main__':
#     unittest.main()

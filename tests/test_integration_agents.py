# import asyncio
# import logging
# import re
# import pytest
# from agent.simple_agent import SimpleAgent
# from handlers.filter_handler import FilterHandler
# from behaviours.simple_message_generator import SimpleMessageGenerator

# @pytest.mark.asyncio
# async def test_agent_communication(capfd):
#     # Creating two instances of SimpleAgent
#     agent1 = SimpleAgent("Agent 1")
#     agent2 = SimpleAgent("Agent 2")

#     # Setting each agent as the other's counterpart
#     agent1.set_other_agent(agent2)
#     agent2.set_other_agent(agent1)

#     # Creating handler for agent 1
#     handler1 = FilterHandler("hello")
#     agent1.register_handle(handler1)

#     # Creating behavior for agent 1
#     behavior1 = SimpleMessageGenerator(["hello", "sun", "world", "space", "moon", "crypto", "sky", "ocean", "universe", "human"])
#     agent1.register_behaviour(behavior1)

#     # Creating handler for agent 2
#     handler2 = FilterHandler("hello")
#     agent2.register_handle(handler2)

#     # Creating behavior for agent 2
#     behavior2 = SimpleMessageGenerator(["hello", "sun", "world", "space", "moon", "crypto", "sky", "ocean", "universe", "human"])
#     agent2.register_behaviour(behavior2)

#     # Running agents
#     task1 = asyncio.create_task(agent1.run())
#     task2 = asyncio.create_task(agent2.run())

#     # Counter for FOUND messages
#     found_messages_agent1 = 0
#     found_messages_agent2 = 0

#     async def read_stdout():
#         nonlocal found_messages_agent1, found_messages_agent2
#         # Read stdout while capturing
#         while True:
#             line = await capfd.stdout.readline()
#             if not line:
#                 break
#             line = line.decode().strip()
#             if "Agent 1 receiving: <FOUND:" in line:
#                 found_messages_agent1 += 1
#             elif "Agent 2 receiving: <FOUND:" in line:
#                 found_messages_agent2 += 1

#     # Start reading stdout
#     read_task = asyncio.create_task(read_stdout())

#     # Wait for 10 seconds
#     await asyncio.sleep(10)

#     # Cancel tasks
#     task1.cancel()
#     task2.cancel()

#     # Wait for tasks to be cancelled
#     await asyncio.gather(task1, task2, read_task, return_exceptions=True)

#     # Print number of FOUND messages
#     print(f"Number of 'FOUND' messages received by Agent 1: {found_messages_agent1}")
#     print(f"Number of 'FOUND' messages received by Agent 2: {found_messages_agent2}")

#     # Verifying communication
#     assert found_messages_agent1 > 0, "No 'FOUND' messages received by Agent 1"
#     assert found_messages_agent2 > 0, "No 'FOUND' messages received by Agent 2"

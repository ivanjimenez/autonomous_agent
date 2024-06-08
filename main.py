from agent.agent import Agent
from behaviours.message_generator import MessageGenerator
from handlers.filter_world import FilterWord
from typing import List
from agent.agent import Agent
import asyncio

async def main():
    
    ALPHABET = ['hello', 'sun', 'world', 'space', 'moon', 'crypto', 'sky', 'ocean', 'universe']
    WORD = 'hello'
    message_generator = MessageGenerator(alphabet=ALPHABET)
    filter_word = FilterWord(WORD)

    agent1 = Agent('Agent 1')
    agent2 = Agent('Agent 2')
    
    agent1.register_handle(filter_word)
    agent1.register_behaviour(message_generator)

    agent2.register_handle(filter_word)
    agent2.register_behaviour(message_generator)

    agent1.set_other_agent(agent2)
    agent2.set_other_agent(agent1)

    task1 = asyncio.create_task(agent1.run())
    task2 = asyncio.create_task(agent2.run())
    # task3 = asyncio.create_task(agent1.generate_messages())
    # task4 = asyncio.create_task(agent2.generate_messages())

    tasks = [task1, task2]

    # Run the tasks until they are canceled
    try:
        await asyncio.gather(*tasks)
    except asyncio.CancelledError:
        print("Tasks were cancelled")

if __name__ == '__main__':
    asyncio.run(main())

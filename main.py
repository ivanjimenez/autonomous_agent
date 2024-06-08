# Asynchronous
import asyncio
import gc

# For agent
from agent.agent import Agent
from behaviours.message_generator import MessageGenerator
from handlers.filter_world import FilterWord


async def main():
    """
        Main metho
    """
    # Setting behaviour
    behaviour_option = [
        'hello', 'sun', 'world', 'space', 'moon',
        'crypto', 'sky', 'ocean', 'universe'
    ]
    message_generator = MessageGenerator(alphabet=behaviour_option)

    # Setting handle
    handle_option = 'hello'
    filter_word = FilterWord(handle_option)

    # Creating Agents
    agent1 = Agent('Agent 1')
    agent2 = Agent('Agent 2')

    # Register handlers and behaviors for both agents
    agent1.register_handle(filter_word)
    agent1.register_behaviour(message_generator)

    agent2.register_handle(filter_word)
    agent2.register_behaviour(message_generator)

    # Seting inbox from an agent to other and viceversa
    agent1.set_other_agent(agent2)
    agent2.set_other_agent(agent1)

    # Create asynchronous tasks for running the agents
    task1 = asyncio.create_task(agent1.run())
    task2 = asyncio.create_task(agent2.run())

    # Grouping in task list
    tasks = [task1, task2]

    # Run the tasks until they are canceled
    try:
        await asyncio.gather(*tasks)
    except asyncio.CancelledError:
        print("Tasks were cancelled")

if __name__ == '__main__':
    # Uncomment to adjust garbage collector thresholds if needed
    gc.set_threshold(1000, 10, 10)
    asyncio.run(main(), debug=True)

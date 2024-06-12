"""Main module for testing purposes"""
import asyncio
import gc
import time
import logging
import tracemalloc
from typing import Callable, Tuple

from agent.simple_agent import SimpleAgent
from behaviours.simple_message_generator import SimpleMessageGenerator
from handlers.filter_handler import FilterHandler
from helpers.custom_stats import print_stats
from helpers.logging_config import setup_logging

async def main(agent_factory: Callable[[], Tuple[SimpleAgent, SimpleAgent]]
)-> None:
    """
    Main method that provides:
    - The instances of agent1 and agent2
    - Setting of Handle and behaviour configuration for agent1 and agent2.
    - Configuration of concrete agents where the InBox of agent 1 is the OutBox of
    agent 2 and vice versa
    - Asynchronous Tasks creation via asyncio module
    - Running the tasks
    
    :param: agent_factory: is a function that returns two agents instances
    """
    tasks = []

    (message_generator, filter_word) = set_handler_behaviour()
    # Creating Agents
    agent1, agent2 = agent_factory()

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
    tasks.append(task1)
    tasks.append(task2)

    # Run the tasks until they are canceled
    try:
        await asyncio.gather(*tasks)
    except asyncio.CancelledError:
        print("Tasks were cancelled")

def callback(agent1 : SimpleAgent, 
             agent2: SimpleAgent
)-> None:
    """
    New behaviour and handler
    """
    new_behaviour_option = [
        'barcelona', 'madrid', 'Manchester', 'mancity', 'liverpool', 'bayern' , 'milan'
    ]
    new_message_generator = SimpleMessageGenerator(input_data=new_behaviour_option)
    new_handle_option = 'barcelona'
    new_filter_word = FilterHandler(message=new_handle_option)

    # Update agents
    agent1.register_behaviour(new_message_generator)
    agent1.register_handle(new_filter_word)

    agent2.register_behaviour(new_message_generator)
    agent2.register_handle(new_filter_word)

    print("Callback executed! Updated behaviour and handle.")

def schedule_callback(loop, 
                      agent_factory: Callable[[], Tuple[SimpleAgent, SimpleAgent]]
)-> None:
    """
    Callback
    """
    agent1, agent2 = agent_factory()
    loop.call_later(5, callback, agent1, agent2)  # Ejecutar el callback después de 5 segundos

if __name__ == '__main__':
    # Uncomment to adjust garbage collector thresholds if needed
    # gc.set_threshold(10000, 10, 10) 

    # Vars used to make some stats
    init : float = 0
    end : float = 0
    stats : dict = {}

    setup_logging()

    def set_handler_behaviour(
            
    )-> Tuple[SimpleMessageGenerator, FilterHandler]:
        """
        Setting a new behaviour and handle
        """ 
        behaviour_option = [
            'hello', 'sun', 'world', 'space', 'moon',
            'crypto', 'sky', 'ocean', 'universe'
        ]
        message_generator = SimpleMessageGenerator(input_data=behaviour_option)
        

        # Setting handle

        handle_option = 'hello'
        filter_word = FilterHandler(message=handle_option)
        return message_generator, filter_word

    # Creating the two Agents: agent1, agent2
    agent1 = SimpleAgent('Agent 1')
    agent2 = SimpleAgent('Agent 2')
  
    def agent_factory() -> Tuple[SimpleAgent, SimpleAgent]:
        """
        To ease the agent creation
        :return: return agents
        """
        return agent1, agent2
 
    # To prevent DeprecationWarning in python versions >= 3.11
    # a loop with asyncio.new_event_loop() is possible to use to remove this warning
    
    loop = asyncio.get_event_loop()   
    schedule_callback(loop, agent_factory)
    try:
        init = time.time()
         # Start memory tracking
        tracemalloc.start()
        loop.run_until_complete(main(agent_factory))
       
    except KeyboardInterrupt as e:
        print(f"Tasks interrupted {e}")
    finally:
        # Cancel all running tasks
        tasks = asyncio.all_tasks(loop)
        for task in tasks:
            task.cancel()
            # Try to cancel tasks in a safe mode
            try:
                loop.run_until_complete(task)
            except asyncio.CancelledError:
                print(f"Task {task} was cancelled.")
        # Closing the loop and show stats
        loop.close()
        end = time.time()
        logging.info(f"""
                     Closing event loop correctly
                     Time: {end - init:.2f} seconds
                     {print_stats(tracemalloc)}
                     """)
        # Stop memory tracking
        tracemalloc.stop()
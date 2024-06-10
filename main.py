# Asynchronous
import asyncio
import gc
import time
from typing import Callable, Tuple

# For agent
from agent.agent import Agent
from behaviours.simple_message_generator import SimpleMessageGenerator
from handlers.filter_handler import FilterHandler


async def main(agent_factory: Callable[[], Tuple[Agent, Agent]]):
    """
        Main method
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

def callback(agent1, agent2):
    # New behaviour and handler
    new_behaviour_option = [
        'barcelona', 'madrid', 'Manchester', 'mancity', 'liverpool', 'bayern' , 'milan'
    ]
    new_message_generator = SimpleMessageGenerator(alphabet=new_behaviour_option)
    new_handle_option = 'barcelona'
    new_filter_word = FilterHandler(new_handle_option)

    # Update agents
    agent1.register_behaviour(new_message_generator)
    agent1.register_handle(new_filter_word)

    agent2.register_behaviour(new_message_generator)
    agent2.register_handle(new_filter_word)

    print("Callback executed! Updated behaviour and handle.")

def schedule_callback(loop, agent_factory: Callable[[], Tuple[Agent, Agent]]):
    agent1, agent2 = agent_factory()
    loop.call_later(5, callback, agent1, agent2)  # Ejecutar el callback después de 5 segundos

if __name__ == '__main__':
    # Uncomment to adjust garbage collector thresholds if needed
    # gc.set_threshold(1000, 10, 10)
    # asyncio.run(main(), debug=True)

    def set_handler_behaviour()->Tuple[SimpleMessageGenerator, FilterHandler]:
        # Setting behaviour
        behaviour_option = [
            'hello', 'sun', 'world', 'space', 'moon',
            'crypto', 'sky', 'ocean', 'universe'
        ]
        message_generator = SimpleMessageGenerator(alphabet=behaviour_option)

        # Setting handle
        handle_option = 'hello'
        filter_word = FilterHandler(handle_option)
        return message_generator, filter_word

    agent1 = Agent('Agent 1')
    agent2 = Agent('Agent 2')
    
    def agent_factory(
            
    ) -> Tuple[Agent, Agent]:
        """
        :return: return agents
        """
        return agent1, agent2
 
    loop = asyncio.get_event_loop()
    schedule_callback(loop, agent_factory)
    try:
        init = time.time()
        loop.run_until_complete(main(agent_factory))
        end = time.time()
        print(f"Time: {end - init}")
    except KeyboardInterrupt as e:
        print(f"Tasks interrupted {e}")
    finally:
        # Cancelar todas las tareas que están actualmente en ejecución
        tasks = asyncio.all_tasks(loop)
        for task in tasks:
            task.cancel()
            # Intentar finalizar las tareas de manera limpia
            try:
                loop.run_until_complete(task)
            except asyncio.CancelledError:
                print(f"Task {task} was cancelled.")
        # Finalmente, cerrar el loop
        loop.close()
        print("Closing event loop correctly")

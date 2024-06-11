import unittest
import logging
from unittest.mock import MagicMock
import asyncio
from agent.simple_agent import SimpleAgent
from behaviours.simple_message_generator import SimpleMessageGenerator
from handlers.filter_handler import FilterHandler

class TestMainIntegration(unittest.IsolatedAsyncioTestCase):

    async def test_main_integration(self):
        # Mockear instancias de agentes, manejadores y comportamientos
        agent1 = MagicMock(spec=SimpleAgent)
        agent2 = MagicMock(spec=SimpleAgent)
        message_generator = MagicMock(spec=SimpleMessageGenerator)
        filter_handler = MagicMock(spec=FilterHandler)

        # Crear instancias de los mocks
        agent1.return_value = agent1
        agent2.return_value = agent2
        message_generator.return_value = message_generator
        filter_handler.return_value = filter_handler

        # Configurar agentes con mocks de manejadores y comportamientos
        agent1.register_handle.return_value = None
        agent1.register_behaviour.return_value = None
        agent2.register_handle.return_value = None
        agent2.register_behaviour.return_value = None

        # Establecer la comunicación entre agentes
        agent1.set_other_agent.return_value = None
        agent2.set_other_agent.return_value = None

        # Crear tareas asincrónicas para ejecutar los mocks de agentes
        task1 = asyncio.create_task(agent1.run())
        task2 = asyncio.create_task(agent2.run())

        # Ejecutar las tareas hasta que sean canceladas
        try:
            await asyncio.gather(task1, task2)
            print("Tareas de los agentes completadas con éxito.")
            logging.info("Tareas de los agentes completadas con éxito.")
        except asyncio.CancelledError:
            print("Tareas canceladas")
            logging.error("Las tareas fueron canceladas.")

        # Agregar más aserciones según sea necesario

if __name__ == '__main__':
    unittest.main(verbosity=2)

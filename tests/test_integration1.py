# import unittest
# import asyncio
# from unittest.mock import MagicMock
# from agent.simple_agent import SimpleAgent
# from behaviours.simple_message_generator import SimpleMessageGenerator
# from handlers.filter_handler import FilterHandler

# class TestMainIntegration(unittest.IsolatedAsyncioTestCase):

#     async def test_main_integration(self):
#         # Crear instancias de agentes, manejadores y comportamientos
#         agent1 = SimpleAgent('Agent1')
#         agent2 = SimpleAgent('Agent2')
#         message_generator = SimpleMessageGenerator(alphabet=['hello', 'sun', 'world', 'space', 'moon', 'crypto', 'sky', 'ocean', 'universe'])
#         filter_handler = FilterHandler('hello')

#         # Configurar el primer handle y behavior en los agentes
#         agent1.register_handle(filter_handler)
#         agent1.register_behaviour(message_generator)
#         agent2.register_handle(filter_handler)
#         agent2.register_behaviour(message_generator)

#         # Configurar la comunicación entre los agentes
#         agent1.set_other_agent(agent2)
#         agent2.set_other_agent(agent1)

#         # Crear tareas asincrónicas para ejecutar los agentes
#         task1 = asyncio.create_task(agent1.run())
#         task2 = asyncio.create_task(agent2.run())

#         # Ejecutar las tareas hasta que sean canceladas
#         try:
#             await asyncio.gather(task1, task2)
#         except asyncio.CancelledError:
#             print("Tareas canceladas")

#         # Actualizar los handles y behaviors en los agentes
#         new_message_generator = SimpleMessageGenerator(alphabet=['barcelona', 'madrid', 'Manchester', 'mancity', 'liverpool', 'bayern' , 'milan'])
#         new_filter_handler = FilterHandler('barcelona')

#         agent1.register_handle(new_filter_handler)
#         agent1.register_behaviour(new_message_generator)
#         agent2.register_handle(new_filter_handler)
#         agent2.register_behaviour(new_message_generator)

#         # Crear tareas asincrónicas para ejecutar los agentes actualizados
#         task1 = asyncio.create_task(agent1.run())
#         task2 = asyncio.create_task(agent2.run())

#         # Ejecutar las tareas hasta que sean canceladas
#         try:
#             await asyncio.gather(task1, task2)
#         except asyncio.CancelledError:
#             print("Tareas canceladas")

#         # Agregar más aserciones según sea necesario

# if __name__ == '__main__':
#     unittest.main()

import asyncio
import pytest
from unittest.mock import MagicMock
from agent.simple_agent import SimpleAgent
from handlers.filter_handler import FilterHandler
from behaviours.simple_message_generator import SimpleMessageGenerator

@pytest.mark.asyncio
async def test_agent_integration():
    # Mock para el manejador (handler) FilterHandler
    filter_handler_mock = MagicMock(spec=FilterHandler)
    filter_handler_mock.run_handle.side_effect = lambda message: f"<FOUND: {message}>" if "hello" in message else f"<NOT FOUND: {message}>"

    # Mock para el comportamiento (behaviour) SimpleMessageGenerator
    behaviour_mock = MagicMock(spec=SimpleMessageGenerator)
    behaviour_mock.use_behaviour.side_effect = ["hello world", "sun sky"]

    # Crear instancia de agente 1
    agent1 = SimpleAgent("Agent 1")
    agent1.register_handle(filter_handler_mock)
    agent1.register_behaviour(behaviour_mock)

    # Crear instancia de agente 2
    agent2 = SimpleAgent("Agent 2")
    agent2.register_handle(filter_handler_mock)
    agent2.register_behaviour(behaviour_mock)

    # Establecer los agentes como pares
    agent1.set_other_agent(agent2)
    agent2.set_other_agent(agent1)

    # Ejecutar los agentes
    task1 = asyncio.create_task(agent1.run())
    task2 = asyncio.create_task(agent2.run())

    # Esperar 5 segundos
    await asyncio.sleep(5)

    # Cancelar tareas
    task1.cancel()
    task2.cancel()

    # Esperar a que las tareas sean canceladas
    await asyncio.gather(task1, task2, return_exceptions=True)

    # Verificar que el manejador fue llamado con los mensajes correctos
    filter_handler_mock.run_handle.assert_any_call("hello world")
    filter_handler_mock.run_handle.assert_any_call("sun sky")

    # Verificar que el comportamiento fue llamado
    behaviour_mock.use_behaviour.assert_any_call()
    behaviour_mock.use_behaviour.assert_any_call()

    # Verificar que el manejador fue llamado con un mensaje que contiene "hello"
    assert filter_handler_mock.run_handle.call_args_list[0][0][0] == "hello world"
    assert filter_handler_mock.run_handle.call_args_list[1][0][0] == "sun sky"

    # Verificar que el agente 1 envió y recibió correctamente el mensaje
    assert "Agent 1 sending: hello world" in agent1.log_output
    assert "Agent 2 receiving: <FOUND: hello world>" in agent2.log_output

    # Verificar que el agente 2 envió y recibió correctamente el mensaje
    assert "Agent 2 sending: sun sky" in agent2.log_output
    assert "Agent 1 receiving: <FOUND: sun sky>" in agent1.log_output

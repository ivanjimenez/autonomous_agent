import asyncio
import uuid
import secrets
import sys
import random

class Agente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cola_entrada = asyncio.Queue()

    async def enviar_mensaje(self, mensaje, destinatario):
        mensaje_id = secrets.token_hex(4)
        color = random.randint(31, 47)  # Colores ANSI entre 31 y 37
        mensaje_id = f"\033[{color}m{mensaje_id}\033[0m"
        print(f"{self.nombre} enviando mensaje {mensaje_id} a {destinatario.nombre}")
        await destinatario.cola_entrada.put((mensaje_id, mensaje))

    async def recibir_mensaje(self):
        while True:
            mensaje_id, mensaje = await self.cola_entrada.get()
            print(f"{self.nombre} recibió mensaje {mensaje_id}: {mensaje}")
            self.cola_entrada.task_done()

    async def iniciar(self):
        asyncio.create_task(self.recibir_mensaje())

async def signal_handler():
    print("Señal de interrupción recibida, deteniendo agentes...")
    tasks = [task for task in asyncio.all_tasks() if task is not asyncio.current_task()]
    for task in tasks:
        task.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)
    sys.exit(0)

async def main():
    agente1 = Agente("Agente1")
    agente2 = Agente("Agente2")

    await agente1.iniciar()
    await agente2.iniciar()

    # Enviar mensajes entre los agentes en un bucle infinito
    try:
        while True:
            await agente1.enviar_mensaje("Hola desde Agente1", agente2)
            await agente2.enviar_mensaje("Hola desde Agente2", agente1)
            await asyncio.sleep(2)
    except asyncio.CancelledError:
        pass

if __name__ == "__main__":
    asyncio.run(main())
import asyncio

async def download_data(source):
    print(f"Iniciando descarga de {source}...")
    await asyncio.sleep(2)  # Simulando el tiempo de descarga
    if source == "fuente 2":
        raise ValueError("Error al descargar de fuente 2")  # Simular un error
    print(f"Datos descargados de {source}")
    return f"Datos de {source}"

async def process_data(data):
    print(f"Procesando {data}...")
    await asyncio.sleep(3)  # Simulando el tiempo de procesamiento
    print(f"{data} procesados")
    return f"{data} procesados"

async def store_data(data):
    print(f"Almacenando {data}...")
    await asyncio.sleep(2)  # Simulando el tiempo de almacenamiento
    print(f"{data} almacenados")

async def main():
    sources = ["fuente 1", "fuente 2", "fuente 3"]
    tasks = []

    for source in sources:
        task = asyncio.create_task(download_process_store(source))
        tasks.append(task)

    # Ejecutar todas las tareas y manejar excepciones
    for task in tasks:
        try:
            await task
        except Exception as e:
            print(f"Error manejado: {e}")

async def download_process_store(source):
    try:
        data = await download_data(source)
        processed_data = await process_data(data)
        await store_data(processed_data)
    except Exception as e:
        print(f"Error en el flujo {source}: {e}")
        raise  # Volver a lanzar la excepción para que sea capturada en main()

def callback():
    print("Callback ejecutado!")

def schedule_callback(loop):
    loop.call_later(5, callback)  # Ejecutar el callback después de 5 segundos
    
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    schedule_callback(loop)
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
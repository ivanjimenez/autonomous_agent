# Implementación básica de programación reactiva en Python


"""
    En este ejemplo, tenemos tres clases:

Observable: Representa el objeto que emite eventos. 
            Tiene un método subscribe para que los observadores se registren y un método notify 
            para notificar a los observadores cuando ocurre un evento.

DataSource: Es un objeto que mantiene un valor interno y notifica a los observadores 
            cuando este valor cambia.

DataConsumer: Representa un observador que consume los datos emitidos por la fuente. 
              En este caso, simplemente imprime los datos que recibe.

Al ejecutar este código, verás que ambos consumidores reciben los datos emitidos 
por la fuente cuando esta cambia su valor. 
Esto es una implementación simple de programación reactiva en Python sin utilizar librerías externas.
"""

class Observable:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, data):
        for observer in self.observers:
            observer(data)

class DataSource:
    def __init__(self):
        self.value = 0
        self.observable = Observable()

    def set_value(self, value):
        self.value = value
        self.observable.notify(self.value)

class DataConsumer:
    def __init__(self, name):
        self.name = name

    def consume(self, data):
        print(f"{self.name} recibió el dato: {data}")

# Crear instancias de DataSource y DataConsumer
source = DataSource()
consumer1 = DataConsumer("Consumer 1")
consumer2 = DataConsumer("Consumer 2")

# Suscribir consumidores a la fuente de datos
source.observable.subscribe(consumer1.consume)
source.observable.subscribe(consumer2.consume)

# Cambiar el valor de la fuente de datos
source.set_value(10)
source.set_value(20)

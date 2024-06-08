import asyncio
import random

class AutonomousAgent:
    def __init__(self):
        self.handlers = {}
        self.behaviors = []
        self.inbox = asyncio.Queue()
        self.outbox = asyncio.Queue()
        self.running = True

    def register_handler(self, message_type, handler):
        if message_type not in self.handlers:
            self.handlers[message_type] = []
        self.handlers[message_type].append(handler)

    def register_behavior(self, behavior):
        self.behaviors.append(behavior)

    async def send_message(self, message):
        await self.outbox.put(message)

    async def receive_message(self):
        return await self.inbox.get()

    async def handle_messages(self):
        while self.running:
            if not self.inbox.empty():
                message = await self.receive_message()
                message_type = message['type']
                if message_type in self.handlers:
                    for handler in self.handlers[message_type]:
                        await handler(message)

            for behavior in self.behaviors:
                message = behavior()
                if message:
                    await self.send_message(message)

            await asyncio.sleep(1)  # Adjust sleep time as needed

    def stop(self):
        self.running = False

class ConcreteAgent(AutonomousAgent):
    def __init__(self):
        super().__init__()

    async def handle_hello(self, message):
        print(message)

    def generate_message(self):
        if random.random() < 0.5:  # Adjust probability as needed
            return {'type': 'random_message', 'content': ' '.join(random.sample(["hello", "sun", "world", "space", "moon", "crypto", "sky", "ocean", "universe", "human"], 2))}

async def main():
    agent1 = ConcreteAgent()
    agent2 = ConcreteAgent()

    agent1.register_handler("random_message", agent2.receive_message)
    agent2.register_handler("random_message", agent1.receive_message)

    agent1.register_behavior(agent1.generate_message)
    agent2.register_behavior(agent2.generate_message)

    # Start agent tasks
    task1 = asyncio.create_task(agent1.handle_messages())
    task2 = asyncio.create_task(agent2.handle_messages())

    # Let the agents run for some time
    await asyncio.sleep(10)

    # Stop agents
    # agent1.stop()
    # agent2.stop()

    await task1
    await task2

if __name__ == '__main__':
    asyncio.run(main())

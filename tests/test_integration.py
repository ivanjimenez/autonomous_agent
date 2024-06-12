import unittest
import asyncio
from agent.simple_agent import SimpleAgent
from handlers.filter_handler import FilterHandler
from behaviours.simple_message_generator import SimpleMessageGenerator
from helpers.logging_config import setup_logging_file
import re
from config import LOG_FILE_PATH


setup_logging_file()
class TestIntegration(unittest.TestCase):
    
    print(f"#### Starting TEST AGENTS INTEGRATION")

    def setUp(self):
        self.alphabet = [
            'hello', 'sun', 'world', 'space', 'moon', 
            'crypto', 'sky', 'ocean', 'universe'
        ]
        self.word = 'hello'
        self.agent1 = SimpleAgent('Agent 1')
        self.agent2 = SimpleAgent('Agent 2')
        self.filter_word = FilterHandler(self.word)
        self.message_generator = SimpleMessageGenerator(self.alphabet)

        self.agent1.register_handle(self.filter_word)
        self.agent1.register_behaviour(self.message_generator)
        self.agent2.register_handle(self.filter_word)
        self.agent2.register_behaviour(self.message_generator)
        self.agent1.set_other_agent(self.agent2)
        self.agent2.set_other_agent(self.agent1)

        self.log_file_path = LOG_FILE_PATH

    def remove_ansi_escape_sequences(self, file_path):
        ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
        with open(file_path, 'r') as file:
            log_content = file.read()
        clean_content = ansi_escape.sub('', log_content)
        with open(file_path, 'w') as file:
            file.write(clean_content)
    
    def count_found_not_found(self, file_path):
        found_count = 0
        not_found_count = 0
        
        found_pattern = re.compile(r'<FOUND: .* id \w{10}>')
        not_found_pattern = re.compile(r'<NOT FOUND: .* id \w{10}>')
        
        with open(file_path, 'r') as file:
            for line in file:
                if found_pattern.search(line):
                    found_count += 1
                elif not_found_pattern.search(line):
                    not_found_count += 1
        
        return found_count, not_found_count
    
    def print_log_file(self, file_path):
        with open(file_path, 'r') as file:
            log_content = file.read()
        print(log_content)

    async def test_agent_interaction(self):
        # Create and start tasks
        
        task1 = asyncio.create_task(self.agent1.run())
        task2 = asyncio.create_task(self.agent2.run())

        try:
            await asyncio.sleep(5)  # Run the agents for 4 seconds
        finally:
            task1.cancel()
            task2.cancel()

            # Await cancellation of tasks
            try:
                await task1
            except asyncio.CancelledError:
                print("Agent 1 task was cancelled")

            try:
                await task2
            except asyncio.CancelledError:
                print("Agent 2 task was cancelled")
        
        self.remove_ansi_escape_sequences(self.log_file_path)
        found, not_found = self.count_found_not_found(self.log_file_path)
        print(">>> Tests Results")
        print(f"FOUND count: {found}")
        print(f"NOT FOUND count: {not_found}")
        print(f"""
              >>> The previous stdout is recorded in the following stdouput <<<
              >>> Just compare the resultos above and below                 <<<
              >>> Integration Tests improvements in future versions :-> !!  <<<
              """)
        self.print_log_file(self.log_file_path)

    def test_async(self):
        asyncio.run(self.test_agent_interaction())

if __name__ == '__main__':
    unittest.main()

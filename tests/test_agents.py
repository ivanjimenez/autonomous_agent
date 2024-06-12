# import unittest
# from unittest.mock import MagicMock
# from handlers.filter_handler import FilterHandler
# from behaviours.simple_message_generator import SimpleMessageGenerator

# class TestHandlersAndBehaviours(unittest.TestCase):
#     def test_filter_handler(self):
#         # Crear una instancia del manejador
#         handler = FilterHandler("hello")

#         # Verificar que el manejador se crea correctamente
#         self.assertIsInstance(handler, FilterHandler)
#         self.assertEqual(handler.content, "hello")

#         # Verificar que el manejador devuelve los resultados esperados
#         self.assertEqual(handler.run_handle("hello world"), "<FOUND: hello world>")
#         self.assertEqual(handler.run_handle("sun sky"), "<NOT FOUND: sun sky>")

#     def test_simple_message_generator(self):
#         # Crear una instancia del comportamiento
#         behaviour = SimpleMessageGenerator(["hello", "sun", "world", "sky"])

#         # Verificar que el comportamiento se crea correctamente
#         self.assertIsInstance(behaviour, SimpleMessageGenerator)
#         self.assertEqual(behaviour.alphabet, ["hello", "sun", "world", "sky"])

#         # Verificar que el comportamiento genera mensajes correctamente
#         msg = behaviour.process_message()
#         self.assertEqual(len(msg.split()), 2)

#         alphabet = ["hello", "sun", "world", "sky"]
#         word1, word2 = msg.split()
#         self.assertIn(word1, alphabet)
#         self.assertIn(word2, alphabet)

# if __name__ == '__main__':
#     unittest.main()

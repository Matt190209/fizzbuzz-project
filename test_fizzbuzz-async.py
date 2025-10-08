import unittest
import asyncio
from FizzBuzz_Alternative import FizzBuzzGame  # Asegúrate de que el nombre coincide con tu archivo

class TestFizzBuzzGame(unittest.IsolatedAsyncioTestCase):

    async def test_get_fizzbuzz_value(self):
        # Creamos un juego con los mismos jugadores de tu main
        game = FizzBuzzGame(["Abdul", "Bart", "Claudia", "Divya"], (3,5), 20)

        # Lista de pruebas: (input, resultado esperado)
        tests = [
            (1, "1"),
            (3, "¡fizz!"),
            (5, "¡buzz!"),
            (15, "¡fizzbuzz!"),
            (7, "7"),
        ]

        for number, expected in tests:
            result = game.get_fizzbuzz_value(number)
            self.assertEqual(result, expected)

    async def test_game_progression(self):
        # Jugadores como en tu main
        player_names = ["Abdul", "Bart", "Claudia", "Divya"]
        game = FizzBuzzGame(player_names, (3,5), 20)

        # Ejecutar el juego de manera async
        await game.start()

        # Verificar que terminó el juego
        self.assertTrue(game.finished)
        self.assertEqual(game.current_number, 21)  # max_number + 1

if __name__ == "__main__":
    unittest.main()

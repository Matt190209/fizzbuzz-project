import pytest
import threading
import io
import sys
import time
from contextlib import redirect_stdout

from FizzBuzz import FizzBuzzGame  

# ---------- TEST UNITARIO BÁSICO ----------
def test_fizzbuzz_values():
    """Valida que la lógica FizzBuzz sea correcta."""
    game = FizzBuzzGame(["A", "B"], (3, 5), 15)

    assert game.get_fizzbuzz_value(3) == "¡fizz!"
    assert game.get_fizzbuzz_value(5) == "¡buzz!"
    assert game.get_fizzbuzz_value(15) == "¡fizzbuzz!"
    assert game.get_fizzbuzz_value(2) == "2"


# ---------- TEST INTEGRADO DEL JUEGO ----------
def test_game_sequence(monkeypatch):
    """
    Captura la salida del juego y valida:
    - Que se impriman líneas con formato correcto
    - Que el número total de líneas coincida con max_number
    - Que la secuencia aumente ordenadamente
    """

    names = ["A", "B", "C"]
    game = FizzBuzzGame(names, (2, 3), 6)

    # Capturar salida de consola
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        game.start()

    output = buffer.getvalue().strip().splitlines()

    # Filtrar solo las líneas donde los jugadores hablan
    lines = [l for l in output if "dice" in l]

    assert len(lines) == game.max_number, "Debe haber una línea por número"
    assert lines[0].startswith("A dice 1"), "El primer jugador debe empezar con 1"

    # Validar que el orden de jugadores se repita correctamente
    sequence = [line.split()[0] for line in lines]
    expected_pattern = [names[i % len(names)] for i in range(len(lines))]
    assert sequence == expected_pattern, "Los jugadores deben turnarse correctamente"

    # Validar que el juego terminó correctamente
    assert any("Game over" in line for line in output), "Debe imprimir fin del juego"
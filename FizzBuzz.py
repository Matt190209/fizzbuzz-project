import threading
import time

class Player(threading.Thread):
    def __init__(self, name, game, position):
        super().__init__()
        self.name = name
        self.game = game
        self.position = position

    def run(self):
        while True:
            with self.game.condition:
                while self.game.current_player != self.position and not self.game.finished:
                    self.game.condition.wait()

                if self.game.finished:
                    break

                number = self.game.current_number
                output = self.game.get_fizzbuzz_value(number)
                print(f"{self.name} dice {output}")

                self.game.current_number += 1
                if self.game.current_number > self.game.max_number:
                    self.game.finished = True
                    self.game.condition.notify_all()
                    break

                self.game.current_player = (self.game.current_player + 1) % len(self.game.players)
                self.game.condition.notify_all()

            time.sleep(0.1)
class FizzBuzzGame:
    def __init__(self, players_names, divisors=(3, 5), max_number=20):
        self.players = []
        self.players_names = players_names
        self.divisors = divisors
        self.max_number = max_number
        self.current_number = 1
        self.current_player = 0
        self.finished = False
        self.condition = threading.Condition()

        for i, name in enumerate(players_names):
            self.players.append(Player(name, self, i))

    def get_fizzbuzz_value(self, number):
        fizz, buzz = self.divisors
        if number % fizz == 0 and number % buzz == 0:
            return "¡fizzbuzz!"
        elif number % fizz == 0:
            return "¡fizz!"
        elif number % buzz == 0:
            return "¡buzz!"
        else:
            return str(number)

    def start(self):
        print(f"\n🎮 Start the game with {len(self.players)} players:\n")
        for p in self.players:
            p.start()
        for p in self.players:
            p.join()
        print("\n✅ Game over.\n")


if __name__ == "__main__":
    # Opción 1: Juego estándar
    names = ["Abdul", "Bart", "Claudia", "Divya"]
    FizzBuzzGame(names, (3, 5), 20).start()

    # Opción 2: Juego personalizado
    custom_names = ["Matthieu", "Sofía", "Nico"]
    FizzBuzzGame(custom_names, (2, 7), 15).start()

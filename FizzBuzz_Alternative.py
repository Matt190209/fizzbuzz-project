import asyncio

class Player:
    def __init__(self, name, position, game):
        self.name = name
        self.position = position
        self.game = game

    async def play(self):
        while True:
            await self.game.turn_event[self.position].wait()
            if self.game.finished:
                break

            num = self.game.current_number
            text = self.game.get_fizzbuzz_value(num)
            print(f"{self.name} dice {text}")
            await asyncio.sleep(0.1)

            self.game.current_number += 1
            if self.game.current_number > self.game.max_number:
                self.game.finished = True
                for ev in self.game.turn_event:
                    ev.set()
                break

            self.game.turn_event[self.position].clear()
            next_p = (self.position + 1) % len(self.game.players)
            self.game.turn_event[next_p].set()

class FizzBuzzGame:
    def __init__(self, player_names, divisors=(3,5), max_number=20):
        self.players = [Player(name, i, self) for i, name in enumerate(player_names)]
        self.divisors = divisors
        self.max_number = max_number
        self.current_number = 1
        self.finished = False
        self.turn_event = [asyncio.Event() for _ in self.players]
        self.turn_event[0].set()  # empieza el primer jugador

    def get_fizzbuzz_value(self, n):
        f, b = self.divisors
        if n % f == 0 and n % b == 0: return "¡fizzbuzz!"
        if n % f == 0: return "¡fizz!"
        if n % b == 0: return "¡buzz!"
        return str(n)

    async def start(self):
        print("\n🎮 Comienza el juego (modo async)\n")
        await asyncio.gather(*(p.play() for p in self.players))
        print("\n✅ Juego terminado.\n")

if __name__ == "__main__":
    asyncio.run(FizzBuzzGame(["Abdul", "Bart", "Claudia", "Divya"], (3,5), 20).start())
    asyncio.run(FizzBuzzGame(["Matthieu", "Sofía", "Nico"], (2,7), 15).start())
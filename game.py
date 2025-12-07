import random

class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.x = 0
        self.y = 0
        self.health = 100
        self.coin = 0

    def move(self, direction, map_size):
        if direction == "w":
            if self.x > 0:
                self.x -= 1
            else:
                print("You cannot move that way!")
        elif direction == "s":
            if self.x < map_size - 1:
                self.x += 1
            else:
                print("You cannot move that way!")
        elif direction == "a":
            if self.y > 0:
                self.y -= 1
            else:
                print("You cannot move that way!")
        elif direction == "d":
            if self.y < map_size - 1:
                self.y += 1
            else:
                print("You cannot move that way!")


class GameMap:
    def __init__(self, size=9):
        self.size = size

    def draw(self, player):
        for i in range(self.size):
            row = ""
            for j in range(self.size):
                if i == player.x and j == player.y:
                    row += "C "
                elif i == self.size - 1 and j == self.size - 1:
                    row += "M "
                else:
                    row += ". "
            print(row.strip())
        print(f"Health: {player.health}")
        print(f"Coin: {player.coin}")


class Game:
    def __init__(self):
        self.map_size = 9
        self.player = Player()
        self.map = GameMap(self.map_size)
        # Default events list (tests override this)
        self.events = ["find a coin", "meet a monster", "do nothing"]
        self.game_name = "All You Can Eat Buffet"

    def check_event(self):
        if self.events:
            event = self.events.pop(0)
        else:
            event = random.choice(["find a coin", "meet a monster", "do nothing"])

        if event == "find a coin":
            self.player.coin += 1
        elif event == "meet a monster":
            self.player.health -= 10
        # do nothing → no change

    def play(self):
        # Welcome message & name prompt
        print("Welcome to " + self.game_name + "!")
        print("======================")
        self.player.name = input("Before we begin, what is your character's name?\n> ")
        print("Bigback")
        print(f"Great, {self.player.name}! Let's begin the adventure!\n")

        direction = ""
        while direction != "q":
            self.map.draw(self.player)
            direction = input("Your next move (w/a/s/d/q): ").strip()
            if direction == "q":
                break
            self.player.move(direction, self.map_size)
            # Win condition
            if self.player.x == self.map_size - 1 and self.player.y == self.map_size - 1:
                print("Congratulations! You reach the gate for next level.")
                break
            self.check_event()


if __name__ == "__main__":
    Game().play()
  
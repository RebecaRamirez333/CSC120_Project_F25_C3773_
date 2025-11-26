import random

#2.1 Greet the player
game_name = "All You can Eat Buffet"
print("Welcome to " + game_name + "!")
print("======================")

# Ask for the character's name
name = input("Before we begin, what is your character's name?\n> ")

# Print the name
print("Bigback")
print("Great, " + name + "! Let's begin the adventure!")

# 2.2 Use dictionary to build character stats
player = {
    "name": name,
    "health": 100, 
    "coin": 0
}

# 2.3 Add some random events
events = ["find a coin", "meet a monster", "do nothing"]

# Randomly choose one event
event = random.choice(events)
print(f"While exploring, you {event}!")

# 2.4 Update character stats
if event == "find a coin":
    player["coin"] += 1
    print(f"{player['name']} found a coin, {player['name']} now has {player['coin']} coins.")
elif event == "meet a monster":
    player["health"] -= 10
    print(f"{player['name']} got hurt during the combat with monster, health is now {player['health']}.")
else:
    print(f"{player['name']} wandered around but nothing happened.")

import random

# 1. Change variable name to string literal
name = "Tester"

# 2. Declare global variables
player = {
    "name": name,
    "health": 100,
    "coin": 0,
    "x": 0,  # new key for player location
    "y": 0   # new key for player location
}

# Global variables
events = ["find a coin", "meet a monster", "do nothing"]
map_size = 9  # 5. map size for drawing

# 3. Put previous code logic into check_event(), but remove print() inside
def check_event():
    global player, events
    event = random.choice(events)
    if event == "find a coin":
        player["coin"] += 1
    elif event == "meet a monster":
        player["health"] -= 10
    # "do nothing" → no change


# 4. draw_ui() function
def draw_ui(x, y):
    print("=" * 25)
    for i in range(map_size):
        for j in range(map_size):
            if i == y and j == x:
                print("C", end=" ")
            elif i == map_size - 1 and j == map_size - 1:
                print("M", end=" ")
            else:
                print(".", end=" ")
        print()
    print("=" * 25)
    print(f"Health: {player['health']}")
    print("-" * 25)
    print(f"Coin: {player['coin']}")
    print("=" * 25)
    print("Your move (w/a/s/d/q):")


# 7. move() function
def move(direction):
    global player, map_size

    if direction == 'w' and player['x'] > 0:
        player['x'] -= 1
    elif direction == 'a' and player['y'] > 0:
        player['y'] -= 1
    elif direction == 's' and player['x'] < map_size - 1:
        player['x'] += 1
    elif direction == 'd' and player['y'] < map_size - 1:
        player['y'] += 1
    else:
        print("You cannot move that way!")


# 8. main() function
def main():
    draw_ui(player['x'], player['y'])
    direction = input("Your next move (w/a/s/d/q): ")

    while direction != 'q':
        move(direction)

        # Check if player reached the gate
        if player['x'] == map_size - 1 and player['y'] == map_size - 1:
            print("Congratulations! You reach the gate for next level.")
            break

        check_event()
        draw_ui(player['x'], player['y'])
        direction = input("Your next move (w/a/s/d/q): ")


# 9. Call main()
if __name__ == '__main__':
    main()
  
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


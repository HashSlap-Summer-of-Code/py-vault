import sys

def intro():
    print("\n🌄 You wake up in a dark forest. You see two paths ahead:")
    print("1. A narrow trail leading into deeper woods.")
    print("2. A rocky path climbing up a hill.")
    choice = input("Which path do you choose? (1 or 2): ")

    if choice == "1":
        forest_path()
    elif choice == "2":
        hill_path()
    else:
        print("❌ Invalid choice. Try again.")
        intro()

def forest_path():
    print("\n🌲 You walk deeper into the forest and hear growling.")
    print("1. Investigate the sound.")
    print("2. Hide behind a tree.")
    choice = input("What do you do? (1 or 2): ")

    if choice == "1":
        print("\n🐺 A wild wolf appears and chases you! You run but trip on a root.")
        game_over("You were caught by the wolf.")
    elif choice == "2":
        print("\n🦉 You quietly hide. The sound fades. You find a hidden map near the tree.")
        cave_path()
    else:
        print("❌ Invalid choice. Try again.")
        forest_path()

def hill_path():
    print("\n⛰️ You climb the hill and find an abandoned cabin.")
    print("1. Enter the cabin.")
    print("2. Walk past it.")
    choice = input("What do you do? (1 or 2): ")

    if choice == "1":
        print("\n🏚️ Inside the cabin, you find food and a lantern. It’s getting dark.")
        cave_path()
    elif choice == "2":
        print("\n🌌 You get lost as night falls. It’s too dark to see, and you fall into a ditch.")
        game_over("You got lost in the darkness.")
    else:
        print("❌ Invalid choice. Try again.")
        hill_path()

def cave_path():
    print("\n🗺️ The map leads you to a cave entrance lit by fireflies.")
    print("1. Enter the cave.")
    print("2. Stay outside.")
    choice = input("What do you do? (1 or 2): ")

    if choice == "1":
        treasure_room()
    elif choice == "2":
        game_over("You waited too long, and a storm forces you to retreat.")
    else:
        print("❌ Invalid choice. Try again.")
        cave_path()

def treasure_room():
    print("\n💰 You enter the cave and find a glowing chest!")
    print("1. Open the chest.")
    print("2. Ignore it and explore deeper.")
    choice = input("What do you do? (1 or 2): ")

    if choice == "1":
        print("\n🎉 Inside is treasure! You’ve completed your quest successfully!")
        play_again()
    elif choice == "2":
        print("\n🕳️ You step into a trap and fall into a pit!")
        game_over("You fell into a hidden trap.")
    else:
        print("❌ Invalid choice. Try again.")
        treasure_room()

def game_over(reason):
    print(f"\n💀 Game Over: {reason}")
    play_again()

def play_again():
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    if choice in ["yes", "y"]:
        intro()
    else:
        print("Thanks for playing!")
        sys.exit()

if __name__ == "__main__":
    print("🧭 Welcome to the Text Adventure Game!")
    intro()

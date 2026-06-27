import random


def roll_dice():
    return random.randint(1, 6)


print("--- Welcome to the Dice Roller ---")

while True:
    input("\nPress Enter to roll the dice...")

    result = roll_dice()
    print(f"You rolled: {result}")

    choice = input("Roll again? (y/n): ").strip().lower()

    if choice == "n":
        print("Thanks for playing!")
        break
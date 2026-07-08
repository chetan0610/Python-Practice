# ==========================================
# Program 08: 08_DictionaryComprehension.py
# Description: Demonstrating dictionary comprehensions
# for compact and fast dictionary creation.
# ==========================================
import json

def display_dict(title, data):
    print(f"\n========== {title} ==========")
    print(json.dumps(data, indent=4))

def main():
    print("🚀 DICTIONARY COMPREHENSION SHOWCASE 🚀")

    # 1. Squares (Numbers 1 to 10)
    # Syntax: {key: value for item in iterable}
    squares = {x: x*x for x in range(1, 11)}
    display_dict("SQUARES (1 to 10)", squares)

    # 2. Cubes (Numbers 1 to 10)
    cubes = {x: x**3 for x in range(1, 11)}
    display_dict("CUBES (1 to 10)", cubes)

    # 3. Even Numbers (Squares of even numbers only)
    # Syntax: {key: value for item in iterable if condition}
    evens = {x: x**2 for x in range(1, 11) if x % 2 == 0}
    display_dict("EVEN NUMBERS (Squares)", evens)

    # 4. Odd Numbers (Squares of odd numbers only)
    odds = {x: x**2 for x in range(1, 11) if x % 2 != 0}
    display_dict("ODD NUMBERS (Squares)", odds)

    # ------------------------------------------
    # 🎯 BONUS CHALLENGE
    # ------------------------------------------
    print("\n" + "-"*35)
    print("🎯 BONUS CHALLENGE: DYNAMIC INPUT")
    print("-"*35)
    try:
        limit = int(input("Enter a number to generate squares up to: "))
        # Generates dictionary dynamically based on user input
        dynamic_squares = {x: x*x for x in range(1, limit + 1)}
        display_dict(f"SQUARES UP TO {limit}", dynamic_squares)
    except ValueError:
        print("❌ Invalid input! Please enter a valid whole number.")

    # ------------------------------------------
    # 🔥 EXTRA CHALLENGE
    # ------------------------------------------
    # ord('A') gives 65, chr(65) gives 'A'.
    # We loop from 65 to 90 (which is range(65, 91)) to get A to Z.
    ascii_dict = {chr(i): i for i in range(65, 91)}
    display_dict("🔥 EXTRA CHALLENGE: ASCII VALUES (A-Z)", ascii_dict)

    print("\nProgram Completed Successfully! 🚀")

if __name__ == "__main__":
    main()
    
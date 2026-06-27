import random

def generate_number():
    """Generates and returns a random number between 1 and 10."""
    return random.randint(1, 10)


secret_number = generate_number()

print("I have chosen a secret number between 1 and 10. Try to guess it!")

while True:
    user_guess = int(input("Enter your guess: "))

    if user_guess > secret_number:
        print("Too high! Try again.")
    elif user_guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Correct! You win!")
        break
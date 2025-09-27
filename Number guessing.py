import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    max_attempts = 7
    attempt = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempt < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempt + 1}: Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempt += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"🎉 Correct! You guessed the number in {attempt} attempt(s).")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    else:
        print(f"\n❌ You've used all {max_attempts} attempts.")
        print(f"The correct number was: {number_to_guess}")

# Run the game
number_guessing_game()

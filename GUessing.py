import random

def guessing_game():
    # Generate a random number between 1 and 50
    number_to_guess = random.randint(1, 50)
    guess = None

    print("Welcome to the Guessing Game!")
    print("Guess a number between 1 and 50.")

    # Loop until the user guesses the correct number
    while guess != number_to_guess:
        try:
            # Take the user's guess
            guess = int(input("Enter your guess: "))
            
            # Provide feedback if the guess is too high or too low
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed the right number.")
        except ValueError:
            print("Please enter a valid number.")

# Run the game
guessing_game()

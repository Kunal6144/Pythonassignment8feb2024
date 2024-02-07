import random


def guess_number():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    # Prompt the user to guess the number
    guess = None
    while guess != secret_number:
        try:
            guess = int(input("Guess the number between 1 and 10: "))
            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                continue
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print("Correct!")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    guess_number()

import random

secret_number = random.randint(1, 100)

for i in range(1, 8):

    guessed_number = int(input("Guess a number between 1 and 100: "))
    if guessed_number < 1 or guessed_number > 100:
        print("Please enter a number between 1 and 100.")
    elif guessed_number < secret_number:
        print("Your guessing number is low")
    elif guessed_number > secret_number:
        print("Your guessing number is high")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {i} tries.")
        break

if guessed_number != secret_number:
    print(f"Sorry, you didn't guess the number. The secret number was {secret_number}.")
else:
    print("Game Over")
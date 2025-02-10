import random

random_number = random.randint(1, 50)

print("I'm thinking of a number between 1 and 50.")

for guess in range (1,6):
    guess_input = int(input("What is your guess: "))

    if guess_input < random_number:
        print(f"Your guess is too low.")
    elif guess_input > random_number:
        print(f"Your guess is too high.")
    else:
        print(f"You guessed the number.")
        break    

print(f"You are out of guesses. The number was {random_number}.")

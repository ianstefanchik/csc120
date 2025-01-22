import random

correct_answer = random.randint(0, 10)

print("I'm thinking of a number between 0 and 10.")
guess = int(input("What's your guess? "))

guess_difference = abs(guess - correct_answer)

if guess_difference == 0:
    print(F"You got it!\nI was thinking of {correct_answer}.")
elif guess_difference < 3:
    print(f"You were close!\nI was thinking of {correct_answer}.")
else:
    print(f"You were way off!\nI was thinking of {correct_answer}.")
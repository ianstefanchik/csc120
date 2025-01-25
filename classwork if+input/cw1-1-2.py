fruits_list = ['apple', 'banana', 'mango', 'strawberry', 'orange']

fruit_number = int(input('Which fruit do you want to know? '))

fruit_at_number = fruits_list[fruit_number]

print(f"The fruit at position {fruit_number} is {fruit_at_number}")

import random

fruit_list = ['banana', 'orange', 'apple', 'grape', 'cherry']

random_fruit = random.choice(fruit_list)

print(f"Your choices are {fruit_list}")

guess = input("What's your guess? ")

if guess == random_fruit:
    print(f"You got it, I was thinking of {random_fruit}.")
else:
    print(f"Sorry, I was thinking of {random_fruit}.")

import random

amount_of_numbers = int(input("How many numbers do you want to choose from? "))

if amount_of_numbers >= 20:
    print("This is going to be nearly impossible.")

elif amount_of_numbers >= 5:
    print("This is going to be somewhat difficult.")

else:
    print("This should be easy.")

print(f"I'm thinking of a number between 1 and {amount_of_numbers}")

random_number = random.randint(1,amount_of_numbers)

user_guess = int(input("What's your guess? "))
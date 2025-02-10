import random

my_list = random.sample(range(1,21), k=5)

print("I'm thinking of 5 random numbers between 1 and 20.")

guess = int(input(f"Can you guess any of them? "))

if guess in my_list:
    print(f"{guess} is in the list.")
    print(sorted(my_list))
else:
    print(f"Sorry, {guess} was not in my list!")
    print(sorted(my_list))

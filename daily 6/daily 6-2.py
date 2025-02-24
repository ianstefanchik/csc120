favorite_numbers = {
    'Avery': 711,
    'Duncan': 22,
    'Simon': 10,
    'Jeremy': 50,
    'Mayson': 100,
    }

user_input = input("Enter a name: ").title()

if user_input in favorite_numbers:
    print(f"{user_input}'s favorite number is {favorite_numbers[user_input]}.")
else: 
    print(f"I don't know what {user_input}'s favorite number is.")
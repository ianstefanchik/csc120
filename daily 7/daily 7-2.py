prices = { "skeeball": 3, "air hockey": 2, "pinball": 1, "batting cage": 15, "bumper cars": 9 }

prompt = "\nWhat is an activity you want to do at the arcade?"
prompt += "\nEnter quit to stop: "

total_costs = 0

while True:
    activity = input(prompt)

    if activity == 'quit':
        break
    elif activity in prices:
        total_costs += prices[activity]
    else: 
        print("That activity is not an option, please try again.")

print(f"The total cost is {total_costs} dollars.")
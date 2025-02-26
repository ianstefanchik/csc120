prompt = "\nWhat is a topping you want on a pizza?"
prompt += "\nEnter quit to stop: "

while True:
    pizza_topping = input(prompt)
    if pizza_topping != 'quit':
        print(f"I will add {pizza_topping} to your pizza.")
    else:
        break

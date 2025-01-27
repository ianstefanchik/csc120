fruits = []

for amount in range(5):
    fruit = input("Enter a fruit: ").strip().lower()
    fruits.append(fruit)

banana_count = fruits.count("banana")

print(f"You entered banana {banana_count} times.")

#a
names = ["joe", "john", "michael", "peter", "eric"]

names_capitalized = [name.title() for name in names]

print(names_capitalized)

#b
cubed_integers = [number ** 3 for number in range(101)]

print(cubed_integers)

#c 
fruits = ["apple", "orange", "blackberry", "kiwi", "strawberry"]

sentences = [f"I am eating this {fruit}." for fruit in fruits]

print(sentences)
from pathlib import Path

fruits = []

for fruit in range(5):
    fruit_input = input("Enter a fruit: ")
    fruits.append(fruit_input)

single_string = "\n".join(fruits)

path = Path("fruit_log.txt")

path.write_text(single_string)

from pathlib import Path

path = Path('numbers.txt')
contents = path.read_text()

numbers = contents.splitlines()

amount_larger = 0

for number in numbers:

    list_one = number.split(',')
    list_two = number.split(',')

    if int(list_one[0]) > int(list_two[1]):
        amount_larger += 1

print(amount_larger)

numbers = [1.5, 2.3, 5.6, 6.99, 8.12]
total_numbers = 0

for number in numbers:
    print(round(number))
    total_numbers += round(number)

print(total_numbers)
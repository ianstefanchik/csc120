numbers = [int(input("Enter a number: ")) for i in range(6)]

first_three = sum(numbers[:3])

count_numbers = sum(1 for number in numbers[3:] if number > first_three)

print(f"There was {count_numbers} that were larger than the sum of the first three numbers.")

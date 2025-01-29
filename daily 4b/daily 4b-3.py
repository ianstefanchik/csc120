numbers = [int(input(f"Enter a number: ")) for i in range(6)]

largest_two_numbers = sorted(numbers, reverse=True)[:2]
smallest_two_numbers = sorted(numbers)[:2]

print(f"The twol argest numbers were {largest_two_numbers[0]} and {largest_two_numbers[1]}")
print(f"The two smallest numbers were {smallest_two_numbers[0]} and {smallest_two_numbers[1]}")

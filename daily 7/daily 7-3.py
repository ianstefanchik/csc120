from pathlib import Path

number = int(input("Enter a positive integer: "))

output_file = Path("output.txt")

steps = 0
results = [number]

while number != 1:
    if number % 2 == 0:
        number //= 2
    else:
        number = number * 3 + 1
    results.append(number)
    steps += 1

print(f"It took {steps} steps to complete.")

output_file.write_text("".join(str(results)))

# age = input("How old are you? ")
# print(f"Next year you will be {age + 1} years old.")

#error is that age is type str, when it should be type int
age = input("How old are you? ")
print(f"Next year you will be {int(age) + 1} years old.")
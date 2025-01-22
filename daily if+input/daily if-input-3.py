grade = int(input("What is your numerical course grade? "))

if 90 <= grade <= 100:
    letter_grade = "A"
elif 80 <= grade < 90:
    letter_grade = "B"
elif 70 <= grade < 80:
    letter_grade = "C"
elif 60 <= grade < 70:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"Your letter grade is {letter_grade}.")
systolic = int(input("Enter systolic pressure: "))
diastolic = int(input("Enter diastolic pressure: "))

if systolic > 180 or diastolic > 120:
    print("Your blood pressure is in hypertensive crisis.")
elif systolic > 140 or diastolic > 90:
    print("Your blood pressure is high (stage 2).")
elif systolic > 130 or diastolic > 80:
    print("Your blood pressure is high (stage 1).")
elif systolic > 120 and diastolic < 80:
    print("Your blood pressure is elevated.")
else:
    print("Your blood pressure is normal.")
    
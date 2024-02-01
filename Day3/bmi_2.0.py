weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

bmi = weight / (height / 100) ** 2
bmi = round(bmi, 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi} you are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi} you are normal")
elif bmi < 30:
    print(f"Your bmi is {bmi} You are slightly overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi} you are overweight")
else:
    print(f"Your bmi is {bmi} you are obese")
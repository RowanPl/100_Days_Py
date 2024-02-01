weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

bmi = weight / (height / 100) ** 2
print(f"Your bmi is: {round(bmi, 2)}")

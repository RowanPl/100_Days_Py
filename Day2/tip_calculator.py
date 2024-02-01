print("Welcome to the tip calculator")
bill = float(input("What was the total bill in EURO? €"))
people = int(input("How many people to split the bill? \n"))
total = bill / people
print("Each person should pay:")

print(f'if you tip 15% : € {"{:.2f}".format(round(total * 1.15, 2))}')
print(f'if you tip 12% : €{"{:.2f}".format(round(total * 1.12, 2))}')
print(f'if you tip 10% : €{"{:.2f}".format(round(total * 1.10, 2))}')
print(f'if you tip 5% : €{"{:.2f}".format(round(total * 1.05, 2))}')
print(f'if you tip nothing : €{"{:.2f}".format(round(total, 2))}')

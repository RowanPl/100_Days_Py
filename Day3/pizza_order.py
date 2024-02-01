print("Welcome to the Python Pizza Order Calculator")
size = input("What size pizza would you like to order? S, M or L ").capitalize()
add_pepperoni = input("Would you like extra pepperoni? Y, N ").capitalize()
extra_cheese = input("Would you like extra cheese? Y, N ").capitalize()

bill = 0
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill} for an {size} pizza.")
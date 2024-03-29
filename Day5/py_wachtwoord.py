import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','@', '#', '$', '%', '^', '&', '(', ')', '*', '+', '_', '-', '=']

print("Welkom bij de Py_wachtwoord generator!")
nr_letters = int(input("Hoeveel letters wil je in je wachtwoord?\n"))
nr_symbols = int(input("Hoeveel symbolen wil je in je wachtwoord?\n"))
nr_numbers = int(input("Hoeveel nummers wil je in je wachtwoord??\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for i in range(0, nr_letters):
    password += random.choice(letters)
for i in range(0, nr_symbols):
    password += random.choice(symbols)
for i in range(0, nr_numbers):
    password += random.choice(numbers)
print(password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
for i in range(0, nr_letters):
    password_list.append(random.choice(letters))
for i in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for i in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
print("shuffled password: ")
print("".join(password_list))

# Ultra Hard Level -

number = 14
password_list_hard = []
all_characters = letters + numbers + symbols
for i in range(0, number):
    password_list_hard.append(random.choice(all_characters))

print( "ultra password" , ("".join(password_list_hard)))

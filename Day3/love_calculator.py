print("Welcome to the Love Calculator!")
name1 = input("What is your name?")
name2 = input("What is their name?")
combine_name = name1 + name2
combine_name = combine_name.lower()

t = combine_name.count("t")
r = combine_name.count("r")
u = combine_name.count("u")
e = combine_name.count("e")
first_digits = t + r + u + e


l = combine_name.count("l")
o = combine_name.count("o")
v = combine_name.count("v")
e = combine_name.count("e")
second_digits = o + l + v + e

total = int(str(first_digits) + str(second_digits))
print("Calculating! : Please wait....")
if total < 10 or total > 90:
    print(f"Your score is {total} you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total} you are alright")
else:
    print(f"Your score is {total}")
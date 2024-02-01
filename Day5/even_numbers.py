target = int(input("Which number do you want to check? "))

total = 0
if target > 1000:
    print("Please enter a number less than 1000.")
else:
    # One way to do it
    for number in range(1, target + 1):
        if number % 2 == 0:
            total += number
    print(total)

    # Similar way to do it, showing that the range can be used to skip numbers
    stotal = 0
    for number in range(2, target + 1, 2):
        stotal += number
    print(stotal)

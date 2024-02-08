def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}



def calculator():
    active = True
    num1 = float(input("Whats your first number? "))
    for operation_symbol in operations:
        print(operation_symbol)
    operation = input("What operation would you like to use ")
    num2 = float(input("Whats your second number? "))


    calculation = (operations[operation](num1, num2))
    print(f"{num1} {operation} {num2} = {calculation}")

    while active:

        user_input = input("Would you like to continue with this calculation? Type 'y' to continue or 'n' to exit ")
        if user_input == "y":
            operation =input("What operation would you like to use? ")
            num3 = float(input("Whats your next number?"))
            answer = calculation
            calculation = (operations[operation](calculation, num3))
            print(f"{answer} {operation} {num3} = {calculation}")
        else:
            active = False
            calculator()

calculator()





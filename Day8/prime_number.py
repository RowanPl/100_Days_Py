n = int(input('Enter a number: '))


def is_prime(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime == True:
        print(number, 'is a prime number')
    else:
        print(number, 'is not a prime number')

is_prime(n)
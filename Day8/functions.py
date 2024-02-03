import math

test_h = int(input("Enter the height of the wall"))
test_w = int(input("Enter the width of the wall"))

coverage = 5


def calculate_area(test_h, test_w, cover):
    num_cans = (test_h * test_w) / cover
    cans = round(math.ceil(num_cans))
    print(f"You need {cans} cans of paint")


calculate_area(test_h, test_w, cover=coverage)

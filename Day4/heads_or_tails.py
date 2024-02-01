import random

random_int = random.randint(1, 10)
head_tails = "Heads"
if random_int >= 5:
    head_tails = "Tails"


heads_or_Tail = input("Guess Heads or Tails")
if heads_or_Tail == "Heads" and heads_or_Tail == "Heads":
    print("Heads")
    print("You win!")
else:


import random

random_int = random.randint(1, 10)
head_tails = "Heads"
if random_int >= 5:
    head_tails = "Tails"

heads_or_tail = input("Guess Heads or Tails: ").lower().capitalize()

if heads_or_tail == "Heads" and head_tails == "Heads":
    print("Heads")
    print("You win!")
elif heads_or_tail == "Tails" and head_tails == "Tails":
    print("Tails")
    print("You win")
else:
    print("You lose")
    print(f"It was {head_tails}")

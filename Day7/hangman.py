import random

word_list = ["python", "ruby", "javascript", "java", "springboot"]

end_of_game = False

word = random.choice(word_list)
win = False
lives = 10
# print(word)

display = []
for _ in range(len(word)):
    display.append("_")


while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            display[position] = letter
        else:
            lives -= 1

    print(display)

    if "_" not in display:
        end_of_game = True

print("You Win")

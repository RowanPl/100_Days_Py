import random
import hangman_acii
import hangman_words

stages = hangman_acii.stages
logo = hangman_acii.logo
end_of_game = False
win = False
lives = 6
word = random.choice(hangman_words.word_list)
display = []
guessed_letters = []

print(logo)

for _ in range(len(word)):
    display.append("_")


def check():
    if "_" not in display:
        print("You win")
        return True
    if lives == 0:
        print("You lose")
        print("the word was: " + word)
        return True


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)
    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            display[position] = letter

    if guess not in word:
        print(guess + " was not in the word.")
        lives = lives - 1
        print(stages[lives])

    print(display)
    end_of_game = check()

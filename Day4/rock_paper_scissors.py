import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def rps():
    game_images = [rock, paper, scissors]

    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    print("You chose:")
    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")
    else:
        print(game_images[user_choice])

        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(game_images[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print("You win!")
        elif user_choice == 2 and computer_choice == 1:
            print("You win!")
        elif user_choice == 1 and computer_choice == 0:
            print("You win!")
        elif user_choice == computer_choice:
            print("It's a draw!")
        else:
            print("You lose!")

    # play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    # if play_again == "y":
    #     rps()
    # else:
    #     print("Goodbye!")
    #     return

while __name__ == "__main__":
    rps()

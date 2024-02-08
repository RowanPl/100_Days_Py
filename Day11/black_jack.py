import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calc_total(array):
    total = sum(array)
    return total


def check_for_ace(array):
    total = calc_total(array)
    if total > 21 and 11 in array:
        array.remove(11)
        array.append(1)
    return calc_total(array)


def blackjack():
    while True:
        player_hand = []
        computer_hand = []
        player_hand.append(deal_card())
        player_hand.append(deal_card())
        computer_hand.append(deal_card())
        computer_hand.append(deal_card())

        print("------- Dealer's Card -------")
        print(computer_hand[0])
        player_total = calc_total(player_hand)

        print("------- Your Hand -------")
        print(player_hand)
        print(player_total)

        while player_total <= 21:
            user_input = input("Would you like another card? Type 'y' for another card, type 'n' to stop: ")
            if user_input == 'y':
                player_hand.append(deal_card())
                player_total = check_for_ace(player_hand)
                player_total = calc_total(player_hand)
                print(player_hand)
                print(player_total)
            else:
                break

        dealer_total = check_for_ace(computer_hand)

        if dealer_total <= 17:
            computer_hand.append(deal_card())
            dealer_total = check_for_ace(computer_hand)

        if player_total > 21:
            print("Bust! You lose")
        elif player_total == dealer_total:
            print("Draw!")
        elif player_total == 21:
            print("Blackjack! You win")
        elif dealer_total > 21 or player_total > dealer_total:
            print("You Win")
            print(f"{computer_hand} = {dealer_total} is less then {player_hand} = {player_total}")
        else:
            print("Dealer Wins")
            print(f"{player_hand} = {player_total} is less then {computer_hand} = {dealer_total}")

        play_again = input("Would you like to play again? (y/n): ")
        if play_again.lower() != 'y':
            print("Thanks for playing!")
            break


blackjack()

import b_a_art

print(b_a_art.logo)
blind_auction = {}
using = True


def bid():
    name = input("What is your name? \n")
    price = int(input("What is the amount your willing to bid\n€"))
    blind_auction[name] = price


bid()
while using:

    more = input("Are there more people who want to bid? \n")

    if more == "yes":
        bid()

    else:
        highest_name = ""
        highest_price = 0
        for person in blind_auction:
            if int(blind_auction[person]) > highest_price:
                highest_price = blind_auction[person]
                highest_name = person

        print(f"The highest price is €{highest_price} and the name is {highest_name}")
        using = False

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_right = input("Would you like to go Left or Right")
if left_right == "right":
    print("You fell into a hole, Sad you died.")
else:
    print("You came by a lake")
    swim_wait = input("Would you like to 'swim' or 'wait'")
    if swim_wait == "swim":
        print("You swam, sadly a trout liked your toes and it killed you")
    else:
        print("You didn't swim and the boat came, You got on an island there are 3 doors")
        door = input("Which door would you like to, Red, Yellow, Blue")
        if door == "red":
            print("Behind the door there was a flame, you died")
        elif door == "yellow":
            print("Behind the door there was the treasure, you won")
        elif door == "blue":
            print("Behind the door was a beast, it killed you...")
        else:
            print("You didn't open an door, you didnt swim, you didnt went right what the hell are you doing...")

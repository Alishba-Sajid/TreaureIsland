print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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

way = input("Which way will you choose to go? L or R?")
if way =="L":
    print("You have selected right door")
    swim_wait = input("Do you want to wait or swim?")
    if swim_wait == "Wait":
        print("You are now on a boat safe and sound!")
        door = input("Which door you want to go?"
                     "Blue , Red , Yellow?")
        if door == "Blue":
            print("Eaten by Beast :( Game Over!")
        elif door == "Yellow":
            print("Woohoo! You win")
        elif door == "Red":
            print("Burned By Fire! Game Over!")
        else:
            print("Select the valid choice")

    elif swim_wait == "Swim":
        print("Opps!You are dinner for crocodiles")
    else:
        print("Please select the right choice")
elif way == "R":
    print("You Fell into a hole:( Game is over!")
else:
    print("Invalid Choice")

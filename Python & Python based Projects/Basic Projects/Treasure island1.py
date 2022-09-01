print('\n'
      '*******************************************************************************\n'
      '          |                   |                  |                     |\n'
      ' _________|________________.=""_;=.______________|_____________________|_______\n'
      '|                   |  ,-"_,=""     `"=.|                  |\n'
      '|___________________|__"=._o`"-._        `"=.______________|___________________\n'
      '          |                `"=._o`"=._      _`"=._                     |\n'
      ' _________|_____________________:=._o "=._."_.-="\'"=.__________________|_______\n'
      '|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |\n'
      '|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". \'__|___________________\n'
      '          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |\n'
      ' _________|___________| ;`-.o`"=._; ." ` \'`."\` . "-._ /_______________|_______\n'
      '|                   | |o;    `"-.o`"=._``  \'` " ,__.--o;   |\n'
      '|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________\n'
      '____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____\n'
      '/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_\n'
      '____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____\n'
      '/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_\n'
      '____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____\n'
      '/______/______/______/______/______/______/______/______/______/______/_____ /\n'
      '*******************************************************************************\n')
print("WELCOME TO TREASURE ISLAND\n Your mission is to find the treasure!")
direction = str(input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower())
if direction == "right" :
    print ("Game over! go to hell.")
elif direction == "left" :
    print('Good choice!')
    travel = str(input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat.'
                       ' Type "swim" to swim across. \n').lower())
    if travel == "swim":
        print("Game over! How does the shark saliva smell to you?")
    elif travel == "wait":
        print("good choice, patience is the key!")
        door = str(input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower())
        if door == "red":
            print("Damn bruh!! seriously? It's a room full of fire. Game Over. #BurntIntoAshes")
        elif door == "blue":
            print("Damn bruh!! seriously? Game over! who have ran into a room full of snakes. My deep consolences to you , Have fun in hell! ")
        elif door == "yellow":
            print("Well done buddy, you found the treasure! you win!")
        else:
            print('check your spelling monkey!')






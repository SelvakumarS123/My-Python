# the while loop
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# for hurdles in range(6):
#     jump()

number_of_hurdles = 6  # or             while number_of_hurdles > 0 and number_of_hurdles < 6  :
while number_of_hurdles > 0:  # this us used if number of hurdles is determined by the user
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)

while not at_goal():       # which is          while at_goal == False
    jump()


# while at_goal() != True:
#    jump()

# THE ROCK PAPER SCISSOR GAME
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
ROCK
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
PAPER
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
SCISSOR
'''

user = int(input("type 1 for rock , 2 for paper and 3 for scissors:\n"))
if user == "1":
    print(f"You chose: {rock}")
elif user == "2":
    print(f"You chose: {paper}")
elif user == "3":
    print(f"You chose: {scissors}")


import random
computers_list = [1, 2, 3]
computers_list[0] = rock
computers_list[1] = paper
computers_list[2] = scissors
random_number = random.choice(computers_list)
print(f"The computer chose: {random_number}")

if user > 3 or user < 1:
    print("you have chosen an invalid number, you lose!")

elif user == "1" and random_number == computers_list[0]:
    print("you drew")

elif user == "1" and random_number == computers_list[1]:
    print("you lose")

elif user == "1" and random_number == computers_list[2]:
    print("you win")

elif user == "2" and random_number == computers_list[0]:
    print("you win")

elif user == "2" and random_number == computers_list[1]:
    print("you drew")

elif user == "2" and random_number == computers_list[2]:
    print("you lose")

elif user == "3" and random_number == computers_list[0]:
    print("you lose")

elif user == "3" and random_number == computers_list[1]:
    print("you win")

elif user == "1" and random_number == computers_list[2]:
    print("you lose")

elif user == "3" and random_number == computers_list[0]:
    print("you drew")




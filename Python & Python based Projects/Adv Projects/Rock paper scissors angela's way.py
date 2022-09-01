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

game_images = [rock, paper, scissors]
user = int(input("type 0 for rock , 1 for paper and 2 for scissors:\n"))
if user > 2 or user < 0:
    print("you have chosen an invalid number, you lose!")
else:
    print(f"you chose: {game_images[user]}")
    import random

    computer = random.randint(0, 2)
    print(f"the computer chose: {game_images[computer]}")

    if user == 0 and computer == 2:
        print("you win!")
    elif user == 2 and computer == 0:
        print("you lose!")
    elif user > computer:
        print("you win!")
    elif user < computer:
        print("you lose! ")
    elif user == computer:
        print("you drew")

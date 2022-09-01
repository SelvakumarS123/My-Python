import random

word_list = ["ardvark", "baboon", "camel"]
guess = str(input("Guess a letter\n>>").lower())
chosen_word = random.choice(word_list)
for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")

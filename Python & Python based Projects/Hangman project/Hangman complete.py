from hangman_arts import logo, stagesA
print(f" {logo} \n                 Good luck!😈           \n")
print("             Welcome to HANG_AN\n       you have 6 chances to save your life.\n       ")

import random
from hangman_words import word_list
end_of_game = False
lives = 6
chosen_word = random.choice(word_list)
dash_list = []
for char in chosen_word:  # here, char is the corresponding letter
    dash_list.append("-")
    # dash_list += "-"
print(dash_list)
while not end_of_game:
    guess = str(input("Guess a letter\n>>").lower())
    if guess in dash_list:
        print(f"you have already guessed this letter {guess}, please try guessing a different letter")
    for position in range(len(chosen_word)):  # here, position is the index of the corresponding letter,
        letter = chosen_word[position]  # (that is the speciality of range() function)
        if guess == letter:
            dash_list[position] = letter
            # dash_list[position] = guess
    print(dash_list)
    if guess not in chosen_word:
        print(f"your guess {guess},is not in the word. you lose a life")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            print(f"you're hanged to death!\nThe word is {chosen_word.upper()}")
            end_of_game = True
            print("you lose!")
    if "-" not in dash_list:
        end_of_game = True
        print("you win!")


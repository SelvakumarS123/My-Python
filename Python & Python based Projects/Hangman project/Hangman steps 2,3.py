import random

word_list = ["ardvark", "baboon", "camel"]
# guess = str(input("Guess a letter\n>>").lower())
chosen_word = random.choice(word_list)
dash_list = []
for char in chosen_word:  # here, char is the corresponding letter
    dash_list.append("-")
    # dash_list += "-"
print(dash_list)

while "-" in dash_list:
    guess = str(input("Guess a letter\n>>").lower())
    for position in range(len(chosen_word)):  # here, position is the index of the corresponding letter,
        letter = chosen_word[position]  # (that is the speciality of range() function)
        if guess == letter:
            dash_list[position] = letter
            # dash_list[position] = guess
    print(dash_list)
print("you win!")
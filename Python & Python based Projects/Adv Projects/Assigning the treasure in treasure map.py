print("WELCOME TO THE TREASURE MAP")
row1 = [" 🥲 ", " 🥲 ", " 🥲 "]
row2 = [" 🥲 ", " 🥲 ", " 🥲 "]
row3 = [" 🥲 ", " 🥲 ", " 🥲 "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = (input("where do you wanna put the treasure?:\n"))  # basically this input is a string
row = int(position[0])      # 2
column = int(position[1])   # 3
# selected_row = map[row - 1]
# selected_row[column - 1] = " X "
map[row - 1][column - 1] = " X "
print(f"{row1}\n{row2}\n{row3}")

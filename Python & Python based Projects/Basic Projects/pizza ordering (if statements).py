# pizza order program
size = input("size?(s ,m ,or l)\n ")
add_pepperoni = input("do you want extra pepperoni?(y or n)\n ")
add_cheese = input("do you want extra cheese?(y or n)\n ")
bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
else:
    bill += 25

if add_pepperoni == "y":
    if size == "s":
        bill += 2  # use nested if function if you want to check two probabilities
    else:
        bill += 3

if add_cheese == "y":
    bill += 1

print(f"please pay ${bill}")

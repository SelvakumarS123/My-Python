
# solving  the ticket crisis
height = int(input("what is your height(cm):  "))
bill = 0
if height >= 120:
    print("you can ride the roller coaster!")
    age = int(input("what is your age: "))
    if age <= 12:  # this is a nested if statement
        bill = 5
        print("child tickets are $5")

    elif age <= 18:
        bill = 7
        print("youth tickets are $7")
    else:
        bill = 12
        print(" Adult tickets are $12")
    pic = (input("do you need a picture?(y or n)\n") )
    if pic == "y":
        bill += 3
    print(f" please pay ${bill}")
else:
    print("sorry! you have to grow taller before you can ride ")
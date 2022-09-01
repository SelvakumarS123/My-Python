# logical operators
# and --> if both conditions are true, it will return true ( returns false if any one or both conditions are false)
# or --> returns true if at least one condition is true ( returns false only if both the conditions are false)
# not --> reverses a condition

# a = 5
# b = 12
# and_operator = a > 4 and b > 10
# or_operator = a > 6 or b > 13
# not_operator = not a > 2
# print(and_operator, "\n", or_operator, "\n", not_operator)

# solving  the  new ticket crisis for mid life people using logical operators
height = int(input("what is your height(cm):  "))
bill = 0
if height >= 120:
    print("you can ride the roller coaster!")
    age = int(input("what is your age: "))
    if 45 <= age <= 55:  # mid life people get to ride for free
        bill = 0
        print(f" mid life tickets are ${bill}")
    elif age <= 12:  # this is a nested if statement
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
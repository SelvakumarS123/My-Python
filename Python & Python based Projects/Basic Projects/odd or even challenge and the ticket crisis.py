# # odd or even exercise
# print("welcome to odd or even calculator")
# number = int(input("tpe in the number you want to check: "))
# if number % 2 == 0:
#     print(f"{number} is an even number")
# else:
#     print(f"{number} is an odd number")


# solving  the ticket crisis
height = int(input("what is your height(cm):  "))
if height >= 120:
    print("you can ride the roller coaster!")
    age = int(input("what is your age: "))
    if age <= 12:  # this is a nested if statement
        print("please pay $5")
    elif age <= 15:  # this condition will only be checked if the previous condition(if statement) is false
        #  so this condition is for the age group 12 to 15.
        print("please pay $6")
    elif age <= 18:
        print("you should pay $7")
    else:
        print("please pay $12")

else:
    print("sorry! you have to grow taller before you can ride ")

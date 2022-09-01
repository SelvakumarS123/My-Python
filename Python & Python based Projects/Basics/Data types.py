# subscripting
# str , int , bool , float etc --> datatypes
print("hello"[4])
print(123 + 345)
# num_char = len(input("name? "))
# print("your name has " + num_char + "characters")

# we cant add a string to an integer(num_char) .
# len function will not return a string, it will always return only an integer
# we can check the type of data using the following (type) function
# print(type(num_char))


# so the correct method is

# num_char = len(input("name? "))
# # type conversion:
# new_num_char = str(num_char) # this converts numchar(integer) into newnumchar(string)
# print(type(new_num_char))
# print("your name has " + new_num_char + " characters")
# print(int(70) + float(100.5))
# print(str(70) + str(100.5))

# challenge

num = int(input("enter a 2 digit number "))   # num = str(input("enter a 2 digit number "))
new_num = str(num)
new_num1 = new_num[0]
new_num2 = new_num[1]
result = (int(new_num1) + int(new_num2))
print(result)




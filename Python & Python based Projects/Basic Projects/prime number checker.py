
#
# def prime_checker(number):
#     for num in range(2, number - 1):
#         if number % num != 0:
#             print(f"{number} is a prime")
#
#         else:
#             print(f"{number} is not a prime")


def prime_checker(number):
    is_prime = True
    for num in range(2, number - 1):
        if number % num == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is a prime")
    else:
        print(f"{number} is not a prime")


n = 1
while 6 > n:
    number = int(input("check the number:\n"))
    prime_checker(number)
    n += 1

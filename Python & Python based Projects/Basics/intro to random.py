import random
import my_modules

print(random.randint(1, 100))  # includes 1 and 100
print(random.random())  # this returns a random floating point number between 0.0 to 1.0 ( upto 0.999999, THIS WILL NOT INCLUDE 1)
print(my_modules.pi)

# the coin toss program
head_tail = random.randint(1, 2)
if head_tail == 1:
    print("heads")
else:
    print("tails")

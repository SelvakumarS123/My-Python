for number in range(1, 10):  # by default the range function will step through all the numbers from the start to end,
    # and it will increase by 1. if you wanted to increase by any other number
    # then you have to specify how  large you want the steps to be
    print(number)  # this will not print 10
for number in range(0, 11, 3):
    print(number)

# how to add up all the numbers from 1 to 100 using for loop
sum_total = 0
for number in range(1, 101):
    sum_total += number
    print(sum_total)

print(50*101)  # carl gauss's trick that stunned his teacher

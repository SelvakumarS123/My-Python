# adding evens exercise
sum_of_evens = 0
for number in range(2, 101, 2):  # if you put 1 in place of the starting value which is set to 2 now,
    # it will give you the sum of all odd numbers
    sum_of_evens += number
print(sum_of_evens)

total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)



# average height exercise
heights = input("Type in the list of student heights:\n").split()
for n in range(0, len(heights)):
    heights[n] = int(heights[n])  # this removes the single quotes meant for strings ['1', '2', '3', '4']
# print(heights)
# print(type(n))
i = 0
total_height = 0
# for i in range(i, len(heights), 1):
#     # i = i + 1
#     total_height += heights[i]
for height in heights:
    total_height += height
print(total_height)
# for loop will run as for as many times there are items inside the list
num_heights = 0
for height in heights:
    num_heights += 1                                              # average = sum of items / number of items
average_height = total_height / num_heights
# average_height = total_height / len(heights)
print(f"the average height is: {average_height}")


# this program is just for understanding the for loops ,
# in real world you can just use the sum(heights) function and the len(heights) function

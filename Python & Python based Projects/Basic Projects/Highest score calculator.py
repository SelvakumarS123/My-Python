# THE HIGHEST SCORE CHALLENGE
marks = input("Type in the list of student marks:\n").split()
marks.sort()
for m in range(0, len(marks)):
    marks[m] = int(marks[m])
i = 0
highest_mark = 0
for mark in marks:
    if mark > highest_mark:   # initially the highest_mark is set to 0
        highest_mark = mark

print(marks)
print(f"the highest mark is {highest_mark}")


# print(max(marks))
# print(min(marks))

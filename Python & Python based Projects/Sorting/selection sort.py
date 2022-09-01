print("selection sort")
a = [10, 14, 27, 33, 35, 19, 42, 44]

for i in range(len(a)):

    initial_index = i
    for j in range(i+1, len(a)):
        if a[initial_index] > a[j]:
            initial_index = j
    a[i], a[initial_index] = a[initial_index], a[i]
    print(a)
print('\n')
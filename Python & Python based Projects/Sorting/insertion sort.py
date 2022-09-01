print("inserion sort")
a = [3, 7, 5, 6, 9]

for i in range(1, len(a)):
    m = a[i]
    initial_index = i-1
    while initial_index >= 0 and a[initial_index] > m:
        a[initial_index + 1] = a[initial_index]
        initial_index -= 1
    a[initial_index + 1] = m
    print(a)
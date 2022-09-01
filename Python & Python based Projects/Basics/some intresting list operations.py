from typing import List

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a[0] = 100
print(a)
a[1:3] = [100, 100, 100]
print(a)
a[0:3] = []
print(a)
a[0:0] = [-2, -1, 0]
print(a)
# alising
b = a[:]
print(b)
print(a is b)
a[3] = 66
print(a)
print(b)
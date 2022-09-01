print("odd no")
till = int(input("enter a num: "))
total = []
for i in range(till + 1):
    if i % 2 != 0:
        total.append(i)
        print(i)
print(len(total))

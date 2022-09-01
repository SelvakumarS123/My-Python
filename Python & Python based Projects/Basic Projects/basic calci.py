print('''Choose any one choice
1-Addition
2-Subtraction
3-Multiplication
4-Division
5-Equals''')
i = 1
a = float(input("Enter a number:"))
b = int(input("Operation:"))
c = float(input("Enter a number:"))
while(i):
    if(b==1):
        a = a+c
        b = int(input("Operation:"))
        if(b<5):
            c = int(input("Enter a number:"))
        else:
            print(a)
            i = 0
    elif(b==2):
        a = a-c
        b = int(input("Operation:"))
        if(b<5):
            c = int(input("Enter a number:"))
        else:
            print(a)
            i = 0
    elif(b==3):
        a = a*c
        b = int(input("Operation:"))
        if(b<5):
            c = int(input("Enter a number:"))
        else:
            print(a)
            i = 0
    elif(b==4):
        a = a/c
        b = int(input("Operation:"))
        if(b<5):
            c = int(input("Enter a number:"))
        else:
            print(a)
            i = 0
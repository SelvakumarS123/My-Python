def circulate(list,n):
    for i in range(2,n+1):
        c=list[i:]+list[:i]
        print("the circulated value:",i, "=",c)
        return


list=[3,6,5,9,10,7]
n=int(input(">> "))
circulate(list,n)

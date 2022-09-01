myVar = "Podu inniki maja tha"
print(myVar.split("i"))
print(myVar[-1])
print(myVar[3:9]) #excludes 9
fn="jose"
ln="portilla"
print(f"hello {fn} {ln}")
myList=[10,20,90,40,30,60,80,70]
myList.append(70)
print(myList)
myList.insert(1,myVar)
print(myList)
myList.pop()
print(myList)
myList.pop(1)
print(myList)
myList.sort()
print(myList)
myList.reverse()
print(myList)
employees = {"chef":"Amy","ceo":"jose"}
print(employees["ceo"])
employees["waiter"]="Mike"
print(employees)
employees["chef"]="jose"
employees["ceo"]=employees["waiter"]
employees["waiter"]="amy"
print(employees["ceo"].capitalize())
stock = {"google":[200,300,400],"gme":[300,200,100]}
history=stock["google"]
print(stock["google"])
print(history[2])
mydict={"outer":{"inner":100}}
print(mydict["outer"])
outer=mydict["outer"]
print(outer["inner"])
print(mydict["outer"]["inner"])
print(employees.keys())
print(employees.values())
print(employees.items())#tuple_formation #tuples are immutable
#Booleans will be our building blocks for logic and control flow(true or false)
myTuple=(1,2,3)
print(myTuple[0])
#control_flow
print(1<2)
print(fn==ln)
print(1>2 or 2==2)
pw="pablo escobar"
stored_pw="pablo emilio escobar gaviria"
admin=True
if pw == stored_pw:
    print("match")
elif admin:
    print("admin grant")
    admin=False
else:
    print("no match")

for st in stock:
    print(stock[st][0])

for out in mydict:
    print(mydict[out])
    print(mydict[out]["inner"])
    oute = mydict[out]
    for inn in oute:
        print(oute[inn])
        print(f"Value of inner is {mydict[out][inn]}")

for position in employees:
    print(f"the {position} is held by {employees[position]}")

#tuple_unpacking
newlist=[]
newlist.append(employees.items())
print(newlist)

oldlist=[('a','b'),('c','d'),('e','f'),(1,2)]

for item1,item2 in oldlist: # for item1,item2 in oldlist
    print(item2)


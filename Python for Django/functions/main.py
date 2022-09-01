def sayHello(first_name,last_name):
    return f"Hello {first_name} {last_name}"

print(sayHello(first_name="jose",last_name="portilla"))

def checker(number):
    if(number>=100):
        return ">=100"
    else:
        return "!>=100"
print(checker(101))

def list_checker(listtocheck):
    for num in listtocheck:
        if num == 10:
            return True
    return False
list=[1,2,3,4,5,10]

print(list_checker(list))

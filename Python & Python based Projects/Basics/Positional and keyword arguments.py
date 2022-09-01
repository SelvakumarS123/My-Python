# TODO
# POSITIONAL ARGUMENTS
def greet_with(name,location):
    print(f"Hello, {name}")
    print(f"Welcome to {location}.")


name = str(input("Enter ur name:>\n "))
location = str(input("Where are you?\n "))
greet_with(name,location)

greet_with(location="london", name="Tamil" )
# KEYWORD ARGUMENTS
def key(a,b,c):
    print(a)
    print(b)
    print(c)
key(c=1,b=3,a=5)
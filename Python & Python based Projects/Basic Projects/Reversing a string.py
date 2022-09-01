
# write a python code To display elements of list in reverse order

def myfunc(a):
    rev_str = []
    for x in a:
        rev_str.insert(0, x)
    return rev_str
print(myfunc([10,2,100,740,8500,89,1902,788]))
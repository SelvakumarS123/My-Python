try:
    print("10" + 10) #TypeError
#except TypeError:
    #print("wrong data types")
except IOError:
    print("did u check the file permissions")
except:
    print("hey u got an error")
else:
    print("no error")

#no exception run else
try:
    print(10 + 1) #TypeError
#except TypeError:
    #print("wrong data types")
except IOError:
    print("did u check the file permissions")
except:
    print("hey u got an error")
else:
    print("no error")

#exception found still run else

try:
    print("10" + 10) #visit a url(modify database)
except TypeError:
    print("wrong data types") #report back to the user
except IOError:
    print("did u check the file permissions") #report back to the user
except:
    print("hey u got an error") #report back to the user
finally:
    print("thank youuuuuuu") #take them to another page(refresh)
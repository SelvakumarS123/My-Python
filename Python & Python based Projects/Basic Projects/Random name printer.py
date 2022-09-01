# print a random name in a list
# import random
# names = input("type down your names, separated by a comma:\n")
# namelist = names.split(",")
# number_of_names = int(len(namelist))
# random_name = random.randint(0, number_of_names - 1)  # because len gives the total number of items in a list ,
# # in which index of the last item is always 1 less than the total number of items. if the total number of items is 5 ,
# # then the index of the last item will be 4
# print(namelist[random_name])


# or simply use the choice function
import random
names = input("type down your names, separated by a comma:\n")
namelist = names.split(",")
person_who_will_pay_the_bill = random.choice(namelist)
print(person_who_will_pay_the_bill)




# welcome to tip calcualtor
total = int(input("enter the total amount($): "))
percent = int(input("what percentage of bill you want to give as tip: "))
num_of_persons = int(input("how many persons you want t share this bill with?: "))
# percentage = percent/100
# percent_total = percentage * total
# new_total = percent_total + total
# new_shared_total = new_total / num_of_persons

new_shared_total = (total * percent / 100 + total) / num_of_persons
# we have to round this amount to two decimal places
# new_new_shared_total = round(new_shared_total, 2) --> this doesn't work because this is a formatting problem
# rather than a mathematical problem
new_new_shared_total = "{:.2f}".format(new_shared_total)  # this coverts new_shared_total(which is a float) to a string
# and the string is displayed in this particular format(2f)
print(f"each person should pay {new_new_shared_total} $")

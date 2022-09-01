# love calculator
name = str(input("Enter your name:\n ").lower())
crush_name = str(input("Enter your crush's name:\n ").lower())
merged_name = crush_name + name
t = merged_name.count("t")
r = merged_name.count("r")
u = merged_name.count("u")
e = merged_name.count("e")

merged_true = t + r + u + e

l = merged_name.count("l")
o = merged_name.count("o")
v = merged_name.count("v")
e = merged_name.count("e")

merged_love = l + o + v + e

# print(f" your true love value is {merged_true}{merged_love}%")
love_score = int(str(merged_true) + str(merged_love))
# if 10 > love_score > 90:
if (love_score < 10) and (love_score > 90):
     print(f"your true love value is {love_score}%, you go together like coke and mentos.")
# elif 40 <= love_score <= 50:
elif (love_score >= 40 ) and (love_score <= 50):
    print(f" your true love value is {love_score}%, you are alright together.")
else:
    print(f" your true love value is {love_score}%!")
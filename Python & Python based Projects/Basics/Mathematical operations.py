# PEMDAS
# P--> parenthesis
# E--> exponent
# M--> multiplication <==> (same priority) # D--> division
# A--> addition <==> # S-->
print(3 * 3 + 3 / 3 - 3)  # calculation goes from left to right
print(3 * (3 + 3) / 3 - 3)

weight = input("enter weight(kg): ")
height = input("enter height(m): ")
BMI = int(weight) / float(height) ** 2  # now wew ant to print our bmi as a whole number
# BMI_as_int = int(BMI)
# print(BMI_as_int)
print(round(BMI))

# rounding a float number to a number with specified number of decimal places
print(round(8/3, 2))     # where 2 is the number of decimal places we should round it(float) to.
print(type(8 / 3))
print(type(8 // 3))
print(type(8 % 3))
score = 0
score += 1
print("score: ", score)
#f strings

print(f"YOUR SCORE IS {score}")



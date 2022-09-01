# Newtons method  to find the square root of a number
a = float(input("Enter the number:\n>>"))
x = float(input("Estimation:\n>>"))
final = (0.5 * (x + (a / x)))
new_x = (0.5 * (final + (a / final)))
print(f" The root of ur number is: {new_x}")




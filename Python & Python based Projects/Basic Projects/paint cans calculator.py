# TODO
# let's paint the wall today
# one can of paint can cover 5 square meters of the wall.
import math


def paint_cans(height, width, cover):
    no_of_cans = math.ceil((height * width) / cover)
    # we have round up the number
    print(f"you need {no_of_cans} cans of paint to paint this wall ")


cover = int(input("Area covered per can?\n"))
ht = int(input("Enter height in meters:\n"))
wt = int(input("Enter width in meters:\n"))
paint_cans(height=ht, width=wt)

# # return value
# import math
# def paint_cans(height, width, cover):
#     no_of_cans = math.ceil((height * width) / cover)
#     return no_of_cans
#
#
# hey = paint_cans(2,4,5)
# hii = hey/2
# print(hii)

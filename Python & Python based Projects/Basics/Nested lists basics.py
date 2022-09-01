solar_system = ["Mercury", "Venus", "earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
num_planets = len(solar_system)
print(solar_system[7])
#  print(solar_system[num_planets])  # --> this gives you IndexError: list index out of range#
print(solar_system[num_planets - 1])

# nested lists
fruits_vegies = ["strawberries", "banana", "mangoes", "apples", "oranges", "potatoes", "spinach", "kale", "tomatoes",
                 "celery"]
fruits = ["strawberries", "banana", "mangoes", "apples", "oranges"]
vegies = ["potatoes", "spinach", "kale", "tomatoes", "celery"]
fruits_and_vegetables = [fruits, vegies]  # this nests the lists
print(fruits_and_vegetables)

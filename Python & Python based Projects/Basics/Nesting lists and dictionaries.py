# Nesting lists and dictionaries

# syntax

nesting = {
    "key": [list],
    "key2": {dict},
}
travel_log = {"US": ["MIT", "Stanford", "Washington DC", "Las Vegas", ], "number_of_visits": [6, 5, 4], "USA": {
    "cities_visited": ["MIT", "Stanford", "Washington DC", "Las Vegas", ],
    "number_of_visits": [6, 5, 4],
}, "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "number_of_visits": [6, 5, 4]
}, "Earth": [{
    "Australia": 6, "Antartica": 4,
    "Atlantis": 2
},
    {
        "India": 1, "Indonesia": 9, "Iran": 0
    },
    {
        "This is a": " dictionary nested in a list "
    }, ], "Australia": {"cities_visited": ["sydney", "melbourne"], "no_of_visits": [2, 2]}}

travel_log["Earth"].append({"HELLO": "EVERYONE"})

print(travel_log)


# # Nesting dictionaries in a list
# Earth = [{
#     "Australia": 6, "Antartica": 4,
#     "Atlantis": 2
# },
#     {
#         "India": 1, "Indonesia": 9, "Iran": 0
#     },
#     {
#         "This is a": " dictionary nested in a list "
#     }]
#
countries = [{
    "Australia": 6, "Antartica": 4, "Atlantis": 2,
    "number_of_visits": [6, 4, 2],
    "total_visits": 12
}, {
    "India": 1, "Indonesia": 9, "Iran": 0,
    "number_of_visits": [1, 9, 0],
    "total_visits": 10
}, {"Singapore": 1, "Serbia": 0, "number_of_visits": [1, 0], "total_visits": 1}]
print(countries)

travel_log2 = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(country_visited, number_of_visits, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = number_of_visits
    new_country["cities"] = cities_visited
    travel_log2.append(new_country)



add_new_country("Russia",2,["Moscow", 'saint petersburg'])
print(travel_log2)


# travel_log = {
#     # Nesting list in a dictionary
#
#     "US": ["MIT", "Stanford", "Washington DC", "Las Vegas", ],
#     "number_of_visits": [6, 5, 4],
#
#     # Nesting dictionary in a dictionary
#
#     "USA": {
#             "cities_visited": ["MIT", "Stanford", "Washington DC", "Las Vegas", ],
#             "number_of_visits": [6, 5, 4],
#     },
#     "France": {
#             "cities_visited": ["Paris", "Lille", "Dijon"],
#             "number_of_visits": [6, 5, 4]
#     },
#
#     # Nesting dictionary in a list
#
#     "Earth": [{
#         "Australia": 6, "Antartica": 4,
#         "Atlantis": 2
#     },
#         {
#             "India": 1, "Indonesia": 9, "Iran": 0
#         },
#         {
#             "This is a": " dictionary nested in a list "
#         },]
#
# }
#
# travel_log["Australia"] = {"cities_visited": ["sydney", "melbourne"], "no_of_visits": [2,2]}
# travel_log["Earth"].append({"HELLO": "EVERYONE"})
#
# print(travel_log)
#
#
#
#

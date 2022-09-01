# python lists --> stores grouped pieces of data (data structure)
# order is important
solar_system = ["Mercury", "Venus", "earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(solar_system[3])
print(solar_system[-1])
solar_system[2] = "Earth"
print(solar_system)

solar_system.append("Pluto")
# solar_system.append(["Pluto", "la la land"])
print(solar_system)
solar_system.extend(["Pandora", "la la land", "Tomorrowland"])
print(solar_system)
solar_system.insert(3, "Andromeda")
print(solar_system)
solar_system.remove("Earth")
print(solar_system)


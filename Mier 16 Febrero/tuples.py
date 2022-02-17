# Tuplas agrupacion de items, y las tuplas son inmutables

car = ("Ford", "Tesla", "Vwosvagen", 2320)
print(car)
 # car[0] = "BMW" -> son inmutables

arolienas_string = ("Avianca")
print(type(arolienas_string))
arolienas = ("Avianca",)
print(type(arolienas))



nueva = (2,4, [2,4])
nueva[-1][1] = [100]
print(nueva)


hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")

awesome_team = hero1 + hero2
print(awesome_team)

awesome = (hero1, hero2)
print(awesome)

cities = ("London", "Paris", "Los Angeles", "Tokyo")
print(cities.index("Tokyo"))

print("London" in cities)
#  cuando necesito que sea rapido
num_list = []

#append
num_list.append(1)
num_list.append(2)
num_list.append(3)
num_list.append([23,23])
print(num_list)

#insert
num_list.insert(3,4)
print(num_list)
num_list.insert(1, "hola")
num_list.insert(1, "hola")
print(num_list)
# modifcar
num_list[0] = "Cambiado"
print(num_list)

# pop()
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
last_house = houses.pop()
print(last_house)
print(houses)

# remove
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", "Hufflepuff"]
houses.remove("Hufflepuff")
print(houses)

# List Slicing
num_list = [1,2,3,4,5,6,7,8]
print(num_list[2:5])

# index
cities = [ "london", "Paris", "Los Angeles", "Beirut"]
print(cities.index("london"))

print("london" in cities)
print("bucaramanga" in cities)
print("Queretaro" not in cities)


lista_num = [55,2,53,89,1054,232,453,723,13,53,1]
lista_num.sort()
lista_num.sort(reverse=True)
print(lista_num)
lista_num.pop(3)
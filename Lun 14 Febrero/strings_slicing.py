# Slicing -> Al proceso de obtener una porcion (substring) de un string usando sus indices
# string[start:end]
my_string = "This is MY string!"
print(my_string[0:4]) # Desde el inicio hasta antes del indice 4
print(my_string[1:7])
print(my_string[8:len(my_string)])

# string[start:end:step]
print(my_string[0:7:2])
print(my_string[0:7:5])

# Reverse Slicing
print(my_string[13:2:-1])


# PArtial Slincin
# Tanto start como end son opcionales
print(my_string[:8])
print(my_string[8:])
print(my_string[:])

anita = "anita lava la tina"
print(anita[::-1])
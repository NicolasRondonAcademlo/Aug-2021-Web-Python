# Capitalize


message  = "paga tu factura de la luz"
message = message.capitalize()
print(message)  # Paga tu factura de la luz

# Upper
message = message.upper()
print(message)

# Casefold -> Super Agresivo [Convetir si o si todo a minuscula]
message = message.casefold()
print(message)
message = message.upper()
print(message)

# lower [Puede llegar el caso que no te convierta todo en minuscual] -> Ruso, 
message = message.lower()
print(message)

# Center
message = "Banana"
message = message.center(20) #
print(message)
message = "Banana"
message = message.center(11, 'i') # El primero son cantidad de caracteres string, el segundo cracter con que se llena
print(message)

# endswit
txt = "Hello, welcome to my world."
txt = txt.endswith(".")
print(txt)

# startwith
txt = "Hello, welcome to my world."
print(txt.startswith("h"))

# find
x = txt.find("welcome")
print(x)

# is lowe
texto = "este e sun texto en minuscula"
print(texto.islower())

# is upper
texto = "TODO EN MAYUS"
print(texto.isupper())

txt = "Hello, welcome to my world."
z = "welcome" in txt

# title
txt = txt.title()
print(txt)


# zfill
txt = "Fact-1"
txt = txt.zfill(10)
print(txt)

# replace

txt = "Hello, welcome to my world."
txt = txt.replace("Hello", "Hola")
print(txt)

txt =  "Hello, welcome to my world. Hello Friend"
txt = txt.replace("Hello", "Hola",1)
print(txt)

# split

txt =  "Hello, welcome  my world. Hello Friend"
txt = txt.split(",")
print(txt)

# count

txt =  "Hello, welcome to my world. Hello Friend"
txt = txt.count("Hello")
print(txt)

# join
txt =  "Hello, welcome  my world. Hello Friend"
txt = txt.split(",")
print(txt)
txt = ",".join(txt)
print(txt)

# https://www.w3schools.com/python/python_ref_string.asp


Final = """
It was a special pleasure to see things eaten, to see things blackened and changed. 
with the brass nozzle in his fists, with this great python spitting 
its venomous kerosene upon the world, the blood pounded in his head,
and his hands were the hands of some amazing conductor playing all
the symphonies of blazing and burning to bring down the tatters
and charcoal ruins of history. - Fahrenheit 451
"""

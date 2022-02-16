# Comparasion
# Concatenacion
# Search

# Comparacion
print("a"< "b") # Unicode Value -> Cada caracter tiene asignado un numero

house = "Gryffindor"
house_copy = "Gryffindor"

print(house == house_copy)

new_house = "Slytherin"

print(new_house <= house)
# Concatenacion
first_half = "Bat"
second_half = "Man"

ful_name = first_half + second_half
print(ful_name)
hola = "Hola"
print(hola*4)

# 
# 1 % -> 2.6 python
# 2 .format() -> < 3.6
# 3. f strings -> 3.6 > Cuando el string no depende de un input dle usuario
# 4. Templates -> 3.6 > Cuando el string depende del input de un usuario | 


name = "Nicolas"
last_name = "Rondon"

sentence = "{} {}  es el profesor de python".format(
    name, last_name
)
sentence = "{0} {1}  es el profesor de python".format(
    name, last_name
)
print(sentence)


pensionarte = 64
edad = 27

sentence = f"Faltan  {64-27} años para pensionarte"
print(sentence)

from string import Template

template = Template('$name  is the $job of $company')

string = template.substitute(
    name="Raju Kumar",
    job ="TCE",
    company="GOOGLE"
)
print(string)

string = template.safe_substitute(
    name="Raju Kumar",
    job ="TCE",

)


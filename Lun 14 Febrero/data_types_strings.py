# String -> Coleccion de caracteres que estan dentro de comillas, simples, dobles, triples

texto_1 = 'Commilas simples'
texto_2 = "Comillas dobles"
texto_3 = """Comillas Triples"""
texto_4 = '''Comilals simples tripes'''
print(texto_1)
print(texto_2)
print(texto_3)
print(texto_4)

long_text = "Hola este es un texto muy largo"
len_text = len(long_text)
print(len_text)

print("-----")
batman = "Bruce Wayne"
print(batman[0])
print(batman[5])
print(batman[-1])

last = batman[len(batman) -1]
print(last)

batman = "Soy yo"
print(batman)
print(batman[0])
#batman[0] = "H" -> Los items en una cadena de caracteres son inmutables
#print(batman)

"sisetma que nos va decir si las lllaves estan balanceadas o no"
 # [[[]]] -> True  ---- [[[]] -> False --- ][ -> false ]]]]

brackets = "[[]][][]" # Listas, Tuples, Strings, Iterados customizados
check = 0
for  bracket in brackets:
    if bracket == "[":
        check += 1
    
    elif bracket == "]":
        check -= 1

    if check < 0:
        break

print(check == 0)

# Funciones, Manejo De Errores, Modulo (Import), Manejo Archivos

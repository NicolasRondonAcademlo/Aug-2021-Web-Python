# Errores 
# Exceptions - Syntax Errores
from modulos.funciones import variable
# print(0/0)) -> Esto es un error de sintaxis
 
#print(0/0) -> Exception Error ZeroDivisionError:

#x = 10
#if x > 5:
#    raise Exception(f"The number should no exceed 5 the value of x was {x}")

try:
    print(0/0)
except:
    print("Por si falla")


print(".........")
a = 545
b = 10
try:
    a/b
except TypeError as e:
    print("Asegurate que todo lo que se ingrese sea  numero")
except ZeroDivisionError as e:
    print("Asegurate que no estas dividiendo por 0")
else:
    print("Aqui")
finally:
    print("Esto siempre se ejecuta")



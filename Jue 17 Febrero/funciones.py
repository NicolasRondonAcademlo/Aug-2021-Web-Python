# Funciones

num1 = 1
num2 = 40

if num1< num2:
    minimun = num1
else:
    minimun = num2

print(minimun)

num1 = 450
num2 = 40

if num1< num2:
    minimun = num1
else:
    minimun = num2
print(minimun)

minimun = min(10,40) # None
print(minimun)
minimun = min(1,232,424,545)
print(minimun)
print(min([232,54,65]))
# Built -in -> Ya existen
# User-defined users

# def function name (parameters)
##### Instructions set to perform

def my_print_function():
    print("This")
    print("is")
    print("A")
    print("Function")

my_print_function()


def minimun(first, second):
    if first < second:
        print(first)
    else:
        print(second)

num = 1 
num = 2
minimun(2,1)

num1 = 100
num2 = 2323
minimun(num2,num1)
minimun(
    first=num1,
    second=num2
)
#minimun(1)
result = minimun(1032,123)
print(result)

def minimun(first, second):
    if first < second:
        print(first)
    else:
        print(second)

    return
result = minimun(1032,123)
print(result)

def minimun(first, second):
    if first < second:
        return first
    return second

result = minimun(1032,123)
print(result)
print("-------")
def func():
    name = "Stack"
    return name

name = func()
print(name)

num = 20

def multiply_by_10(n):
    n*=10
    num = n

    z = 0
    print("Value of nume inside function: ", num)
    return n


multiply_by_10(num)
print("Value of num outside function: ", num)
print("######")

num_list = [10,20,30,40]
print(num_list)

def multiply_by_10(my_list=[23,43,44]):
    my_list[0] *= 10
    my_list[1] *= 10
    my_list[2] *= 10
    my_list[3] *= 10

num_list =multiply_by_10(num_list)
print(num_list)

# type hints

def saludar(name, message):
    return f"Hola, {name} {message}"

print(saludar(23, 443))
from typing import Optional, List

#def saludar(name:str, message:Optional[List]) -> str:
#    return f"Hola, {name} {message}"

#def saludar(name:str, message:List[List[tuple]]]) -> str:
#    return f"Hola, {name} {message}"


def multiply(a:int, b:int) -> int:
    """
    Params:
        a: int -> Numero uno a multiplicar
        b: int -> Numero dos a multiplicar
    Returns:
        c: int -> Resultado
    """
    c = a *b 
    #return a*b
    return c

multiply()

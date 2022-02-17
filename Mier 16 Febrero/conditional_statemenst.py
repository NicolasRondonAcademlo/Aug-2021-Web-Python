# Condicionales
# 
# if
#if else
# if elif else

# if -> condicion -Z> Code to be executed

num = 5

if num == 5:
    print("The number is equal to 5")

if num > 5:
    print("The number is greater than 5")


num = 12

if num % 2 == 0 and num %3 == 0 and num % 4 == 0:
    print("The number is a multiple of 2,3,4")

if num % 5 == 0 or num%6 == 0:
    print("The number is a multiple of 5 and/or 6")


num = 63

if num >= 0 and num <= 100:
    print("----")
    if num >= 50 and num <=75:
        print("----")
        if num >=60 and num <=70:
            print("the number is in the 60-70 range")

num = 10
if num > 5:
    num = 20
    new_num = num*5

print(num)
print(new_num)
print("##########")

# if else
num = 60

if num <= 50:
    print("The numbers es menor o igual a 50")
else:
    print("El numero es mas grande que 50")

num = 60

output = "El numero es mas pequeno que 50" if num <= 50 else "El numero es mas grande que 50"
print(output)

# if elif else

light = "Red"

if light == "Green":
    print("Go")

elif light == "Yellow":
    print("Caution")

elif light == "Red":
    print("Stop")
    
elif light == "Red":
    print("Stop 2")
else:
    print("WTF clon el semaforo")
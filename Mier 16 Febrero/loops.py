# lopps estructura de control que ejecuta isntrucciones un numero determinado de vecese
# for loop, while lopp
# For -> iterador, secunciea, instrucciones
# string, lista, tuple, range, 

for i in range(1,11):
    if i % 2 == 0:
        print(i, " is even")
    else:
        print(i, " is")


lista = [1,3,4,5,5]
for i in lista:
    print(i)


jose_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}

print("----")
for i in  jose_dict:
    print(jose_dict[i])


cars = ["bmw", "audi", "tesla"]
for car in cars:
    print(car)

print("#####")
float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
count_greater = 0

for  num in float_list:
    if num>10:
        count_greater +=1

print(count_greater)
print("*****")

for i, num in enumerate(float_list):
    print(i, num)

print("pppp")

n = 50
num_list = [10, 4, 23, 6, 18, 27, 47]

#for n1 in num_list:
#    print(n1, "primera")
#    for n2 in num_list:
#        print(n2, "segunda")
#        if n1 +n2 == n:
#           print(n1, n2)


for num in num_list:
    print(num, "a")
    if num == 4:
        break

# [ expresion for lopp if condition]
nums = [10, 20, 30, 40, 50]

nums_doble = [n*2 for n in nums]
print(nums_doble)

nums_doble_30 = [n*2 for n in nums if n <= 30]
print(nums_doble_30)

#while
# condition sea verdadera

n = 2
power= 0
val = n
while val < 1000:
    power += 1
    val *=n
    print(val, '.....')
    #break
print(power)

lista = []
for i in [1,2,3]:
    if i >1:
        lista.append(i)
print(lista)
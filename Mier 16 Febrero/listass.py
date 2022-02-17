frutas = ["manzana", "pera", "granadilla"]
frutas_valor = ["manzana", 34, True, "pera"]

print(frutas[0])
print(frutas[-1])
print(len(frutas))

frutas[0] = "Coco"
print(frutas)

frutas_valor[1] += 3
frutas_valor[1] = frutas_valor[1] + 3


num_seq = range(0,10)
print(num_seq)
num_list = list(num_seq)
print(num_list)

#a = str(int(4.5))

num_list = list(range(3,21,3))
print(num_list)

world_cup_winners = [
    [2006, "Italy"],
    [2010, "Spain"],
    [2014, "Germany"]

]
print(world_cup_winners)

germany =  world_cup_winners[-1][-1]
print(germany)

spain = world_cup_winners[1][1]


part_a = [1,2,3,4,5]
part_b = [6,7,8,9,10]
full_part = part_a + part_b
print(full_part)

part_a = [1,2,3,4,5]
part_b = [6,7,8,9,10]
part_a.extend(part_b)
z = part_a
print(z)
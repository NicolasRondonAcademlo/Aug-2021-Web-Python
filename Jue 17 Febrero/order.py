from collections import OrderedDict
d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}

new_d = OrderedDict(sorted(d.items()))
print (new_d)
for key  in new_d:
    print(key, new_d[key])
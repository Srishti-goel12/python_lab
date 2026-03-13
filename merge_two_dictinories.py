d1 = {"a":1, "b":2}
d2 = {"c":3, "d":4}

for k,v in d2.items():
    d1[k] = v

print(d1)

#Output

{'a': 1, 'b': 2, 'c': 3, 'd': 4}
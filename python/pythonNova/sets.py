# Los sets son otro tipo de estructuras de datos. Se diferencian de listas, diccionarios y tuplas porque son una coleccion mutable de elementos inmutables
# no ordenados ni repetidos

# los sets los podemos declarar de la siguiente manera

# set(1, 2, 3, 4, 5, 6)

# {1, 2, 3, 4, 5, 6}

# set([1, 2, 3, 4, 5, 6])

mi_set = set([1, 2, 3, 4, 5, 6, (1, 2, 3)])
print(type(mi_set))
print(mi_set)

otro_set = {1, 2, 3}
print(type(otro_set))
print(otro_set)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)

s1 = {1, 2, 3}
s1.add(4)
print(s1)

s1 = {1, 2, 3}
s1.remove(3)
print(s1)

s1 = {1, 2, 3}
s1.discard(7)
print(s1)


s1 = {1, 2, 3}
s1.pop()
print(s1)

s1 = {1, 2, 3}
s1.clear()
print(s1)

mi_set_a = {1, 2, "tres"}
mi_set_b = {3, "tres"}
mi_set_c = mi_set

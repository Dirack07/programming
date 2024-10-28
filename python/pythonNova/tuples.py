# Los tuples o tuplas, son estructuras de datos que almacenan multiples elementos en una unica variable

# Se caracterizan por ser ordenadas e inmutables (Ocupan menos espacio y se procesan mas rapido)

# Son parecidos a las listas pero son inmutables y no se pueden modificar

mi_tuple = (1, "dos", [3.33, "cuatro"], (5.0, 6))
print(mi_tuple)
print(type(mi_tuple))
print(mi_tuple[3][0])

# Castig conversion de tipos de datos
lista1 = list(mi_tuple)
print(lista1)

# Unpacking

mi_tuple = (1, 2, 3, 4)
print(mi_tuple)

mi_tuple = (1, 2, 3, 4)
print(mi_tuple[0])

mi_tuple = (1, 2, (10, 20), 4)
print(mi_tuple[2])

mi_tuple = (1, 2, (10, 20), 4)
print(mi_tuple[2][0])

t = (1, 2, 3, 1)
print(t.count(1))

t = (1, 2, 3, 1)
print(t.index(2))

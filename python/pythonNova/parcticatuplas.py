# Utiliza un metodo de tuplas para contar la conatidad de veces que aparece el valor 2 en la siguiente tupla

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

# Convierte a la lista la siguinete tupla y almacenala en una variable llamada mi_lista

mi_tupla = (1, 2, 3, 3, 2, 1, 1, 3, 2)
mi_lista = list(mi_tupla)
print(mi_lista)
print(type(mi_lista))

# Extrae los elementos de la siguiente tupla en cuatro variables a,b,c,d

mi_tupla = (1, 2, 3, 4)
a = mi_tupla[0]
b = mi_tupla[1]
c = mi_tupla[2]
d = mi_tupla[3]

print(a)
print(b)
print(c)
print(d)

mi_tupla = (1, 2, 3, 4)

# Forma mas sencilla
a, b, c, d = (mi_tupla)
print(a)
print(b)
print(c)
print(d)

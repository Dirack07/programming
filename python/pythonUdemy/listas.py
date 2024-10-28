nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']

print(nombres)

print(nombres[0])
print(nombres[1])
print(nombres[-1])
print(nombres[-3])

print(nombres[0:2])

for nombre in nombres:
    print(nombre)
else:
    print("No existen mas nombres en la lista!")

# preguntar el largo de una lista
print(len(nombres))
# agregar un nuevo elemento a la lista
nombres.append('Lorenzo')
# insertar un elemento en un indice especifico
nombres.insert(1, 'Octavio')
print(nombres)

# remover un elemento en especifico
# nombres.remove('Karla')
# print(nombres)

# remover el ultimo valor agregado
# nombres.pop()
# print(nombres)

# remover un elemento en un indice
# del nombres[0]
# print(nombres)

# limpiar la lista
# nombres.clear()
# print(nombres)

# borrar la lista por completo
# del nombres
# print(nombres)

temp = [30.5, 19.8, 12.3, 31.0, 19.9, 34.4, 25.3]
print(temp)
# for i in range(len(temp)):
#     print(temp[i])

for i in temp:
    print(i)

temp.append(18.3)
temp.insert(5, 12.3)

print(temp)


lista = ['Alicia', 1998, 'Bob', 1990, 'Carlos', 1986, 'David', 2001]
for i in range(0, len(lista), 2):
    nombre = lista[i]
    nacimiento = str(lista[i+1])
    print(nombre, nacimiento)

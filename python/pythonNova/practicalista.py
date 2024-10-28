mi_lista = ["a", "b", "c"]
print(type(mi_lista))

mi_lista = ["a", "b", "c"]
otra_lista = ["hola", 55, 6, 1]

mi_lista = ["a", "b", "c"]
print(len(mi_lista))

mi_lista = ["a", "b", "c"]
resultado = mi_lista[0]
print(resultado)

mi_lista = ["a", "b", "c"]
resultado = mi_lista[0:1]
print(resultado)

mi_lista = ["a", "b", "c"]
resultado = mi_lista[0:2]
print(resultado)

mi_lista = ["a", "b", "c"]
mi_lista2 = ["d", "e", "f"]
print(mi_lista)
print(mi_lista2)

mi_lista = ["a", "b", "c"]
mi_lista2 = ["d", "e", "f"]
mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)

mi_lista = ["a", "b", "c"]
mi_lista2 = ["d", "e", "f"]
mi_lista3 = mi_lista + mi_lista2
mi_lista3[0] = "alfa"
print(mi_lista3)

mi_lista = ["a", "b", "c"]
mi_lista2 = ["d", "e", "f"]
mi_lista3 = mi_lista + mi_lista2
mi_lista3.append("g")
print(mi_lista3)

mi_lista = ["a", "b", "c"]
mi_lista2 = ["d", "e", "f"]
mi_lista3 = mi_lista + mi_lista2
mi_lista3.pop()
print(mi_lista3)

lista = ["g", "o", "b", "m", "x"]
lista.sort()
print(lista)

lista = ["g", "o", "b", "m", "x"]
lista.sort()
lista.reverse()
print(lista)

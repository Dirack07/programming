# Son tipo de datos mutables y pueden ser asignados a una variable

# Se escriben entre corchetes y se separan por comas

# Se pueden hacer listas anidadas

lista_1 = ["C", "C++", "Python", "Java"]
lista_2 = ["PHP", "SQL", "Visual Basic"]

# Indexado: podemos acceder a los elementos de una lista a traves de sus inidices [inicio:fin:paso]

print(lista_1[1:3])

# Cantidad de elementos a traves de la propiedad len
print(len(lista_1))

# Concatenacion: sumamos los elementos de varias liostas con el simbolo +
print(lista_1 + lista_2)


lista_1 = ["C", "C++", "Python", "Java"]
lista_2 = ["PHP", "SQL", "Visual Basic"]
lista_3 = ["d", "a", "c", "b", "e"]
lista_4 = [5, 4, 7, 1, 9]

# Funcion append: Agregar un elemento a una lista en el lugar

lista_1.append("R")
print(lista_1)

# Funcion pop(): elimina Elimina un elemento de la lista dado el indice y devuelve el valor quitado

print(lista_1.pop(4))

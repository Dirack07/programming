# Definir una tupla
frutas = ("Naranja", "Platano", "Guayaba")

# Tamanio de una tupla
print(len(frutas))
print(type(frutas))
# acceder a un elemento
print(frutas[0])

# Navegacion inversa
print(frutas[-1])

# Acceder a un rango
print(frutas[0:2])

perros = ('Pastor',)
print(perros)
print(type(perros))

# Recorrer elementos

for fruta in frutas:
    print(fruta, end=' ')
print("")
# cambiar el valor de una tupla
frutasLista = list(frutas)
frutasLista[0] = 'Pera'
frutas = tuple(frutasLista)
print(frutas)

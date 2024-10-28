# Realizar un codigo que pida al usuario que ingrese una frase. Convertir la frase en una lista de palabras

# Ordenar la lista alfabeticamente y despues vamos a imprimir la lista

frase = input("Ingresa una frase: ")
frase = frase.split()
frase.sort()
print(frase)

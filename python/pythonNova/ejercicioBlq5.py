# Crear un codigo que pida al usuario que ingrese una frase y convierta todas las letras a mayusculas
# Despues convierta la frase en una lista de palabras

frase = input("Ingresa una frase: ")
frase_mayusculas = frase.upper()
lista_palabras = frase_mayusculas.split()

print(lista_palabras)
print(type(lista_palabras))

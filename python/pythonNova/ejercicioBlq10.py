# Crea un codigo que pida al usuario una palabra, almacena cada letra como elemento de una tupla
# Imprime las ultimas tres letras de la palabra

palabra = input("Ingresa una palabra: ")
mi_tupla = tuple(palabra)
print(mi_tupla[-3:])

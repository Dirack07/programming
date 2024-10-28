# Crear un codigo que pida al usaurio que ingrese una oracion

# extrae las primaeras 5 letrras de la oracion y conviertelas en una tupla e imprime la tupla

oracion = input("Ingresa una oracion: ")
letras = tuple(oracion[0:6])
print(letras)
print(type(letras))

# Crear una tupla con los numeros del 1 al 10 y solicitar que el usuairo ingrese un numero. Verificar si el nunmero esta en la tupla

mi_tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
numero = int(input("Ingresa un numero para verificar si esta en la tupla: "))
resultado = numero in mi_tupla
print(f"El numero esta en la tupla?: {resultado}")

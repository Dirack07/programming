# 1. Escribe un programa que le pida su nombre al usuario y como salida
# le diga cuantos caracteres tiene su nombre.
# test
nombre = input("Ingresa tu nombre: ")
if " " in nombre:
    nombre = nombre.replace(" ", "")
numero_caracteres = len(nombre)
print(f"Tu nombre tiene {numero_caracteres} caracteres")

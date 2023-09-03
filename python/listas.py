numbers = [10, 5, 7, 2, 1]
print("El contenido de la lista: ", numbers)

numbers[0] = 111
print("Nuevo contenido de la lista: ", numbers)

numbers[1] = numbers[4]
print("Nuevo contenido de la lista: ", numbers)

print("Longitud de la lista: ", len(numbers))

del numbers[1]
print(len(numbers))
print(numbers)
print(numbers[-4])

hat_list = [1, 2, 3, 4, 5]

print("Reemplazar el numero de en medio con un numero ingresado por el usuario")
numero = int(input("Ingresa un numero: "))
tamanio_lista = len(hat_list)
medio = tamanio_lista//2

hat_list[medio] = numero

print(hat_list)

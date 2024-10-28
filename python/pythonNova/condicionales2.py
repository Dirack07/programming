'''
Realizar un programa que al introducir dos numeros, si el primero es mayor que el segundo se sumen
en caso contrario se resten
'''

numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))

if numero1 > numero2:
    print("La suma de los numeros es: ", numero1 + numero2)

else:
    print("La resta de los numero es: ", numero1 - numero2)

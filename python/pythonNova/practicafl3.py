# Dada la siguiente lista de numeros realiza la suma de todos los numeros pares e impares por separado en las variables

# suma_pares y suma_impares
suma_pares = 0
suma_impares = 0
lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2,
                 6, 4, 8, 5, 9, 8, 5, 3, 4, 3, 5, 6, 4]

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

print(
    f"""
    La suma de los numeros pares = {suma_pares}
    La suma de los numeros impares = {suma_impares}
""")

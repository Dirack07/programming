# Crear un codigo que pida al usuario dos numeros conviertelos a enteros y muestra la suma, resta, multiplicacion y division de ambos

numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
if numero2 == 0:
    print("No se puede realizar la division entre 0")
else:
    division = numero1 / numero2

    print(f"""
    Resultado Suma = {suma}
    Resultado Resta = {resta}
    Resultado Multiplicacion = {multiplicacion}
    Resultado Division = {division}
""")

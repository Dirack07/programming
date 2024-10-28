continuar = "s"
contador = 0

while True:
    if continuar == "s" or continuar == "S":
        contador += 1
        print(f"Operacion: {contador}")
        numero1 = int(input("Ingresa el primer numero: "))
        numero2 = int(input("Ingresa el segundo numero: "))
        if numero1 > numero2:
            print(numero2, numero1)
        elif numero2 > numero1:
            print(numero1, numero2)
        else:
            print(f"Los numeros son iguales: {numero1} {numero2}")
    elif continuar == "n" or continuar == "N":
        print("Find el programa!!! Adios :)")
        break
    else:
        print("Ingresa una opcion valida!!! [s/n] ")
    print("=========================================================")
    continuar = input("Continuar? [s/n]: ")
    print("=========================================================")

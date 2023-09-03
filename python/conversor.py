def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " dolares")

menu = """
Bienvenido al conversor a tipo de monedas

1.-Pesos Mexicanos a Dolares
2.-Pesos Argentinos a Dolares
3.-Pesos Colombianos a Dolares

Elige una opcion: """

opcion = int(input(menu))

if opcion ==1:

    conversor("mexicanos", 20.11)

elif opcion ==2:
    
    conversor("argentinos", 151.55)

elif opcion ==3:
    
    conversor("colombianos", 4698.01)

else:
    print("Ingresa una opcion correcta")



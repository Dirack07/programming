
for i in range(1, 4, 1):
    print("""Las actividades que puede realizar la persona son:
          1. Dormir
          2. Sentarse 
          """)
    actividad = int(input("Ingrese actividad que realiza la persona: "))
    minutos = int(input("Ingrese minutos: "))
    if actividad == 1:
        calorias = 1.08 * minutos
        print("===========================================================")
        print(f"La persona ha consumido {calorias} en {minutos} minutos")
        print("===========================================================")
    elif actividad == 2:
        calorias = 1.66 * minutos
        print("===========================================================")
        print(f"La persona ha consumido {calorias} en {minutos} minutos")
        print("===========================================================")
    else:
        print("===========================================================")
        print("Actividad no registrada!!!")
        print("===========================================================")

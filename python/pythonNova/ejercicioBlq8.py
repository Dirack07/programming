# Crear un codigo que resulva el area del crculo dado el radio
# El usaurio tiene que ingresar el radio

pi = 3.1416
print("Calcular el area de un circulo")
radio = float(input("Ingresa el radio del circulo: "))
area = round(pi * radio * radio, 2)

print(f"El area del circulo es: {area}")

# Utilizando las variables num1 y num2 se alimentan con el input del usaurio
# Crear una estrcutura de control de flujo

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

if num1 > num2:
    print(f"El numero {num1} es mayor que el numero {num2}")
elif num1 < num2:
    print(f"El numero {num1} es menor que el numero {num2}")
else:
    print("Los numeros son iguales")

# Tu trabajas en una empresa donde los vendedores reciben comisiones del 13% por sus ventas totales
# Ayudes a los vendedores a calcular sus comisiones
# Les debe preguntar su nombre
# Cuanto han vendido este mes
# Responder con una frase que incluya su nombre y el monto que les corresponde por las comisiones

nombre = input("Ingresa tu nombre: ")
ventas_totales = float(
    input("Ingresa el monto de tus ventas totales de este mes: "))
comision = round(ventas_totales * 0.13, 2)
print(f"{nombre} tu comision por las ventas de este mes es: ${comision} pesos")

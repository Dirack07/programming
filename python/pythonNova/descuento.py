'''
En un almacen se hace el 20% de descuento a los clientes
cuya compra super los $1000
Cual sera la cantidad que pagara por su compra?
'''


cantidad = float(input("Ingrese la cantidad de la compra: "))

if cantidad >= 1000:
    descuento = cantidad * .20
    print('El total a pagar con el 20% de descuento es: ', cantidad - descuento)
else:
    descuento = cantidad * .02
    print("El total a pagar con el 2% de descuento es: ", cantidad - descuento)

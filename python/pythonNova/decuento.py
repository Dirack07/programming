'''
Una tienda ofrece un descuento del 15% sobre el total de 
la compra y un cliente desea saber cuanto debera
pagar finalmente por su compra

'''

nombre_cliente = input("Ingresa el nombre del cliente: ")
total = float(input("Introduce el total de la compra: $ "))
descuento = total * .15
precio_con_descuento = total - descuento

print('===========================================================================')
print('****** Ticket de compra ******')
print(f'Nombre del cliente: {nombre_cliente}')
print(f"Total de la compra: $ {total:.2f}")
print(f'Descuento 15%: $ {descuento:.2f}')
print(
    f'El total a pagar: $ {precio_con_descuento:.2f}')
print('===========================================================================')

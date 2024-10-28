'''

En un hospital existen tres reas: Ginecologa, Pediatra, Traumatologia. El presupuesto anual del hospital
se reparte conforme a la sig. tabla:

Area Porcentaje del presupuesto
Ginecologa 40%
Traumatologia 30%
Pediatra 30%
Obtener la cantidad de dinero que recibir cada Area, para cualquier monto presupuestal.

'''
monto_presupuestal = float(
    input("Ingresa el monto presupuestal para este anio: "))
presupuesto_ginecologia = monto_presupuestal * 0.4
presupuesto_traumatologia = monto_presupuestal * 0.3
presupuesto_pediatria = monto_presupuestal * 0.3

print(f'El monto presupuestal para Ginecologia es: {presupuesto_ginecologia}')
print(
    f'El monto presupuestal para Traumatologia es: {presupuesto_traumatologia}')
print(f'El monto presupuestal para Pediatria es: {presupuesto_pediatria}')

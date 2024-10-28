'''
Un hombre sesea saber cuanto dinero se genera por concepto de intereses sobre la contidad
que tiene en inversion en el banco.
El decidira reinvertir los intereses siempre y cuando excedan a $100, y en ese caso desea saber
cuanto dinero tendra finalmente en su cuenta.
'''

cantidad_inicial = float(input("Ingresa la cantidad de inversion inicial:"))
interes_banco = float(input("Ingrese el interes que da el banco: "))
intereses_generados = (cantidad_inicial * (interes_banco / 100)) / 360
print("Total de intereses generados en un dia= ", intereses_generados)

if intereses_generados > 100:
    print("Esta cantidad sera reinvertida: ", intereses_generados)
else:
    print("La cantidad no sera reinvertida, regresa a la cuenta general: ",
          intereses_generados)

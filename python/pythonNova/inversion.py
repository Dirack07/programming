'''
Un vendedor recibe un sueldo base mas un 10% extra por comisin de sus ventas, el vendedor desea saber
cuanto dinero obtendr por concepto de comisiones por las tres ventas que realiza en el mes y el total que
recibir en el mes tomando en cuenta su sueldo base y comisiones.

'''
'''
Para 5 empleados
'''
empleados = ['Juan', 'Pedro', 'Ana', 'Liz', 'Ara']


def sueldo_empleados(empleado):
    print("====================================================================")
    print(f"Ingrese la informacion del empleado {empleado}")
    sueldo_base = float(input("Ingrese el sueldo base del empleado: "))
    venta1 = (float(input("Ingrese la cantidad de la venta numero 1: ")))
    venta2 = (float(input("Ingrese la cantidad de la venta numero 2: ")))
    venta3 = (float(input("Ingrese la cantidad de la venta numero 3: ")))
    total_ventas = venta1 + venta2 + venta3
    ganancia_comision = (total_ventas * .01)

    print(f"Sueldo por comision: {ganancia_comision}")
    print("Sueldo total, suledo base + comision: ",
          sueldo_base + ganancia_comision)


for empleado in empleados:
    sueldo_empleados(empleado)

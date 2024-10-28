'''
En una escuela la colegiatura de los alumnos se determina según el numero de materias que cursan. El
costo de todas las materias es el mismo.
Se ha establecido un programa para estimular a los alumnos, el cual consiste en lo siguiente: si el promedio
obtenido por un alumno en el ultimo periodo es mayor o igual que 9, se le hará un descuento del 30 % sobre la
colegiatura y no se le cobrara IVA
si el promedio obtenido es menor que 9 deberá pagar la colegiatura
completa, la cual incluye el 10 % de IVA.
Obtener cuanto debe pagar un alumno.
'''

costo_materia = float(input("Ingresa el costo por materia: "))

materia_1 = float(input("Ingresa la calificacion de la primera materia: "))
materia_2 = float(input("Ingresa la calificacion de la segunda materia: "))
materia_3 = float(input("Ingresa la calificacion de la tercera materia: "))
materia_4 = float(input("Ingresa la calificacion de la cuarta materia: "))
materia_5 = float(input("Ingresa la calificacion de la quinta materia: "))

costo_colegiatura = (costo_materia * 5)

promedio = (materia_1 + materia_2 + materia_3 + materia_4 + materia_5) / 5
print(f"Promedio del alumno: {promedio:.2f}")

if promedio >= 9:
    descuento = (costo_colegiatura * .30)
    colegiatura_total = (costo_colegiatura - descuento)
    print(
        f"Pago por colegiatura con el 30% de descuento= ${colegiatura_total:.2f}")
else:
    colegiatura_total = (costo_colegiatura * 1.10)
    print(
        f"Pago por colegiatura sin descuento + IVA 10%= ${colegiatura_total:.2f}")

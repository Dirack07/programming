BEGIN{print "Reporte de fechas de ingreso de empleados"}
{
    texto = "Campo 1: " $1 ", Ultimo campo: " $NF
    print texto
}
END{print "Fin del reporte"}
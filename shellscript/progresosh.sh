#!/bin/sh

total=10

echo -n "Progreso: "

i=0
while [ $i -lt $total ]; do
    # Calcula el porcentaje actual
    percentage=$((i * 100 / total))

    # Imprime la barra de progreso
    printf "["
    j=0
    while [ $j -lt $percentage ]; do
        printf "="
        j=$((j + 1))
    done
    while [ $j -lt 100 ]; do
        printf " "
        j=$((j + 1))
    done
    printf "] $percentage%% \r"

    # Incrementa el contador
    i=$((i + 1))

    # Pausa durante 1 segundo
    sleep 1
done

echo # Nueva línea después de la barra de progreso completa
echo "Proceso completado."

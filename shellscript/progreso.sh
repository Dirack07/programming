#!/bin/bash

total=1800

echo -n "Progreso: "

for ((i = 1; i <= total; i++)); do
    # Calcula el porcentaje actual
    percentage=$((i * 100 / total))

    # Imprime la barra de progreso
    echo -ne "["
    for ((j = 1; j <= percentage; j++)); do
        echo -n "="
    done
    for ((j = percentage + 1; j <= 100; j++)); do
        echo -n " "
    done
    echo -ne "] $percentage% \r"

    # Pausa durante 1 segundo
    sleep 1
done

echo # Nueva línea después de la barra de progreso completa
echo "Proceso completado."

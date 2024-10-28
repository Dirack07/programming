#!/bin/sh

# Obtener la fecha en formato "Año-Mes-Día Hora:Minutos:Segundos"
formatted_date=$(date "+%Y-%m-%d %H:%M:%S")

# Convertir la fecha formateada a segundos desde la epoch usando awk
epoch_time=$(echo $formatted_date | awk '{
  split($1, date_parts, "-");
  split($2, time_parts, ":");
  printf "%d\n", mktime(date_parts[1] " " date_parts[2] " " date_parts[3] " " time_parts[1] " " time_parts[2] " " time_parts[3])
}')

echo "Epoch Time: $epoch_time"


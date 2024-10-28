#!/bin/bash

# # Definir la variable en el script de shell
# mi_variable="Hola desde Shell"

# # Exportar la variable como una variable de entorno
# export mi_variable

# # Ejecutar código Python desde el script y pasar la variable
# x=$(
#     python3 - <<END
# import os

# # Obtener el valor de la variable desde las variables de entorno
# mi_variable = os.environ.get('mi_variable', 'Valor predeterminado si no se proporciona')

# #mi_variable = "Variable de python"
# # Código Python aquí
# print(mi_variable)
# END
# )

# # Más código de shell aquí
# echo "Imprimiendo el valor de varibale desde shell: $x"

# Obtener la fecha en formato "Año-Mes-Día Hora:Minutos:Segundos"
# formatted_date="2020-11-25 12:34:56"
# minutos=10
# # Convertir la fecha formateada a segundos desde la epoch usando Python
# epoch_time=$(python3 -c "from datetime import datetime; print(int(datetime.strptime('$formatted_date', '%Y-%m-%d %H:%M:%S').timestamp()))")

# echo "Epoch Time: $epoch_time"

# segundos=`echo "$minutos * 60" | bc`
# echo $segundos
# resultado=`echo "$epoch_time + $segundos" | bc`
# echo "resultado $resultado"

# hora_final=$(python3 -c "from datetime import datetime; print(datetime.utcfromtimestamp($resultado).strftime('%Y-%m-%d %H:%M:%S'))")

# echo "Hora final: $hora_final"


# Obtener la fecha en formato "Año-Mes-Día Hora:Minutos:Segundos"
formatted_date=`date "+%Y-%m-%d %H:%M:%S"`
minutos=10

# Convertir la fecha formateada a segundos desde la epoch usando Python 2.7
epoch_time=$(python3 -c "from datetime import datetime; import time; print(int(time.mktime(datetime.strptime('$formatted_date', '%Y-%m-%d %H:%M:%S').timetuple())))")

segundos=`echo "$minutos * 60" | bc`
echo $segundos
resultado=`echo "$epoch_time + $segundos" | bc`
echo "resultado $resultado"

# Convertir el tiempo en epoch a una fecha y hora formateada usando Python 2.7 y strftime
hora_final=$(python3 -c "from datetime import datetime; print(datetime.fromtimestamp($resultado).strftime('%Y-%m-%d %H:%M:%S'))")

echo "Hora actual: $formatted_date"
echo "Epoch Time: $epoch_time"
echo "Hora final: $hora_final"
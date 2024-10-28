#!/bin/bash

awk '
BEGIN{
    FILENAME == archivo 
}
$0 ~ /ALERTA/ {
    print "La cadena es: $0"
}
'
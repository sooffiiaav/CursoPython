#Convertir de cadena a numero
from xmlrpc.client import boolean

numero_cadena='10'
numero_entero=int(numero_cadena)
print(numero_entero)

#Convertir de cadena a flotante
numero_cadena='3.14'
numero_flotante=float(numero_cadena)
print(numero_flotante)

#Convertir de numero a cadena
numero_entero=25
numero_cadena=str(numero_entero)
print(numero_cadena)

#Convertir a boolean
#Tipo booleano es falso en los siguientes casos:
#Si el valor es 0, cadena vacía,o None

#Tipo boolean es True si:
#El valor es distinto de 0, si es distinto de cadena vacía y si es distinto de None


numero_entero=0;
boolean=bool(numero_entero)
print(boolean)


numero_entero=5;
boolean=bool(numero_entero)
print(boolean)
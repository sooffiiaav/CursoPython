numero=int(input('Introduce un num del 1 al 12:'))

if numero==1 or numero==2 or numero==12:
    print('INVIERNO')
elif numero==3 or numero==4 or numero==5:
    print('PRIMAVERA')
elif numero==6 or numero==7 or numero==8:
    print('VERANO')
elif numero==9 or numero==10 or numero==11:
    print('OTOÑO')
else:
    print('ESTACION DESCONOCIDA')
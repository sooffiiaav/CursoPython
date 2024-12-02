from random import randint

print('***SISTEMA ID UNICO***')

nombre=input('Dime tu nombre')
apellidos=input('Dime tu apellido')
fecha_nacimiento=input('Dime tu fecha de nacimiento (YYYY)')
valor_random=randint(1,3000)

inicio_nombre=nombre[0:2].upper()
inicio_apellido=apellidos[0:2].upper()
final_fecha=fecha_nacimiento[2:4]

print('***************************************')
print(f'Tu ID final es {inicio_nombre}{inicio_apellido}{final_fecha}{valor_random}')

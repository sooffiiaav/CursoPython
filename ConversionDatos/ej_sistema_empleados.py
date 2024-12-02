from ConversionDatos.conversion_tipos_datos import boolean

nombre=input('Dime tu nombre:')
edad=int(input('Dime tu edad'))
salario=float(input('Dime tu salario mensual'))
jefe_departamento=input('¿Eres jefe de departamento?')
jefe_departamento = jefe_departamento.lower() == 'si'

print(f'***LISTADO DE EMPLEADOS***\n Nombre: {nombre}\nEdad:{edad}\nSalario:{salario}\nEs jefe de departamento:{jefe_departamento}')
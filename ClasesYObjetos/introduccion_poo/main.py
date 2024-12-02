from ClasesYObjetos.introduccion_poo.empleado import Empleados
from ClasesYObjetos.introduccion_poo.empresa import Empresa

#Creamos una instancia de empresa
empresa1= Empresa('Telefonica')

#Contratar empleados
empresa1.contratar_empleado('Juan','Ventas')
empresa1.contratar_empleado('Miguel','administrador')
empresa1.contratar_empleado('Sofia','Programadora')

print(f'Total empleados: {Empleados.contador_empleados}')

#Obtener numero empleados en x departamento:
print(f'Empleados en el dep de Ventas: {empresa1.obtener_numero_empleados_departamento('Ventas')}')
empresa1.obtener_total_empleados()


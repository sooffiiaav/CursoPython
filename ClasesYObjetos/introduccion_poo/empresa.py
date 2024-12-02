from traceback import print_tb

from ClasesYObjetos.introduccion_poo.empleado import Empleados


class Empresa:

    def __init__(self,nombre_emp):
        self.nombre_emp=nombre_emp
        self.empleados=[]


    def contratar_empleado(self,nombre,departamento):
        empleado = Empleados(nombre,departamento)
        self.empleados.append(empleado) #Agregamos a la lista vacía los empleados

    def obtener_numero_empleados_departamento(self,departamento):
        contador_empleados_por_departamento = 0
        for empleados in self.empleados:
            if empleados.departamento == departamento:
                contador_empleados_por_departamento +=1
        return contador_empleados_por_departamento

    def obtener_total_empleados(self):
        print('Total de empleados: ')
        for empleado in self.empleados:
            print(f'''Id: {empleado.id}
            Nombre: {empleado.nombre}
            Departamento: {empleado.departamento}
            ''')
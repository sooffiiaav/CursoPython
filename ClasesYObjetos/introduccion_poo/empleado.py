
class Empleados:

    contador_empleados=0

    def __init__(self, nombre, departamento):
        self.nombre=nombre
        self.departamento=departamento
        Empleados.contador_empleados +=1
        self.id=Empleados.contador_empleados

    @classmethod
    def obtener_total_empleados(cls):
        return cls.contador_empleados

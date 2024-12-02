

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad


#Para sobrecargar el operador suma, cada operador tiene un metodo determinado
    def __add__(self, other):
        return f' {self.nombre}  {other.nombre}'


    def __sub__(self, other):
        return self.edad - other.edad


persona1= Persona('Juan',10)
persona2=Persona('Pepe',9)
print(persona1+persona2)
print(persona1-persona2)




#Al no especificar de que clase esamos heredando, de forma predeterminada heredamos de la clase Object
class Persona:
    def __init__(self,nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

    #Sobreescribir metodo str, que permite imprimir los valores de los atributos de nuestra clase

    def __str__(self):
        return f'''
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        Dir. mem: {super.__str__(self)} 
'''
#En caso de que queramos acceder al metodo definido en la clase padre: {super.__str__(self)}

#Codigo principal:
persona1=Persona('Sofia','Velardiez')
print(persona1) #Se llama automaticamente al metodo str desde print



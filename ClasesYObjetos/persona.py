#Para definir una clase:
class Persona:


    #self sirve para acceder a los metodos y atributos de nuestra clase
    def set_persona(self,nombre,apellido):
        #Creamos atributos de la clase:lo primero es el nombre del parametro y lo segundo el nombre del atributo
        self.nombre = nombre
        self.apellido = apellido

    def get_persona(self):
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')



#Creacion de objetos
if __name__ == '__main__':

    #Creacion d eun primer objeto
    person1 = Persona() #Creamos un objeto vacio en memoria
    person1.set_persona('Layla','Gomez')
    person1.get_persona()
    print()
    person2 = Persona()
    person2.set_persona('Ian', 'Sanchez')
    person2.get_persona()
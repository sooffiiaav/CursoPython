

class Persona2:

    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    def get_persona(self):
        print(f'''Persona:
           Nombre: {self.nombre}
           Apellido: {self.apellido}''')


if __name__ == '__main__':
    '''
    Al haber creado al constructor ya no hace falta crear el objeto,
    como haciamos antes de persona1= Persona(),
    ya que con el constructor CREAMOS e INICIALIZAMOS
    '''
    persona1 = Persona2('Miguel', 'Gomez')
    persona1.get_persona()

    persona2 = Persona2('Sofia', 'Velardiez')
    persona2.get_persona()
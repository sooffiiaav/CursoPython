#Tambien sirve para abrir y cerrar conexiones de bdd etc
class manejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print('Obtenemos el recurso'.center(50,'-'))
        self.nombre = open(self.nombre, 'r', encoding='utf8')
        return self.nombre

    def __exit__(self, exc_type, exc_val, traza_error):
        print('Cerramos el recurso'.center(50,'-'))
        if self.nombre:
            self.nombre.close()
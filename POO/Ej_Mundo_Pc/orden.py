

class Orden:

    contador_ordenes=0

    def __init__(self,ordenadores):
        Orden.id_orden=Orden.contador_ordenes
        self.id_orden=Orden.contador_ordenes
        #Recibimos la lista de objetos de tipo ordenador
        self.ordenadores = ordenadores

    def agregar_ordenadores(self,ordenador):
        self.ordenador.append(ordenador)

    def __str__(self):
        ordenadores_str=' '
        for ordenador in self.ordenadores:
            ordenadores_str += '\n' + ordenador.__str__()
        return f'''Orden {self.id_orden}
        Ordenadores: {ordenadores_str}'''

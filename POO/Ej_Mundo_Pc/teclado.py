from POO.Ej_Mundo_Pc.ej_mundo_pc import DispositivoEntrada


class Teclado(DispositivoEntrada):

    contador_teclados=0

    def __init__(self,marca,tipo_entrada):
        Teclado.contador_teclados +=1
        self.id_teclado=Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'''
        Id Teclado: {self.id_teclado}
        Marca: {self.marca}
        Tipo_entrada: {self.tipo_entrada}'''

if __name__=='__main__':

    teclado1=Teclado('HP', 'Bluethooth')
    print(teclado1)
    teclado2=Teclado('Samsung','USB')
    print(teclado2)
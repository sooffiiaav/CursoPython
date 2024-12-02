from POO.Ej_Mundo_Pc.ej_mundo_pc import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones=0

    def __init__(self,marca,tipo_entrada):
        Raton.contador_ratones +=1
        self.id_raton=Raton.contador_ratones
        #self.marca = marca
        #self.tipo_entrada=tipo_entrada
        super().__init__(marca,tipo_entrada) #Constructor, más recomendable

    def __str__(self):
       return f'''
       Id Raton: {self.id_raton}
       Marca: {self.marca}
       Tipo_entrada: {self.tipo_entrada}
        '''
#Codigo principal:

if __name__== '__main__':
    raton1= Raton('HP','USB')
    print(raton1)
    print()
    raton2=Raton('Acer','Bluetooth')
    print(raton2)


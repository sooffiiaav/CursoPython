

class Aritmetica:



    def __init__(self,operador1=None, operador2=None):
        self.operador1 = operador1
        self.operador2 = operador2

    def sumar(self):
        suma= (self.operador1 + self.operador2)
        print(f'Resultado +: {suma}')

    def restar(self):
        resta= (self.operador1 - self.operador2)
        print(f'Resultado -: {resta}')

    def multiplicar(self):
        multiplicacion= (self.operador1 * self.operador2)
        print(f'Resultado *: {multiplicacion}')

    def dividir(self):
        division= (self.operador1 / self.operador2)
        print(f'Resultado /: {division}')

if __name__ == '__main__':


    serie1=Aritmetica(5,9)
    serie1.sumar()
    serie1.restar()
    serie1.multiplicar()
    serie1.dividir()

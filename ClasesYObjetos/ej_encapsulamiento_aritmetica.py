
class AritmeticaEncapsulada:

    def __init__(self, operador1, operador2):
        self._operador1=operador1
        self._operador2=operador2

    @property
    def operador1(self):
        return self._operador1

    @property
    def operador2(self):
        return self._operador2

    @operador1.setter
    def operador1(self, operador1):
        self._operador1

    @operador2.setter
    def operador2(self, operador2):
        self._operador2

    def sumar(self):
        return self._operador1 + self._operador2

    def restar(self):
        return self._operador1 - self._operador2

    def multiplicar(self):
        return self._operador1 * self._operador2

    def dividir(self):
        return self._operador1 / self._operador2

if __name__ == '__main__':

    operacion1=AritmeticaEncapsulada(10,5)
    print(f'Suma: {operacion1.sumar()}')
    print(f'Resta: {operacion1.restar()}')
    print(f'Division: {operacion1.dividir()}')
    print(f'Multiplicacion: {operacion1.multiplicar()}')




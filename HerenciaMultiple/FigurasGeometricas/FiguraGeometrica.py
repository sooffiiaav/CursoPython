

class FiguraGeometrica:
    def __init__(self, ancho , alto):
        if self._validar_calor(ancho):
            self._ancho=ancho
        else:
            self._ancho=0
            print(f'Valor erroneo ancho: {ancho}')
        if self._validar_calor(alto):
            self._alto=alto
        else:
            self._alto=0
            print(f'Valor erroneo alto:{alto} ')

    def __str__(self):
        return f'''
        ALTO: {self._alto}
        ANCHO: {self._ancho}'''

    def get_alto(self):
        return self._alto

    def set_alto(self,alto):
        if self._validar_calor(alto):
            self._alto=alto
        else:
            print(f'Valor erroneo alto: {alto}')

    def get_ancho(self):
        return self._ancho

    def set_ancho(self,ancho):
        if self._validar_calor(ancho):
            set._ancho=ancho
        else:
            print(f'Valor erroneo ancho: {ancho}')

    def _validar_valor(self,valor):
        return True if 0 < valor < 10 else False



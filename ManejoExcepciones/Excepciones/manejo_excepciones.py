from NumerosIdenticosException import NumerosIdenticosException

resultado = None

try:
    #Ambos valores se deben de convertir a tipos enteros
    a = int(input('Primer numero'))
    b = int(input('Segundo numero'))
    if a == b:
        raise NumerosIdenticosException('Numeros identicos')
    resultado = a/b
except ZeroDivisionError as e:
    print(f'Ocurrio un error:  {e}, {type(e)}')
except TypeError as e:
    print(f'Ocurrio un error {e}, {type(e)}')
except Exception as e: #No se debe de poner al inicio ya que las otras son mas expecificas
    print(f'Ocurrio un error: {e}, {type(e)}')
else:
    print('No se lanza ninguna excepcion')
#El bloque finally siempre se va a ejecutar independientemente de que se lanc la excepcion o no
#Sirve para liberar recursos
finally:
    print('Ejecución del bloque finally')

print(f'Resultado: {resultado}')
print("Continuamos... ")
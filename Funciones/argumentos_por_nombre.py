from Variables.reglas_convenciones import nombre


def imprimir_persona(nombre,apellido,edad):
    print(f'Persona: {nombre}, apellido={apellido}, edad = {edad}')

#De esta forma no es necasario que sigan el orden que tienen los parametros en el metodo, aunque se imprimen en el orden de los parametros
imprimir_persona(nombre='Sofia',apellido='V',edad=19)

#Argumentos por defecto

'''
En caso de que solo queramos mandar un valor, debemos de dejar vacios los parametros
que pasamos en el método o asignarles el valor 0 en caso de que
sea un numero
'''
imprimir_persona(nombre='Carlos')
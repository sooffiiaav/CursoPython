

def persona_mayusculas(nombre,apellido,edad):
    print('Esta funcion devuelve varios valores.')
    return (nombre.upper(),apellido.upper(),edad)

nombre, apellido,edad=persona_mayusculas('Sandra','Jimenez',45)
print(f'Resultado Persona: nombre = {nombre}, apellido= {apellido}, edad= {edad}')
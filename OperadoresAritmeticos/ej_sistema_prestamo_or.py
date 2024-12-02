print('***SISTEMA PRESTAMO DE LIBROS***')

vivienda=int(input('A cuantos km vives?'))
credencial=(input('Tienes credencial de estudiante? (Si/No)'))
prestamo_libro=(vivienda<=3 or credencial.strip().lower()=='si')

print(f'¿Tienes prestamo de libros?{prestamo_libro}')
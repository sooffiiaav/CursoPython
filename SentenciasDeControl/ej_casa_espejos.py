edad=int(input('Que edad tienes?'))
miedo=input('Tienes miedo a la oscuridad(Si/No)?')

if not(edad>=10 and miedo.strip().lower()=='no'):
    print('No puedes entrar a la casa de los espejos')
else:
    print('Puedes entrar a la casa de los espejos')
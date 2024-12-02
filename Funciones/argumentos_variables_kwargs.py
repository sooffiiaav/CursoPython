
#Debe de seguir este orden
def superheroe_superpoderes (nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args} - Mas info: {kwargs}')


superheroe_superpoderes('Spiderman','Instinto aracnido','Armadura', edad=17, empresa='Marvel')

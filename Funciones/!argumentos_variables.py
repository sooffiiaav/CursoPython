

#*args debe de ser el ultimo parametro
def superheroes_poderes(superheroe,nombre,*args):
    print(f'Superheroe: {nombre} - {nombre} - {args}')
    for poderes in args:
        print(f'\t Superpoder: {poderes}')



superheroes_poderes('Spiderman', 'Peter Paker', 'Instinto aracnido', 'Telaraña')
superheroes_poderes('Ironman','Tony Stark', 'Fuerza','Volar','Traje metalico')
superheroes_poderes('Capitan America','ijoputa')
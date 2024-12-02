
n_canciones=int(input('Cuantas canciones tendrá tu lista'))
playlist=[]
contador=0
while contador< n_canciones:
    cancion=input('Introduce una cancion:')
    playlist.append(cancion)
    contador+=1
playlist.sort() #ordena alfabeticamente
for lista in playlist:
    print(lista)
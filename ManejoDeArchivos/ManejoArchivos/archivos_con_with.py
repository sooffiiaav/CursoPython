#Con el with de manera automatica abre y cierra el archivo
#with open('pruebaArchivoPython.txt','r', encoding='utf8') as archivo:
from ManejoArchivos.manejoArchivos import manejoArchivos

with manejoArchivos ('pruebaArchivoPython.txt') as archivo:
    print(archivo.read())

'''
r - read, el archivo debe de estar creado
a - append. añade información aun archivo que ya tiene, sino existe lo crea
w - leer, sino existe lo crea
x - create
t - archivos de texto
b - archivos de tipo binario
w+ o r+ para combinar lectura y escritura
'''
try:
    archivo = open('pruebaArchivoPython.txt','r', encoding='utf8')
    #print(archivo.read())

    #Para leer solo algunos caracteres (decimos el numero de caracteres que queremos leer):
    #print(archivo.read(5))

    #Para leer lineas completas:
    #print(archivo.readline())
    #print(archivo.readline())

    #Iterar el archivo:
    #for linea in archivo:
    #    print(linea)

    #Leer todas las lineas
    #print(archivo.readlines())

    #Acceder a una linea de la lista
    #print(archivo.readlines()[0])

    #Para copiar la info de un archivo existente a otro nuevo
    archivo2 = open('copiaArchivoPython.txt','a', encoding='utf8')
    archivo2.write(archivo.read())

except Exception as e:
    print({e})
finally:
    archivo.close()
    archivo2.close()
    print('Se ha terminado el proceso de leer y copiar archivos')
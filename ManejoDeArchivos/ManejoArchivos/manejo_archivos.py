#open sirve tanto para abrir un archivo como para crearlo en caso de que no exista
#Podemos usarlo para leer y escribir en un archivo
try:
    #Se crea en l propio proyecto a que no le hemos dado una ruta donde crearse
    #El encoding en este caso sirve para que acepte las tildes
    archivo = open('pruebaArchivoPython.txt', 'w', encoding='utf8')
    archivo.write('Agregamos información al archivo\n')
    archivo.write('Adios')
except Exception as e:
    print({e})
finally:
    archivo.close()
    print('Archivo cerrado')


def obtener_coordenadas():
    x,y,z=10,20,30
    return x,y,z

resultado = obtener_coordenadas()
print(resultado)

#Unpacking
def obtener_cordenadas2(x,y,z):
    return x,y,z

x,y,z=obtener_cordenadas2(10,30,50)
print(f'Coordenada x: {x}, y: {y}, z:{z}')


#NO FUNCIONA ESTA CLASE
#variable global:
contador_global=0

def incrementar_contador():
    #variable local:
    contador_local=0

    #usamos variable global,indicando cual es
    global contador_global
    contador_global += 1


    contador_local+=1


print(f'Contador global: {contador_global}')
print(f'Contador local: {contador_local}')

incrementar_contador()
incrementar_contador()
print(f'Contador global: {contador_global}')
print(f'Contador local: {contador_local}')
nombre=input('Dime tu nombre:')
pasos=int(input('Dime los pasos que has caminado hoy:'))

META_PASOS_DIARIO=10000
CALORIAS_POR_PASO=0.04

calorias_quemadas= pasos* CALORIAS_POR_PASO

resolucion= f'Enhorabuena {nombre}, has alcanzado tu rango de pasos' if pasos>=META_PASOS_DIARIO else f'Lo siento {nombre}, no has alcanzado tu meta'
print(f'{resolucion} Tus calorias quemadas en el dia son: {calorias_quemadas}')

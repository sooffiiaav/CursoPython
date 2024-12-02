continuar=input('Deseas continuar dentro del sistema bancario?(Si/No)')

if not(continuar.strip().lower()=='si'):
    print('Saliendo del sistema')
else:
    print('Continuas en el sistema')
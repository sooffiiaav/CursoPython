


def celsius_a_fahrenheit(celsius):
    conversor1=int((celsius*9/5)+32)
    print(f'El resultado de convertir {celsius} grados celsius as Fahrenheit es: {conversor1}')

def fahrenheit_a_celsius(fahrenheit):
    conversor2= int((fahrenheit-32) * 5/9)
    print(f'El resultado de convertir {fahrenheit_us}  grados fahrenheit as Celsius es: {conversor2}')


celsius_us=int(input('Introduce los grados celsius que quieras convertir:'))
celsius_a_fahrenheit(celsius_us)
print()
fahrenheit_us=int(input('Introduce los grados fahrenheit que quieras convertir:'))
fahrenheit_a_celsius(fahrenheit_us)
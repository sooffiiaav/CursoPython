
#Colecciones de datos no ordenadas, eliminan los datos duplicados

a={1,2,3,4}
b={3,4,5,6}

#unir sets
union= a|b
print(union)

#interseccion: valores que coinciden en ambos sets
interseccion=a&b
print(interseccion)

#diferencia: eliminamos del primer set los elementos que se repiten en el segundo
diferencia=a-b
print(diferencia)
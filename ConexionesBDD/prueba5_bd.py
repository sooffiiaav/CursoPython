import psycopg2

conexion = psycopg2.connect(
    user= 'postgres',
    password= 'root',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db'
)

# De esta forma nos eviitamos tener que cerra de forma manual el curso, pero es OBLIGATORIO cerrar la conexion
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s, %s, %s)'
            #valores = ('Carlos', 'Lara','clara@gmailcom')
            valores = (('Carlos', 'Lara','clara@gmailcom'),
                       ('Pepito','Grillo','ppgr@gmail.com'),
                       ('Maria','Gonzalez','mg@gmail.com'))
            #cursor.execute(sentencia,valores) para un solo valor
            cursor.executemany(sentencia, valores)
            # conexion.commit() al usar el with, el commit se ejecuta en automatico, por lo que no hay colocarlo manualmente
            registros_insertados = cursor.rowcount #preguntamos por el numero de registros que han sido afectados
            print(f'Registros Insertados: {registros_insertados}')

except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()

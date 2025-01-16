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
            #ponemos el where para que solo se cambie uno de los registros, sino se modificaran todos
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            #valores = ('Juan Carlos', 'Juarez','jcjuarez@gmail.com',7) # el siete corresponde al id del registro que queremos cambiar
            valores = (
                       ('Pepito','de los Palotes','pepito@gmail.com',6),
                       ('Andrea','Martin','andrmrt2gmai.com',1)
            )
            #cursor.execute(sentencia,valores) #para un solo valor
            cursor.executemany(sentencia,valores)
            registros_actualizados = cursor.rowcount
            print(f'Registros actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()
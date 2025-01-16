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
            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia)
            registros = cursor.fetchall()  # recupera todos los registros de la sentencia (fetchall)
            print(registros)
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()


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
            # sentencia = 'SELECT * FROM persona WHERE id_persona IN (1,2)' # Coge el prime ry segundo registro en este caso
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            #llaves_primarias = ((1,2,3),) # se debe de pasar como tupla de otra tupla
            entrada = input('Proporciona los iid a buscar:')
            llaves_primarias = (tuple(entrada.split(',')),)
            cursor.execute(sentencia,llaves_primarias)
            registros = cursor.fetchall()
            for registros in registros:
                print(registros)
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()


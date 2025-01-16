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
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona = 1
            #id_persona = input('Proporciona el valor id_persona:')
            cursor.execute(sentencia,(id_persona,)) #Es necesario pasarlo a una tupla
            registros = cursor.fetchone()  # mejoramos el rendimiento ya que solo busca un registro (fetchone)
            print(registros)
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()


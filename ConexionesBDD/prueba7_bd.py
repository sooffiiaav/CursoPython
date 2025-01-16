from idlelib.configdialog import is_int

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
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s' #El IN se pone en caso de que sean varios registros, sino se pone =
            #valores = (7,)
            #entrada = input('Proporciona el id_persona a eliminar: ')
            #valores = (entrada ,)
            entrada = input('Proporciona el id_persona a eliminar: ')
            valores = (tuple(entrada.split(',')),)
            cursor.execute(sentencia,valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()

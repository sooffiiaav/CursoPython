import psycopg2 as bd

conexion = bd.connect(
    user= 'postgres',
    password= 'root',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db'
)
#Si quueremos quitar el conexion.autocomit lo unico que debemos hacer es añadir la sentencia de with con exception
try:
    conexion.autocommit = False #no guarda los cambios de forma automatica
    cursor = conexion.cursor()

    sentencia = 'INSERT INTO persona (nombre,apellido,email) VALUES (%s,%s,%s)'
    valores = ('Maria','Esparza','mesparza@gmail.com')
    cursor.execute(sentencia,valores)

    sentencia = 'UPDATE persona SET nombre = %s, apellido=%s, email=%s WHERE id_persona= %s'
    valores = ('Juan Carlos','Juareyhuygbiibz','jc2gmail.com',6)
    cursor.execute(sentencia,valores)

    conexion.commit()
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error {e}')

finally:
    print('Termina la transaccion')
    conexion.close()
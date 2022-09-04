from psycopg2 import connect

connection=connect(
    user='postgres',
    password='afreddy311',
    host='localhost',
    port=5432,
    database='tecsup'
)

cursor=connection.cursor()

# cursor.execute("SELECT version();")

# transaccionabilidad insert,update,delete
try:
    cursor.execute("INSERT INTO area (name) VALUES ('Mineria');")
    connection.commit()
except Exception as e:
    connection.rollback()
    print(f'ocurrio un error ->{e}')


#fetchone -> usar cuando la consulta trauga una fila
#fetchall -> usar cuando la consulta traiga mas de una fila

# record=cursor.fetchone()
record=cursor.fetchall()

print(record)

#obligatorio cerrar la sesion y la conexion 

cursor.close()    
connection.close()






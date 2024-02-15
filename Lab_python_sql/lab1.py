#Primer lab para Conectar la script de Python con PostgreSQL

import psycopg2
conn = psycopg2.connect(host="localhost", database="demo", user="postgres", password="javieredo1234")



cursor = conn.cursor()

# Define tu consulta SQL
sql_query = "SELECT * FROM bookings.flights;"

# Ejecuta la consulta SQL
cursor.execute(sql_query)

# Obtiene todas las filas resultantes
rows = cursor.fetchall()

# Imprime cada fila
for row in rows:
        print(*row)
        #print("%s %s" % (row[0], row[1]))

# Cierra el cursor y la conexión
if conn is not None:
    cursor.close()
    
conn.close()
















import MySQLdb

bd = MySQLdb.connect(host="localhost", # El servidor
					 user="root", # Tu usuario
					 passwd="3141592" # Tu pass word
					 ) # El nombre de la base

cur = bd.cursor()

# Ejecutamos un sentencia en la base
cur.execute("SELECT * FROM TU_TABLA")

# Imprimimos las columnas
for row in cur.fetchall() :
	print row


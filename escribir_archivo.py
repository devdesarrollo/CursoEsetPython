# Codigo de ejemplo para ver como escribir archivos en Python

# Vamos a crear un archivo numeros.txt y vamos a escribir en
# el los numeros del 1 al 100

archivo_salida = open("numeros.txt", "w")

for n in range(1,101):
	archivo_salida.write("%d\n" % n)


archivo_salida.close()
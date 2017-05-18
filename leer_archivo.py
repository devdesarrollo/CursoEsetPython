# Codigo de ejemplo para ver como leer un archivo
# guardando en el disco

# Vamos a abrir el archivo numeros.txt y vamos a leer e
# imprimirlo por pantalla 

archivo_entrada = open("D:/ARAMAYO_NICOLAS/__Curso ESET Python/numeros.txt", "r")

for linea in archivo_entrada.readlines():
	print linea.strip("\n")

archivo_entrada.close()
	
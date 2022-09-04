## Función open(file, mode)
# file -> El nombre del archivo, tener en cuenta la ubicación fisica
# mode -> El permiso con el cual va a ser abierto el archivo
## r -> Lectura
## a ->
## w ->
## x -> Creación, crea el archivo si este no existe, si existe retornara un error
# open('nombres.txt', 'x')
file = open('prueba.txt', 'r')
# Al abrir un archivo en modo lectura, tenemos 2 funciones
# read() -> Retornamos el contenido del archivo
# readlines() -> Retornamos 
#print(file.read())
#file.seek(0) -> Esta función nos regresa al cursor inicial
for line in file:
    print(line)
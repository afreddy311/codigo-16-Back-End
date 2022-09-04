from json import loads, dump

## Función open(file, mode)
# file -> El nombre del archivo, tener en cuenta la ubicación fisica
# mode -> El permiso con el cual va a ser abierto el archivo
## a -> Escribe pero mantiene el contenido del archivo
## w -> Escribe y reemplaza todo el contenido del archivo

## Plus+
# r+ -> Leer y escribir un archivo

# Archivo de texto (.txt)
# file = open('nombres.txt', 'a')
# file.write('Arturo Chaparro\n')
# file.writelines(["Alan Fermin", "Andres Taboada"])
# file.close()

# Archivo json (.json)
# file = open('alumnos.json', 'r+')
# file_data = loads(file.read())
# 
# file_data.append({
#     "nombre": "Alan",
#     "edad": 27
# })
# 
# file.seek(0)
# dump(file_data, file, indent=4)
# file.close()

# Contexto with
# __enter__ y __exit__
with open('alumnos.json', 'r+') as file:
    file_data = loads(file.read())
    
    file_data.append({
        "nombre": "Yesica",
        "edad": 21
    })
    
    file.seek(0)
    dump(file_data, file, indent=4)
from pathlib import Path
from os import listdir
from importlib import import_module

path_parent=Path('./app/routers')

for module in listdir(path_parent):
    if 'router' in module:
        print(module[:-3])#quita los 3 ultimos caracteres
        import_module(#importa automaticamente las nuevas rutas
            f'app.routers.{module[:-3]}'
        )







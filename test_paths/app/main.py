import yaml
import os
print('hola')

# script_dir = os.path.dirname(os.path.abspath(__file__))
# yaml_file_path = os.path.join(script_dir, '../config/local_settings.yaml')

# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# with open('config/local_settings.yaml', "r") as file:
# with open('../config/local_settings.yaml', "r") as file:
with open('..\\config\\local_settings.yaml', "r") as file:
    data_file = yaml.safe_load(file)

print(data_file)


# Obtener la ruta del directorio del script actual
# script_dir = os.path.dirname(os.path.abspath(__file__))

# # Unir la ruta del directorio del script con la ruta relativa al archivo yaml
# yaml_file_path = os.path.join(script_dir, 'config/local_settings.yaml')

# # Abrir el archivo yaml
# with open(yaml_file_path, "r") as file:
#     data_file = yaml.safe_load(file)

# print(data_file)

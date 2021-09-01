import os
   
print('Salida:')
print(os.getcwd())

#Crear un directorio
os.mkdir("C:\MyPythonProject")

#Cambiar el directorio de Trabajo:
os.chdir("C:\\")
print(os.getcwd())

#Cambiar CWD a padre
os.chdir("C:\\MyPythonProject")
print(os.getcwd())

os.chdir("..")
print(os.getcwd())


#Eliminar directorio
os.rmdir("C:\\MyPythonProject")
print(os.listdir("C:\\Datos"))
print(os.listdir())
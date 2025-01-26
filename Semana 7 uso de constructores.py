# "Consideremos un nombre archivo que simula el abierto y cerrado
# un archivo externo, como podría ser un nombre:
class Archivo:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        print(f"Archivo  {self.nombre_archivo} abierto.")

    def __del__(self):
        print(f"Archivo {self.nombre_archivo} cerrado.")

# "Aquí, el constructor __init__ se encarga de inicializar el nombre archivo,
# mientras que el destructor __del__ se encarga de abrir.

# Al crear y eliminar nombre y archivo, se pueden observar las acciones
# de los constructores y destructores:

mi_archivo = Archivo("datos.txt")
del mi_archivo

# La instancia mi_archivode la clase archivo es creada y luego eliminada.
# Esto desencadena primero el constructor y luego el destructor.
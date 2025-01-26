# Ejemplo de Creación de Animal:
# "Vamos a crear una clase animal con atributos.

class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

mi_animal = Animal("Bambi", "Venado")

print(f"Nombre: {mi_animal.nombre}")
print(f"Especie: {mi_animal.especie}")


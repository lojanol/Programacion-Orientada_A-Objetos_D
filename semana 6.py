# clase base (super clase) - animales
class Animal:
    def __init__(self, nombre, edad):
        # Encapsulamiento: Atributos protegidos con - (convencion)
        self._nombre = nombre
        self._edad = edad

    # Metodo obtener para el nombre
    def get_nombre(self):
        return self._nombre

    # Metodo para hacer un sonido ( Polimorfismo - se refine en las subclases)
    def hacer_sonido(self):
        print("sonido generico de animal")

    def __str__(self):
        return f"nombre:{self._nombre}, edad:{self._edad}"

# clase derivada (subclase) - Vaca ( hereda de animal)
class Vaca(Animal):
    def __init__(self, nombre, edad, raza):
        # llaman al constructor de la clase base usando super()
        super().__init__(nombre, edad)
        self._raza = raza # atributo especifico de Vaca

    # polimorfismo: sobrescribe el metodo hacer_sonido()
    def hacer_sonido(self):
        print("Muu Muu")
    # Metodo getter para la raza
    def get_raza(self):
        return self._raza

    def __str__(self):
        return f"{super().__str__()} Raza: {self._raza}"


# clase derivada (subclase) - Perro (herreda de animal)
class Perro(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self._color = color

    # polimorfismo: sobrescribe el metodo hacer_sonido()
    def hacer_sonido(self):
            print("Gua Gua")

    # Metodo getter para el color
    def get_color(self):
        return self._color
    def __str__(self):
        return f"{super().__str__()} Color: {self._color}"

# Funcion que demuestra polimorfismo (acepta objetos de diferentes clases)
def hacer_que_animal_hable(animal):
        animal.hacer_sonido()


# Ejemplo de uso

if __name__ == "__main__":

   mi_vaca =Vaca ("lola",8, "Brama")
   mi_perro = Perro("balu", 2, "amarillo")
   otro_animal = Animal("animal generico",12)

   print(mi_vaca)
   print(mi_perro)
   print(otro_animal)

   print("\nsonidos:")
   hacer_que_animal_hable(mi_vaca)
   hacer_que_animal_hable(mi_perro)
   hacer_que_animal_hable(otro_animal)

   # Encapsulamiento:Acceso controlado a los atributos (usando gettes)
   print(f"nombre de la vaca es:{mi_vaca.get_nombre()}")
   print(f" la raza de la vaca es:{mi_vaca.get_raza()}")
   print(f" el color del perro es:{mi_perro.get_color()}")
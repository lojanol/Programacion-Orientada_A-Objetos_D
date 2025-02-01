# Definición de la clase libro
# Esta clase representa un libro con titulo y año de publicacion.
class libro:
    # Constructor de la clase con tres parámetros: titulo , autor y año
    def __init__(self, titulo, autor, año):
        self.titulo = titulo  # Asigna el titulo del libro
        self.autor = autor  # Asigna el autor del libro
        self.año = año  # Asigna el año de la publicacion del libro

# Definición de la clase biblioteca
# Esta clase maneja una colección de libros.
class Biblioteca:
    # Constructor de la clase biblioteca
    # Inicializa la lista como vacía
    def __init__(self):
        self.libros = []  # Lista para almacenar los objetos de tipo de libro

    # Método para agregar un nuevo libro a la biblioteca
    def agregar_libro(self, libro):
        self.libros.append(libro)  # Añade el objeto libro a la lista de libros

    # Método para mostrar todos los libros en la biblioteca
    def mostrar_libros(self):
        for libro in self.libros:  # Itera para cada libro en la lista de libros.
            # Imprime la información del libro
            print(f"titulo: {libro.titulo}, autor: {libro.autor}, año: {libro.año}")

# Creando instancias de libro
libro1 = libro('El señor de los anillos', 'Damian Cardenas', '1968')
libro2 = libro('la culpa es de la vaca', 'Isabella Alvares', '1950')


# crando una instancia de biblioteca y agregando libros
biblioteca=Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Mostrando los libros en la biblioteca
biblioteca.mostrar_libros()
# creacion de la clave libro

class Libro:
# Creamos el constructor de la clase que inicializara el libro

    def __init__(self, titulo, autor, categoria, codigo):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.codigo = codigo

#Creacion del metodo que nos devuelve una cadena de texto

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}, codigo: {self.codigo}"

# creacion de la clase ususario

class Usuario:
    def _init_(self,nombre_usuario, codigo_usuario):
        self.nombre_usuario = nombre_usuario
        self.codigo_usuario = codigo_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"{self.nombre_usuario} (Codigo: {self.codigo_usuario})-Libros prestados {libro}"

# creacion de la clase biblioteca

class Biblioteca:
    def __init__(self):
        self.catalogo = {}  # ALmacena los libros disponibles decauerdo al codigo del usuario
        self.usuarios = {}  # Almacena a los usuarios registrados por su codigo

    def agregar_libro(self, libros):
        if libro.codigo not in self.catalogo:
            self.catalogo[libro.codigo] = libro
            print(f"Se agregó el libro {libro}")
        else:
            print("Este libro ya está en la biblioteca")

# Metodo de la biblioteca para eliminar un libro

    def eliminar_libro(self, codigo):
        if codigo in self.catalogo:
            del self.catalogo[codigo]
            print(f"Se eliminó el libro {libro}")

        else:
            print(f"No se encontró ningún libro en la biblioteca {codigo}.")

# Metodo registrar usuario, agrega un usario si el codigo no existe

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios[usuario.codigo_usuario] = usuario
            print(f"Se registó usuario : {usuario.nombre_usuario}")

        else:
            print(f"El ID de usuario {usuario.id_usuario} ya está registrado.")

    def eliminar_usuario(self, codigo_usuario):
        if codigo_usuario in self.usuarios:
            self.usuarios.pop(codigo_usuario)
            print(f"Usuario con ID {codigo_usuario} ususario eliminado.")
        else:

            print(f"No se encontró ningún usuario.")

    def prestar_libro(self, codigo_usuario, isbn):
        if codigo_usuario in self.usuarios and isbn in self.usuarios:
            print("El usuario no esta registrado.")

            return
        if Usuario not in self.catalogo:
            print("El libro no está disponible")

        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, codigo_usuario, codigo):
        if codigo_usuario in self.usuarios and codigo in self.usuarios:
            if codigo_usuario not in self.usuarios:
                print("El usuario no se encuentra registrado")

# Busca si el usuario tiene un libro prestado
            usuario = self.usuarios[codigo_usuario]
            for libro in usuario.libros_prestados:
                if libro.codigo == codigo:
                    usuario.libros_prestados.remove(libro)
                    self.catalogo[libro.codigo] = libro  # Usar el objeto libro directamente
                    print(f"{usuario.nombre_usuario}: ha devuelto el libro {libro}")
                    return

            print("Este libro no estaba prestado a ningún usuario")


    def buscar_libros(self, criterio, valor):
        resultados = []
        for libros in self.catalogo.values():
            if criterio == "titulo" and valor.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.autor.lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            return usuario.libros_prestados
        else:
            print("Usuario no encontrado.")
            return []

biblioteca = Biblioteca()

libro1 = Libro("la culpa de la vaca", "Damian alvares", "Ciencia ficcion", "8670062220083")
libro2 = Libro("1987", "Willian Marquez", "Terror", "9670451424834")
libro3 = Libro("el extrajero", "Homero", "Lectura", "8760518250262")

# creacion de biblioteca

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

usuario1 = Usuario("Liliana", "U001")
usuario2 = Usuario("Damian", "U002")

biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

biblioteca.prestar_libro("U001", "9780061120084")
biblioteca.prestar_libro("U002", "9780451524935")

# prestar libro
biblioteca.prestar_libro("Us003", "L005")
biblioteca.prestar_libro("Us001", "L002")
biblioteca.prestar_libro("Us004", "L003")


# Devolver un libro
biblioteca.devolver_libro("Us001", "L002")  # Andrea devuelve "Cien años de soledad"

# Mostrar libros disponibles en la biblioteca después del préstamo
print("\nLibros disponibles en la biblioteca:")
for libro in biblioteca.catalogo.values():
    print(libro)

# Mostrar estado de los usuarios
print("\nEstado de los usuarios:")
print(usuario1)  # Liliana no debería tener libros
print(usuario2)  # Damian sigue teniendo "1987"
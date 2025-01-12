def crear_libro(titulo_libro,autor_libro,año_publicacion):
    """creamos un diccionario que representa un libro.

    Args:
        titulo_libro: titulo del libro(string).
        autor_libro: nombre del libro(string).
        año_publicacion: el año del libro(int).

    Returns:
        un diccionario que representa un libro.
    """
    Libro= {

        "titulo": titulo_libro,
        "autor": autor_libro,
        "año": año_publicacion
        }
    return Libro

# ejemplo de uso
libro1 =crear_libro("el señor de los anillos","Miguel de servantes", 1960)
print(f"libro creado:{libro1}")

print(f"autor del libro:{libro1['autor']}")
# imprimir: autor del libro: Miguel de servantes

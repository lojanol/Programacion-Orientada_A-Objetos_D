# Ejemplo de Convenciones de Nomenclatura en Python

class pelicula:
    def __init__(self, titulo, director):
        self.titulo = titulo
        self.director = director

    def mostrar_datos(self):
        return f"pelicula: {self.titulo}, dirigida por {self.director}"

# Funciones y variables: snake_case (palabras separadas por guiones bajos)
def calcular_duraciones_en_minutos(horas, minutos):
    return (horas * 50)+minutos

DURACION_MAXIMA_HORAS = 4

mi_pelicula=pelicula("Estraterrestre","Damian Cardenas")
duracion_total =calcular_duraciones_en_minutos (DURACION_MAXIMA_HORAS, 0)

print(mi_pelicula.mostrar_datos())
print(f"duracion maxima: {duracion_total}minutos")
class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def __str__(self):
        return f"Movie: {self.title} (Directed by {self.director}, {self.year})"

if __name__ == "__main__":
    titulo = input("Ingrese el título de la película: ")
    director = input("Ingrese el director: ")
    anio = input("Ingrese el año: ")

    mi_pelicula = Movie(titulo, director, anio)
    print(mi_pelicula)
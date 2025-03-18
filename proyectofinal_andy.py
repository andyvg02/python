class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"Libro '{self.titulo}' prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"Libro '{self.titulo}' devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible.")

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Estado: {estado}"

# Función para agregar un nuevo libro
def agregar_libro(biblioteca):
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    isbn = input("Ingrese el ISBN del libro: ")
    libro = Libro(titulo, autor, isbn)
    biblioteca.append(libro)
    print(f"Libro '{titulo}' agregado a la biblioteca.")

# Función para prestar un libro
def prestar_libro(biblioteca):
    isbn = input("Ingrese el ISBN del libro que desea prestar: ")
    for libro in biblioteca:
        if libro.isbn == isbn:
            libro.prestar()
            return
    print(f"No se encontró ningún libro con el ISBN {isbn}.")


# Función para devolver un libro
def devolver_libro(biblioteca):
    isbn = input("Ingrese el ISBN del libro que desea devolver: ")
    for libro in biblioteca:
        if libro.isbn == isbn:
            libro.devolver()
            return
    print(f"No se encontró ningún libro con el ISBN {isbn}.")

# Función para mostrar todos los libros
def mostrar_libros(biblioteca):
    if not biblioteca:
        print("No hay libros en la biblioteca.")
    else:
        print("Lista de libros en la biblioteca:")
        for libro in biblioteca:
            print(libro)

# Función para buscar un libro por ISBN
def buscar_libro(biblioteca):
    isbn = input("Ingrese el ISBN del libro que desea buscar: ")
    for libro in biblioteca:
        if libro.isbn == isbn:
            print(libro)  # Usa el método __str__ para mostrar los detalles
            return
    print(f"No se encontró ningún libro con el ISBN {isbn}.")



# Función principal del programa
def main():
    biblioteca = []  # Lista para almacenar los libros

    while True:
        print("\n--- Menú de Gestión de Biblioteca ---")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar libros")
        print("5. Buscar libro")
        print("6. Salir del programa")

        opcion = input("Elige una opción: ").strip().lower()

        if opcion == "1":
            agregar_libro(biblioteca)
        elif opcion == "2":
            prestar_libro(biblioteca)
        elif opcion == "3":
            devolver_libro(biblioteca)
        elif opcion == "4":
            mostrar_libros(biblioteca)
        elif opcion=="5":
            buscar_libro(biblioteca)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
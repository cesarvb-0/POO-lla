class Biblioteca:
    def __init__(self, autor, titulo, fecha, genero):
        self.autor = autor
        self.titulo = titulo
        self.fecha = fecha
        self.titulo = genero

def agregar_libro(clase, lista):
    autor = input("Ingrese autor: ")
    titulo = input("Ingrese título: ")
    fecha = input("Ingresar fecha: ")
    genero = input("Ingresar genero: ")
    libro_nuevo = clase(autor, titulo, fecha, genero)
    lista.append(libro_nuevo)

lista_libros = []
while True:
    print("Selecciones la opcion deseada")
    print("1. Registrar libro")
    print("2. Ver libros registrados")

    opcion = int(input(":"))

    if opcion == 1:
        agregar_libro(Biblioteca, lista_libros)


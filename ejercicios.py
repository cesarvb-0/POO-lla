class estudiante:
    def __init__(self, nombre, edad, n1, n2, n3):
        self.nombre = nombre
        self.edad = edad
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def mostrar_datos(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Nota 1: ", self.n1)
        print("Nota 2: ", self.n2)
        print("Nota 3: ", self.n3)

    def calcular_promedio(self):
        promedio = (self.n1 + self.n2 + self.n3) / 3

        return promedio
    

"""print("Bienvenido a notas y servicios")
nombre = input("Ingrese el nombre del Estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
n1 = float(input("Ingrese la primera nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercera nota: "))

estudianteF = estudiante(nombre, edad, n1, n2, n3)

promedio_estudiante = estudianteF.calcular_promedio()

print("El promedio del estudiante: ", estudianteF.nombre, "es de: ", promedio_estudiante)"""

print("Sistema de gestion de estudiantes")
lista_estudiantes = []
while True:
    print("\nSeleccione la opcion que desea: ")
    print("1. Agregar estudiante")
    print("2. Mostrar informacion de estudiantes")
    print("0. Salir")
    opcion = int(input("Ingrese el numero: "))

    if opcion == 1:
        nombreEstudiante = input("Ingrese el nombre del nuevo estudiante: ")
        edadEstudiante = input("Ingrese la edad del estudiante: ")
        nota1Estudiante = float(input("Ingrese la primera nota del estudiante: "))
        nota2Estudiante = float(input("Ingrese la segunda nota del estudiante: "))
        nota3Estudiante = float(input("Ingrese la tercera nota del estudiante: "))
        estudianteNuevo = estudiante(nombreEstudiante, edadEstudiante, nota1Estudiante, nota2Estudiante, nota3Estudiante)
        lista_estudiantes.append(estudianteNuevo)

    if opcion == 2:
        numeroEstudiantes = len(lista_estudiantes)
        print("\nEl numero de estudiantes es de: ", numeroEstudiantes)
        for estudianteNuevo in lista_estudiantes:
            print("El nombre del estudiante es: ", estudianteNuevo.nombre)
            print("El promedio del estudiante es de: ", estudianteNuevo.calcular_promedio())

    elif opcion == 0:
        print("\nChao pato")
        break
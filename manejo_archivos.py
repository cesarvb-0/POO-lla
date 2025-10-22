class Estudiante:
    def __init__(self, nombre, promedio):
        self.nombre = nombre
        self.promedio = promedio

    def aprobo(self):
        return self.promedio >= 3.0
    

class Curso:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print("Estudiante agregado exitosamente")
        with open(self.nombre_archivo, "a") as f:
            f.write(f'{estudiante.nombre}, {estudiante.promedio}\n')

    def guardar_archivo(self):
        try:
            with open(self.nombre_archivo, "w") as f:
                for e in self.estudiantes:
                    f.write(f'{e.nombre}, {e.promedio}\n')
            
            print("Estudiantes guardados exitosamente")

        except:
            print("Hubo un error al guardar los estudiantes")

    def mostrar_estudiante(self):
        for e in self.estudiantes:
            print(f'{e.nombre} tiene un promedio de {e.promedio}')

    def cargar_desde_archivo(self):
        self.estudiantes = []
        
        try:
            with open(self.nombre_archivo, "r") as f:
                for linea in f:
                    nombre , promedio = linea.strip().split(",")
                    estudiante = Estudiante(nombre, promedio)
                    self.estudiantes.append(estudiante)

        except:
            print("Hubo un error al cargar los estudiantes")


poo = Curso("Estudiantes.txt")
estudiante3 = Estudiante("Sexar", 2.2)
poo.agregar_estudiante(estudiante3)
poo.cargar_desde_archivo()
poo.mostrar_estudiante()
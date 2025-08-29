class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

class Profesor:
    def __init__(self, nombre, edad, experiencia):
        self.nombre = nombre
        self.edad = edad
        self.experiencia = experiencia

class GrupoAsignatura:
    def __init__(self, nombre, horario, codigo, profesor):
        self.nombre = nombre
        self.horario = horario
        self.codigo = codigo
        self.profesor = profesor
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print("Estudiante agregado exitosamente")

    def promedio(self):
        acumulador = 0
        for estudiante in self.estudiantes:
            acumulador += estudiante.nota
        promedio = acumulador/len(self.estudiantes)
        return promedio
    
    def mostrar_estudiantes (self):
        for estudiante in self.estudiantes:
            print(estudiante.nombre)


profesor = Profesor("Sebastian", 28, 18)
poo = GrupoAsignatura("Programacion Orientada a Objetos", "M-V 10-12", 62 ,profesor)
estudiante1 = Estudiante("Emmanuel", 18, 3.8)
estudiante2 = Estudiante("Tatiana", 20, 3.8)
estudiante3 = Estudiante("Nelson", 18, 5)

poo.agregar_estudiante(estudiante1)
poo.agregar_estudiante(estudiante2)
poo.agregar_estudiante(estudiante3)

print(poo.promedio())
poo.mostrar_estudiantes()
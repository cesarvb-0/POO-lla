class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

    def orinar(self):
        print(f'{self.nombre} está orinando')

class Perro(Animal):
    def hacer_sonido(self):
        print(f'{self.nombre} hace gua gua')

    def salir_a_pasear(self):
        print(f'{self.nombre} está paseando')

class Gato(Animal):
    def hacer_sonido(self):
        print(f'{self.nombre} hace miau')


"""animal = Perro("Mia")
animal.hacer_sonido()
animal.orinar()

animal1 = Gato("Milú")
animal1.hacer_sonido()

print(isinstance(animal, Perro))
print(isinstance(animal, Animal))"""

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def respirar(self):
        print(f'{self.nombre} está respirando')

class Estudiante(Persona):
    def __init__(self, nombre, carrera):
        super().__init__(nombre)
        self.carrera = carrera

    def estudiar(self):
        print(f'{self.nombre} está estudiando {self.carrera}')

persona1 = Persona("Juan")
persona1.respirar()

persona2 = Estudiante("Emmanuel", "Ingenieria de Sistemas")
persona2.estudiar()
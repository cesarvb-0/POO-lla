class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print("El perro que esta ladrando es: ", self.nombre)

class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

print("chirri")


mi_perro = Perro("Toby","San Bernardo")

print(f'El nombre de mi perro es {mi_perro.nombre} y es un {mi_perro.raza}')

tu_perro = Perro("Theo","Golden")

print(tu_perro.nombre)
print(tu_perro.raza)

otro_perro = Perro(input("Ingrese el nombre de su perro: "), input("Ingrese la raza de su perro: "))

print(otro_perro.nombre)
print(otro_perro.raza)

print("El perro que esta ladrando es: ")
mi_perro.ladrar()
tu_perro.ladrar()
otro_perro.ladrar()
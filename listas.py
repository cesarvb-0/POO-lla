import random
"""
listaRandom = []

for i in range(0, 10):
    listaRandom.append(random.randint(1,100))
print(listaRandom)

listaRandom2 = [random.randint(1,100) for _ in range (10)]
print(listaRandom2)"""

"""lista_ejemplo = [i for i in range(0,10)]

print(lista_ejemplo)

lista_ejemplo2 = [elemento for elemento in lista_ejemplo if elemento != 1]
print(lista_ejemplo2)

lista_ejemplo2.sort()
print(lista_ejemplo2)"""

class persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.numeros = [random.randint(100, 999) for _ in range(0,5)]

while True:
    print("Bienvenido a la loteria de Medellín")
    print("Ingrese su nick name: ")
    usuario = input("")
    nuevoUsuario = persona(usuario)

    print(f'Los numeros para {nuevoUsuario.nombre} son: {nuevoUsuario.numeros}')
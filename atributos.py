class Persona:
    def __init__(self, nombre, cedula, ti):
        self.nombre = nombre
        self.__cedula = cedula
        self.__ti = ti

    def obtener_cedula(self):
        if self.__cedula is not None:
            return self.__cedula
        else:
            return self.__ti

persona1 = Persona("Juan", 444, None)
persona2 = Persona("Maria", 111, None)
niño1 = Persona("Ismael", None, 333)

def print():
    print(f'El nombre de la primera persona es: {persona1.nombre} y su cedula es: {persona1.obtener_cedula()}')
    print(f'El nombre de la primera persona es: {persona2.nombre} y su cedula es: {persona2.obtener_cedula()}')
    print(f'El nombre de la primera persona es: {niño1.nombre} y su ti es: {niño1.obtener_cedula()}')



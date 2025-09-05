class Dispositivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = False

    def encender(self):
        self.estado = True
        print(self.nombre, "Encendido")

    def apagar(self):
        self.estado = False
        print(self.nombre, "Apagado")

class Espacio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__dispositivos = []

    def agregarD(self, dispositivo):
        self.__dispositivos.append(dispositivo)
        print("Dispositivo agregado")

    def mostrarD(self):
        for dispositivo in self.__dispositivos:
            print(dispositivo.nombre)

class Casa:
    def __init__(self, direccion):
        self.direccion = direccion
        self.__espacios = []
        
    def agregarE(self, nombre):
        self.__espacios.append(Espacio(nombre))
        print("Espacio agregado")

    def mostrarE(self):
        for espacio in self.__espacios:
            print(espacio.nombre)

    def buscarE(self, nombre):
        for espacio in self.__espacios:
            if espacio.nombre == nombre:
                return espacio
        return None


mi_casa = Casa("Calle 54 #81B - 26")
mi_casa.agregarE("Cocina")
mi_casa.agregarE("Habitacion")
mi_casa.agregarE("Baño")
television = Dispositivo("Television")
mi_casa.buscarE("Habitacion").agregarD(television)
mi_casa.buscarE("Habitacion").mostrarD()
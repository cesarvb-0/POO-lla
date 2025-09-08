class Motor:
    def __init__(self):
        self.estado = False

    def encender_motor(self):
        if self.estado:  
            print("El motor ya está encendido")
        else:
            self.estado = True
            print("El motor se ha encendido")
    
    def apagar_motor(self):
        if not self.estado:
            print("El motor ya está apagado")
        else:
            self.estado = False
            print("El motor se ha apagado")


class Vehiculo:
    def __init__(self, fabricante, tipo, placa, estado):
        self.fabricante = fabricante
        self.tipo = tipo
        self.placa = placa
        self.estado = estado
        self.motor = Motor()

class Flota:
    def __init__(self, nombre):
        self.nombre = nombre
        self.listaVehiculos = []

    def agregar_carro(self, vehiculo):
        if self.buscar_carro(vehiculo.placa) is not None:
            print("Error: ya existe un vehículo con esa placa")
            return
        self.listaVehiculos.append(vehiculo)
        print("El vehiculo ha sido agregado exitosamente")


    def eliminar_carro(self, placa):
        for i in self.listaVehiculos:
            if placa == i.placa:
                self.listaVehiculos.remove(i)
        print("El vehiculo fue eliminado exitosamente")

    def mostrar_carros(self):
        contador = 0
        for carro in self.listaVehiculos:
            contador += 1
            print(f'\nInformacion del carro {contador}: \nFabricante: {carro.fabricante} | Tipo: {carro.tipo} | Placa: {carro.placa} | Estado: {carro.estado}')
    
    def total_carros(self):
        print(f'El total de carros es: {len(self.listaVehiculos)}')

    def buscar_carro(self, placa):
        for carro in self.listaVehiculos:
            if carro.placa == placa:
                return carro
        return None


flota1 = Flota("RR autos")
carro1 = Vehiculo("Toyota", "pick up", 60, "En servicio")
carro2 = Vehiculo("Hyundai", "automovil", 10, "Fuera de servicio")
carro3 = Vehiculo("Koenigsegg", "hiperdeportivo", 99, "En servicio")

flota1.agregar_carro(carro1)
flota1.agregar_carro(carro2)
flota1.agregar_carro(carro3) 

print("\nBienvenido a la Flota!")
while True:
    print("\nSeleccione una opcion:")
    print("1. Agregar un vehiculo a la Flota")
    print("2. Eliminar un vehiculo de la flota")
    print("3. Mostrar vehiculos")
    print("4. Mostrar total vehiculos")
    print("5. Buscar vehiculo por placa")
    print("6. Encender motor de un vehiculo")
    print("7. Apagar motor de un vehiculo")
    print("0. Salir")
    opcion = int(input(": "))

    if opcion == 1: 
        fabricanteNuevo = input("Ingrese el fabricante del carro: ")
        tipoNuevo = input("Ingrese el tipo de vehiculo: ")
        placaNuevo = int(input("Ingrese la placa:  "))
        estadoNuevo = "En servicio"
        nuevoVehiculo = Vehiculo(fabricanteNuevo, tipoNuevo, placaNuevo, estadoNuevo)
        flota1.agregar_carro(nuevoVehiculo)
    
    elif opcion == 2:
        buscarPlaca = int(input("Ingrese la placa del vehiculo que desea eliminar: "))
        flota1.eliminar_carro(buscarPlaca)

    elif opcion == 3:
        flota1.mostrar_carros()
    
    elif opcion == 4:
        flota1.total_carros()
    
    elif opcion == 5: 
        buscarPlaca = int(input("Ingrese la placa del vehiculo que desea buscar: "))
        carro_encontrado = flota1.buscar_carro(buscarPlaca)
        if carro_encontrado is not None:
            print(f'Carro encontrado --> Fabricante: {carro_encontrado.fabricante}, Tipo: {carro_encontrado.tipo}, Estado: {carro_encontrado.estado}')
        else:
            print(f'Carro no encontrado')

    elif opcion == 6:
        buscarPlaca = int(input("Ingrese la placa del vehiculo que desea encender: "))
        carro_encontrado = flota1.buscar_carro(buscarPlaca)
        if carro_encontrado is not None:
            carro_encontrado.motor.encender_motor()
        else:
            print(f'Carro no encontrado')

    elif opcion == 7:
        buscarPlaca = int(input("Ingrese la placa del vehiculo que desea apagar: "))
        carro_encontrado = flota1.buscar_carro(buscarPlaca)
        if carro_encontrado is not None:
            carro_encontrado.motor.apagar_motor()
        else:
            print(f'Carro no encontrado')

    elif opcion == 0:
        print("Hasta luego")

    else:
        print("Ingrese una opción válida")

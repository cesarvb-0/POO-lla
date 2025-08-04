"""class estudiante:
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

        return promedio"""
    

"""print("Bienvenido a notas y servicios")
nombre = input("Ingrese el nombre del Estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
n1 = float(input("Ingrese la primera nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercera nota: "))

estudianteF = estudiante(nombre, edad, n1, n2, n3)

promedio_estudiante = estudianteF.calcular_promedio()

print("El promedio del estudiante: ", estudianteF.nombre, "es de: ", promedio_estudiante)"""

"""print("Sistema de gestion de estudiantes")
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
        break"""

class productos:
    def __init__(self, nombre, precio, cantidadDisponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidadDisponible = cantidadDisponible

lista_productos = [productos("Pan", 1000, 10),
                   productos("Agua", 1500, 5),
                   productos("Leche", 2000, 8)]

def ejercicio2():
    print("Bienvenido a la tienda")
    while True:
        print("\nOpciones disponibles: ")
        print("1. Añadir producto.")
        print("2. Ver productos disponibles.")
        print("3. Comprar producto.")
        print("0. Salir")

        opcion = int(input("Ingrese la opcion deseada: "))
        
        if opcion == 1:
            nombreProducto = input("Ingrese el nombre del produco nuevo: ")
            precioProducto = int(input("Ingrese el precio del producto nuevo: "))
            cantidadProducto = int(input("Ingrese la cantidad que registra: "))
            productoNuevo = productos(nombreProducto, precioProducto, cantidadProducto)
            lista_productos.append(productoNuevo)

        elif opcion == 2:
            for producto in lista_productos:
                print("\nNombre Producto: ", producto.nombre)
                print("Precio Producto: ",producto.precio)
                print("Cantidad disponible: ", producto.cantidadDisponible)
                print("-" * 30)

        elif opcion == 3:
            nombre_buscar = input("Ingrese el nombre del producto que desea comprar: ")

            encontrado = False
            for producto in lista_productos:
                if producto.nombre.lower() == nombre_buscar.lower():
                    encontrado = True
                    cantidad_deseada = int(input(f'Ingrese la cantidad de {producto.nombre} que desea comprar: '))
                    if cantidad_deseada <= producto.cantidadDisponible:
                        producto.cantidadDisponible -= cantidad_deseada
                        total = producto.precio * cantidad_deseada
                        print(f'Compra exitosa. Total a pagar: ${total}')
                        print(f'Unidades restantes de {producto.nombre}: {producto.cantidadDisponible}')
                    else:
                        print("No hay suficientes unidades disponibles.")
                    break
            
            if not encontrado:
                print("Producto no encontrado.")

        elif opcion == 0:
            print("Gracias por visitar la tienda. ¡Hasta pronto!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

class Banco:
    def __init__(self, numeroCuenta, titular, saldo):
        self.numeroCuenta = numeroCuenta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        print(f'Depósito exitoso. Nuevo saldo: ${self.saldo}')

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f'Retiro exitoso. Saldo restante: ${self.saldo}')
        else:
            print("Fondos insuficientes.")

    def consultar_saldo(self):
        print(f'Saldo actual: ${self.saldo}')

def ejercicio3():
    print("Bienvenido al sistema bancario ")
    numero = input("Ingrese su número de cuenta: ")
    titular = input("Ingrese el nombre del titular: ")
    saldo_inicial = float(input("Ingrese el saldo inicial: "))
    cuenta = Banco(numero, titular, saldo_inicial)

    while True:
        print("\nSeleccione una opción:")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Consultar saldo")
        print("0. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            monto = float(input("Ingrese el monto a depositar: "))
            cuenta.depositar(monto)

        elif opcion == "2":
            monto = float(input("Ingrese el monto a retirar: "))
            cuenta.retirar(monto)

        elif opcion == "3":
            cuenta.consultar_saldo()

        elif opcion == "0":
            print("Gracias por usar el sistema bancario.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


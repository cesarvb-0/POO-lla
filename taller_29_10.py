from dataclasses import dataclass, field
from typing import List
from abc import ABC, abstractmethod

@dataclass
class Transporte:
    tipo: str
    placa: int
    marca: str
    color: str
    valor: int
    

    @abstractmethod
    def calcular_impuesto(self):
        ...
class Auto(Transporte):
    def calcular_impuesto(self):
        return self.valor * 0.10 + self.valor
    
class Camion(Transporte):
    def calcular_impuesto(self):
        return self.valor * 0.10 + self.valor
    
class Moto(Transporte):
    def calcular_impuesto(self):
        return self.valor * 0.10 + self.valor

class Empresa:
    nombreArchivo: str
    listaVehiculo: List

    def agergar_vehiculo(self, v):
        self.listaVehiculo.append(v)
        print(f'El vehiculo {v.placa} ha sido agregado exitosamente.')
        with open(self.nombreArchivo, "a") as f:
            f.write(f'{v.tipo}, {v.placa}, {v.marca}, {v.color}, {v.valor}')


    def guardar_en_archivo(self):
        try:
            with open (self.nombreArchivo, "w") as f:
                for v in self.listaVehiculo:
                    f.write(f'{v.tipo}, {v.placa}, {v.marca}, {v.color}, {v.valor}')
            print("Vehiculo agregado correctamente")
        except:
            print("Hubo un error al guardar")
    
    def cargar_vehiculos(self):
        self.listaVehiculo = []
        
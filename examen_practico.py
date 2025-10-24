from dataclasses import dataclass, field
from typing import List

@dataclass
class LineaPedido:
    descripcion: str
    cantidad: int
    pesoUnitario: float

    def calcular_total(self):
        return 0.0

@dataclass
class Pedido(LineaPedido):

    def calcular_total_items(self):
        totalItems = 0
        
    
@dataclass
class Transporte:
    capacidad: float
    velocidad: float
    costoBase: float = field(default = 5000)

    def calcular_tiempo(distancia_km):
        return 0.0
    
    def calcular_costo(distancia_km, peso_kg):
        return 0.0
    
class Bicicleta(Transporte):
    maximo: float = field(default = 15)
    costo: float

    def calcular_tiempo(distancia_km, velocidad):
        tiempo_entrega = distancia_km / velocidad
        return tiempo_entrega
    
    def calcular_costo(self, distancia_km):
        costo = self.costoBase + 0.20 * distancia_km
        return costo
    
class Moto(Transporte):
    maximo: float = field(default = 50)
    costo: float

    def calcular_tiempo(distancia_km, velocidad):
        tiempo_entrega = distancia_km / velocidad
        return tiempo_entrega
    
    def calcular_costo(self, distancia_km, peso_kg):
        costo = self.costoBase + 0.60 * distancia_km + 0.05 * peso_kg
        return costo
    
class Furgoneta(Transporte):
    maximo: float
    costo: float

    def calcular_tiempo(distancia_km, velocidad):
        tiempo_entrega = distancia_km / velocidad
        return tiempo_entrega
    
    def calcular_costo(self, distancia_km, peso_kg):
        costo = self.costoBase + 1.20 * distancia_km + 0.10 * peso_kg
        return costo
    
class GestorDeEnvios:
    transportes_disponibles: list = field(default=["Bicicleta","Moto","Furgoneta","cualquiera","mas_barato"])


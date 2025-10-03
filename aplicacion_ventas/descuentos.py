from abc import ABC, abstractmethod
from typing import List
from modelos import Cliente, LineaFactura

class Descuento(ABC):
    @abstractmethod
    def aplicar(self, cliente: Cliente, linea: LineaFactura) -> float:
        ...

class SinDescuento(Descuento):
    def aplicar(self, cliente: Cliente, linea: LineaFactura) -> float:
        return 0.0
    
class DescuentoVIP(Descuento):
    def aplicar(self, cliente: Cliente, linea: LineaFactura) -> float:
        return 0.10 * linea.subtotal if cliente.vip else 0.0 
    
class DescuentoVolumen(Descuento):
    def aplicar(self, cliente: Cliente, linea: LineaFactura) -> float:
        return 0.15 * linea.subtotal if linea.cantidad >= 10 else 0.0
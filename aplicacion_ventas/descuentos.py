from abc import ABC, abstractmethod
from typing import List
from modelos import Cliente, LineaFactura
from excepciones import DescuentosError

class Descuento(ABC):
    @abstractmethod
    def aplicar(self, cliente: Cliente, linea: LineaFactura) -> float:
        ...

class SinDescuento(Descuento):
    def aplicar(self, cliente: Cliente, linea: LineaFactura) -> float:
        return 0.0

class DescuentoVIP(Descuento):
    def aplicar(self, cliente: Cliente, linea: LineaFactura) -> float:
          
        return 0.10 * linea.subtotal if cliente.vip == True else 0.0
    
class DescuentoVolumen(Descuento):
    def aplicar(self, cliente: Cliente, linea: LineaFactura) -> float:
        return 0.15 * linea.subtotal if linea.cantidad >= 10 else 0.0

class DescuentoValor(Descuento):
    def aplicar(self, cliente: Cliente, linea: LineaFactura) -> float:
        return 0.05 * linea.subtotal if linea.subtotal >= 200000 else 0.0

class DescuentoCompuesto(Descuento):

    def __init__(self, *estrategias: Descuento):
        self.estrategias = list(estrategias)

    def aplicar(self, cliente: Cliente, linea: LineaFactura) -> float:
        return sum(e.aplicar(cliente, linea) for e in self.estrategias)
    
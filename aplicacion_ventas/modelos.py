from dataclasses import dataclass, field
from typing import List, ClassVar, Set
from excepciones import ProductosError, ClientesError

@dataclass
class Producto:
    codigo: int
    nombre: str
    categoria: str
    precio: float 

    CATEGORIAS_PERMITIDAS: ClassVar[Set[str]] = {"alimentos", "servicios", "tecnología"}

    def __post_init__(self) -> None:
        try:
            prueba = float(self.precio)
        except:
            raise ProductosError("Error en el precio del producto")
        if prueba < 0:
            raise ProductosError("El precio del producto no puede ser negativo")

        self.categoria = self.categoria.lower()

        if self.categoria not in self.CATEGORIAS_PERMITIDAS:
            raise ProductosError(
                f"Categoría no permitida: {self.categoria}. "
                f"Categorías permitidas: {self.CATEGORIAS_PERMITIDAS}")

@dataclass
class Cliente:
    id: int
    nombre: str
    vip: bool

    def __post_init__(self) -> None:
        try:
            prueba = int(self.id)
        except:
            raise ClientesError("Error en la identificación del cliente. Debe ser un número entero")

@dataclass
class LineaFactura:
    producto: Producto
    cantidad: int 

    @property
    def subtotal(self) -> float:

        return self.producto.precio * self.cantidad
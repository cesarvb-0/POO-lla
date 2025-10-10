import pytest
from modelos import Producto, Cliente, LineaFactura
from excepciones import ProductosError, ClientesError

def test_producto_cree_correctamente():
    p = Producto(1, "Manzana", "Alimentos", 2500)
    assert p.codigo == 1
    assert p.nombre == "Manzana"
    assert p.categoria == "alimentos"

@pytest.mark.parametrize("precio", [-2500, -5000.50])
def test_producto_precio_negativo(precio):
    with pytest.raises(ProductosError) as exc:
        Producto(1, "Manzana", "Alimentos", precio)
    assert "no puede ser negativo" in str(exc.value).lower()

@pytest.mark.parametrize("precio", ["cinco mil", object(), None])
def test_producto_precio_no_numerico(precio):
    with pytest.raises(ProductosError) as exc:
        Producto(1, "Manzana", "Alimentos", precio)
    assert "Error en el precio del producto" in str(exc.value)

def test_producto_categoria_no_permitida():
    with pytest.raises(ProductosError) as exc:
        Producto(1, "Manzana", "Mascotas", 2500)
    assert "Categoría no permitida" in str(exc.value)

def test_producto_categoria_a_minuscula():
    p = Producto(1, "Manzana", "ALiMenTOs", 2500)
    assert p.categoria == "alimentos"

def test_cliente_valido():
    c = Cliente(123, "Juan", True)
    assert c.id == 123
    assert c.nombre == "Juan"
    assert c.vip == True

@pytest.mark.parametrize("valor", ["uno", None, object()])
def test_cliente_id_numerico(valor):
    with pytest.raises(ClientesError) as exc:
        Cliente(valor, "Juan", False)
    assert "Error en la identificacion del cliente. Debe ser un número entero"

def test_linea_factura_subtotal_cero():
    p = Producto(10, "Pan", "alimentos", 1500)
    linea = LineaFactura(p, 0)
    assert linea.subtotal == 0
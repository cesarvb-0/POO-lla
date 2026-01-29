#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

EMPLEADOS = ["César", "Simón", "Sebas", "Juanjo", "Jero"]

# Precios actualizados (solo +5k a automovil/suv/camioneta; moto igual)
PRECIOS = {
    "moto": 20000,
    "automovil": 35000,
    "suv": 40000,
    "camioneta": 45000
}

# Porcentajes (en enteros para no usar floats)
PORC_CAJA = 10          # 10% del base a caja
PORC_FIJO = 10          # 10% del base a cada empleado (5 empleados)
PORC_POOL = 40          # 40% del base a lavadores + 100% propina


def formatear_pesos(x: int) -> str:
    return f"${x:,}".replace(",", ".")


def pedir_opcion_menu():
    print("\n" + "=" * 50)
    print("        LIQUIDACIÓN - LAVADERO (Consola)")
    print("=" * 50)
    print("1) Agregar vehículo lavado")
    print("2) Ver liquidación actual")
    print("3) Ver detalle de vehículos ingresados")
    print("0) Salir")
    return input("Elige una opción: ").strip()


def pedir_entero(mensaje, minimo=None):
    while True:
        raw = input(mensaje).strip().replace(".", "").replace(",", "")
        if raw == "":
            raw = "0"
        try:
            n = int(raw)
            if minimo is not None and n < minimo:
                print(f"❌ Debe ser >= {minimo}.")
                continue
            return n
        except ValueError:
            print("❌ Ingresa un número válido (ej: 60000).")


def pedir_tipo_vehiculo():
    print("\nTipos disponibles y precios:")
    for k, v in PRECIOS.items():
        print(f" - {k.title():<10} : {formatear_pesos(v)}")
    print(" - Personalizado : (tú defines el precio)")

    while True:
        t = input("\nTipo (moto/automovil/suv/camioneta/personalizado): ").strip().lower()
        if t in PRECIOS:
            return t, PRECIOS[t], t.title()
        if t in ["personalizado", "otro", "especial", "no comun", "nocomun"]:
            nombre = input("Nombre/Descripción (ej: Camión, Full Size): ").strip()
            if not nombre:
                nombre = "Personalizado"
            precio = pedir_entero("Precio base de este servicio: ", minimo=0)
            return "personalizado", precio, nombre
        print("❌ Tipo inválido. Intenta de nuevo.")


def pedir_lavadores():
    print("\nEmpleados:")
    for i, e in enumerate(EMPLEADOS, start=1):
        print(f" {i}) {e}")

    print("\nEscribe los números de quienes lavaron, separados por coma.")
    print("Ejemplo: 2,3,1")

    while True:
        raw = input("Lavadores: ").strip()
        if not raw:
            print("❌ Debes ingresar al menos 1 lavador.")
            continue

        try:
            partes = [p.strip() for p in raw.split(",")]
            idxs = []
            for p in partes:
                if not p:
                    continue
                i = int(p)
                if i < 1 or i > len(EMPLEADOS):
                    raise ValueError
                idxs.append(i - 1)

            # Quitar duplicados respetando el orden
            vistos = set()
            idxs_unicos = []
            for i in idxs:
                if i not in vistos:
                    vistos.add(i)
                    idxs_unicos.append(i)

            if len(idxs_unicos) == 0:
                print("❌ Debes seleccionar al menos 1 lavador.")
                continue

            return idxs_unicos

        except ValueError:
            print("❌ Formato inválido. Usa números separados por coma. Ej: 1,3,5")


def repartir_pool(pool: int, indices_lavadores: list[int]) -> dict[int, int]:
    """
    Reparte 'pool' en pesos enteros entre los lavadores.
    Si no divide exacto, reparte el residuo de a 1 peso a los primeros.
    """
    n = len(indices_lavadores)
    base = pool // n
    residuo = pool % n

    reparto = {}
    for pos, idx in enumerate(indices_lavadores):
        extra = 1 if pos < residuo else 0
        reparto[idx] = base + extra
    return reparto


def ver_liquidacion(caja_total, totales_fijos, totales_variables):
    print("\n" + "-" * 50)
    print("LIQUIDACIÓN ACTUAL")
    print("-" * 50)
    print(f"Caja acumulada: {formatear_pesos(caja_total)}\n")

    print("Por empleado:")
    gran_total_empleados = 0
    for i, e in enumerate(EMPLEADOS):
        fijo = totales_fijos[i]
        var = totales_variables[i]
        total = fijo + var
        gran_total_empleados += total
        print(
            f" - {e:<7} | Fijo: {formatear_pesos(fijo):>10} "
            f"| Variable: {formatear_pesos(var):>10} "
            f"| Total: {formatear_pesos(total):>10}"
        )

    print("\nResumen:")
    print(f"Total pagado a empleados: {formatear_pesos(gran_total_empleados)}")
    print(f"Total caja:              {formatear_pesos(caja_total)}")
    print("-" * 50)


def ver_detalle_vehiculos(registros):
    if not registros:
        print("\n(No hay vehículos ingresados todavía.)")
        return

    print("\n" + "-" * 70)
    print("DETALLE DE VEHÍCULOS")
    print("-" * 70)
    for n, r in enumerate(registros, start=1):
        lavadores = ", ".join(r["lavadores"])
        print(
            f"{n:>2}. {r['fecha']} | {r['nombre_tipo']:<14} "
            f"Base {formatear_pesos(r['base']):>9} | "
            f"Propina {formatear_pesos(r['propina']):>9} | "
            f"Caja {formatear_pesos(r['caja']):>8} | "
            f"Pool {formatear_pesos(r['pool']):>9} | "
            f"Lavaron: {lavadores}"
        )
    print("-" * 70)


def main():
    caja_total = 0
    totales_fijos = [0] * len(EMPLEADOS)
    totales_variables = [0] * len(EMPLEADOS)
    registros = []

    while True:
        op = pedir_opcion_menu()

        if op == "1":
            tipo_key, base, nombre_tipo = pedir_tipo_vehiculo()
            propina = pedir_entero("Propina (0 si no hubo): ", minimo=0)
            indices_lavadores = pedir_lavadores()

            # Cálculos 100% enteros
            caja = base * PORC_CAJA // 100
            fijo_por_empleado = base * PORC_FIJO // 100
            pool = (base * PORC_POOL // 100) + propina

            # Actualizar caja y fijos
            caja_total += caja
            for i in range(len(EMPLEADOS)):
                totales_fijos[i] += fijo_por_empleado

            # Reparto variable
            reparto = repartir_pool(pool, indices_lavadores)
            for idx, monto in reparto.items():
                totales_variables[idx] += monto

            # Guardar registro
            registros.append({
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "tipo": tipo_key,
                "nombre_tipo": nombre_tipo,
                "base": base,
                "propina": propina,
                "caja": caja,
                "fijo_cada_empleado": fijo_por_empleado,
                "pool": pool,
                "lavadores": [EMPLEADOS[i] for i in indices_lavadores],
                "reparto_pool": {EMPLEADOS[i]: reparto[i] for i in reparto}
            })

            # Resumen del vehículo
            print("\n✅ Vehículo agregado:")
            print(f" - Tipo: {nombre_tipo} | Base: {formatear_pesos(base)} | Propina: {formatear_pesos(propina)}")
            print(f" - Caja (10% base): {formatear_pesos(caja)}")
            print(f" - Fijo (10% base) para cada empleado: {formatear_pesos(fijo_por_empleado)}")
            print(f" - Pool (40% base + propina): {formatear_pesos(pool)}")
            print(" - Reparto del pool entre lavadores:")
            for nombre, monto in registros[-1]["reparto_pool"].items():
                print(f"    * {nombre}: {formatear_pesos(monto)}")

        elif op == "2":
            ver_liquidacion(caja_total, totales_fijos, totales_variables)

        elif op == "3":
            ver_detalle_vehiculos(registros)

        elif op == "0":
            print("\n👋 Saliendo. Liquidación final:")
            ver_liquidacion(caja_total, totales_fijos, totales_variables)
            break

        else:
            print("❌ Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

EMPLEADOS = ["César", "Simón", "Sebas", "Juanjo", "Jero"]

PRECIOS = {
    "moto": 20000,
    "automovil": 30000,
    "suv": 35000,
    "camioneta": 40000
}

PORC_CAJA = 0.10
PORC_FIJO_EMPLEADO = 0.10  # a cada empleado (son 5)
PORC_POOL_LAVADORES = 0.40  # del base; la propina se suma completa al pool


def pedir_opcion_menu():
    print("\n" + "=" * 45)
    print("      LIQUIDACIÓN - LAVADERO (Consola)")
    print("=" * 45)
    print("1) Agregar vehículo lavado")
    print("2) Ver liquidación actual")
    print("3) Ver detalle de vehículos ingresados")
    print("0) Salir")
    return input("Elige una opción: ").strip()


def pedir_tipo_vehiculo():
    print("\nTipos disponibles y precios:")
    for k, v in PRECIOS.items():
        print(f" - {k.title():<10} : ${v:,}".replace(",", "."))

    while True:
        t = input("Tipo de vehículo (moto/automovil/suv/camioneta): ").strip().lower()
        if t in PRECIOS:
            return t
        print("❌ Tipo inválido. Intenta de nuevo.")


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


def pedir_lavadores():
    print("\nEmpleados:")
    for i, e in enumerate(EMPLEADOS, start=1):
        print(f" {i}) {e}")

    print("\nEscribe los números de quienes lavaron el vehículo, separados por coma.")
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

            # Quitar duplicados respetando orden
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


def repartir_pool(pool, indices_lavadores):
    """
    Reparte 'pool' en pesos enteros entre los lavadores.
    Si no divide exacto, reparte el residuo de a 1 peso a los primeros.
    Retorna dict {indice_empleado: monto}
    """
    n = len(indices_lavadores)
    base = pool // n
    residuo = pool % n

    reparto = {}
    for pos, idx in enumerate(indices_lavadores):
        extra = 1 if pos < residuo else 0
        reparto[idx] = base + extra
    return reparto


def formatear_pesos(x):
    return f"${x:,}".replace(",", ".")


def ver_liquidacion(caja_total, totales_fijos, totales_variables):
    print("\n" + "-" * 45)
    print("LIQUIDACIÓN ACTUAL")
    print("-" * 45)
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
    print("-" * 45)


def ver_detalle_vehiculos(registros):
    if not registros:
        print("\n(No hay vehículos ingresados todavía.)")
        return

    print("\n" + "-" * 60)
    print("DETALLE DE VEHÍCULOS")
    print("-" * 60)
    for n, r in enumerate(registros, start=1):
        lavadores = ", ".join(r["lavadores"])
        print(
            f"{n:>2}. {r['fecha']} | {r['tipo'].title():<10} "
            f"Base {formatear_pesos(r['base']):>9} | "
            f"Propina {formatear_pesos(r['propina']):>9} | "
            f" Caja {formatear_pesos(r['caja']):>8} | "
            f" Pool {formatear_pesos(r['pool']):>9} | "
            f"Lavaron: {lavadores}"
        )
    print("-" * 60)


def main():
    # Totales acumulados
    caja_total = 0
    totales_fijos = [0] * len(EMPLEADOS)
    totales_variables = [0] * len(EMPLEADOS)

    # Para auditoría/detalle
    registros = []

    while True:
        op = pedir_opcion_menu()

        if op == "1":
            tipo = pedir_tipo_vehiculo()
            base = PRECIOS[tipo]

            propina = pedir_entero("Propina (0 si no hubo): ", minimo=0)
            indices_lavadores = pedir_lavadores()

            # Cálculos
            caja = int(round(base * PORC_CAJA))
            fijo_por_empleado = int(round(base * PORC_FIJO_EMPLEADO))
            pool = int(round(base * PORC_POOL_LAVADORES)) + propina

            # Actualizar caja
            caja_total += caja

            # Fijo para todos
            for i in range(len(EMPLEADOS)):
                totales_fijos[i] += fijo_por_empleado

            # Reparto del pool entre lavadores
            reparto = repartir_pool(pool, indices_lavadores)
            for idx, monto in reparto.items():
                totales_variables[idx] += monto

            # Guardar registro
            registros.append({
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "tipo": tipo,
                "base": base,
                "propina": propina,
                "caja": caja,
                "fijo_cada_empleado": fijo_por_empleado,
                "pool": pool,
                "lavadores": [EMPLEADOS[i] for i in indices_lavadores],
                "reparto_pool": {EMPLEADOS[i]: reparto[i] for i in reparto}
            })

            # Resumen de este vehículo
            print("\n✅ Vehículo agregado:")
            print(f" - Tipo: {tipo.title()} | Base: {formatear_pesos(base)} | Propina: {formatear_pesos(propina)}")
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

from logic.taller import Taller
import time


def main():
    print("🔧 Creando taller...\n")
    taller = Taller()

    print("📥 Llegan autos al taller:")
    autos_que_llegan = [
        ("Sedán", 5),
        ("Deportivo", 3),
        ("Camioneta", 7),
        ("Compacto", 2),
    ]

    for modelo, tiempo in autos_que_llegan:
        ok = taller.agregar_auto(modelo, tiempo)
        estado = "✅ Agregado" if ok else "❌ Cola llena"
        print(f"  {estado} {modelo} ({tiempo}s)")

    print("\n⏱️  Simulando paso del tiempo:\n")

    for segundo in range(1, 25):
        taller.tick()
        estado = taller.obtener_estado()
        mecanico = estado["mecanico"]
        cola = estado["cola"]

        if mecanico["estado"] == "reparando":
            info_mecanico = (
                f"Mecánico reparando {mecanico['auto_actual']['modelo']} "
                f"({mecanico['tiempo_restante']}s restantes)"
            )
        else:
            info_mecanico = "Mecánico libre"

        print(f"Segundo {segundo:2d}: {info_mecanico:<45} | {len(cola)} autos en cola")

        # Si ya no hay nada que hacer, terminamos
        if mecanico["estado"] == "libre" and len(cola) == 0:
            break

        time.sleep(0.1)

    print("\n✅ Simulación terminada")


if __name__ == "__main__":
    main()
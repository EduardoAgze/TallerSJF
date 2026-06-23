from logic.auto import Auto
from logic.min_heap import MinHeap
from logic.mecanico import Mecanico


class Taller:
    """
    Coordina al Mecánico con la cola de autos (MinHeap).
    - Cuando el mecánico está libre y hay autos esperando,
      automáticamente toma el siguiente del heap.
    - Cada segundo, descuenta el tiempo de reparación.
    - Sabe devolver su estado completo en formato diccionario.
    """

    def __init__(self):
        self.cola = MinHeap()  # Sin parámetro - usa MAX = 10 interno
        self.mecanico = Mecanico("Juan")

    def agregar_auto(self, modelo, tiempo_reparacion):
        """
        Crea un Auto y lo intenta meter en la cola.
        Devuelve True si entró, False si la cola estaba llena.
        """
        auto = Auto(modelo, tiempo_reparacion)
        return self.cola.insertar(auto)

    def tick(self):
        """
        Avanza el tiempo 1 segundo:
        1. Si el mecánico está libre y hay autos en cola,
           le entrega el siguiente.
        2. Le pide al mecánico que descuente 1 segundo.
        """
        if self.mecanico.esta_libre() and not self.cola.esta_vacio():
            siguiente_auto = self.cola.extraer_min()
            self.mecanico.tomar_auto(siguiente_auto)

        self.mecanico.tick()

    def obtener_estado(self):
        """
        Devuelve un diccionario con:
        - El estado del mecánico
        - La lista de autos en la cola
        Listo para convertir a JSON y mandarlo al navegador.
        """
        return {
            "mecanico": self.mecanico.to_dict(),
            "cola": [auto.to_dict() for auto in self.cola.obtener_autos()]
        }
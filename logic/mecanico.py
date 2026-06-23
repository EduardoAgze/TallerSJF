LIBRE = "libre"
REPARANDO = "reparando"

class Mecanico:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.estado = LIBRE
        self.auto_actual = None
        self.tiempo_restante = 0

    def tomar_auto(self, auto):
        if auto is None or self.estado != LIBRE:
            return
        self.auto_actual = auto
        self.tiempo_restante = auto.tiempo_reparacion
        self.estado = REPARANDO

    def tick(self):
        if self.estado == REPARANDO:
            self.tiempo_restante -= 1
            if self.tiempo_restante <= 0:
                self.auto_actual = None
                self.estado = LIBRE

    def esta_libre(self):
        return self.estado == LIBRE

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "estado": self.estado,
            "auto_actual": self.auto_actual.to_dict() if self.auto_actual else None,
            "tiempo_restante": self.tiempo_restante
        }
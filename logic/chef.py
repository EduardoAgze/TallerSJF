# Módulo con la lógica del cocinero (Chef).


ESPERANDO = "esperando"
COCINANDO = "cocinando"


class Chef:
    """Representa a un cocinero que procesa pedidos.

    Atributos:
        nombre (str): nombre identificador del chef.
        estado (str): estado actual, uno de ESPERANDO o COCINANDO.
        pedido_actual: objeto "Cliente" que se está cocinando o None.
        tiempo_restante (int): segundos restantes para completar el pedido.
    """

    def __init__(self, nombre: str):
        """Inicializa un cocinero en estado de espera.

        Args:
            nombre (str): nombre del cocinero.
        """
        self.nombre = nombre
        self.estado = ESPERANDO
        self.pedido_actual = None
        self.tiempo_restante = 0

    def tomar_pedido(self, cliente):
        """Asigna un pedido al cocinero si está libre.

        Si cliente es None o el chef no está en estado ESPERANDO, no hace nada.
        """
        if cliente is None or self.estado != ESPERANDO:
            return
        # Asociar el pedido y fijar el tiempo de cocinado
        self.pedido_actual = cliente
        self.tiempo_restante = cliente.tiempo
        self.estado = COCINANDO

    def tick(self):
        """Simula el paso de un segundo en la cocina.

        Decrementa el tiempo restante y marca el pedido como listo cuando
        el tiempo llega a cero o menos.
        """
        if self.estado == COCINANDO:
            self.tiempo_restante -= 1
            if self.tiempo_restante <= 0:
                # Aviso de pedido completado y restauración del estado
                print(f"✓ {self.pedido_actual.platillo} listo!")
                self.pedido_actual = None
                self.estado = ESPERANDO

    def esta_libre(self):
        """Devuelve True si el cocinero está esperando un pedido."""
        return self.estado == ESPERANDO

    def __str__(self):
        """Representación en cadena del estado del cocinero."""
        if self.estado == ESPERANDO:
            return f"{self.nombre}: esperando"
        return (
            f"{self.nombre}: cocinando {self.pedido_actual} — "
            f"{self.tiempo_restante}s restantes"
        )
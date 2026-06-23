class Auto:
    #Representa un auto para la cola de reparación.
    

    _contador = 0  # cuenta cuántos autos se han creado y nos sirve para asignar un orden único a cada auto.

    def __init__(self, modelo: str, tiempo_reparacion: int):
        """Inicializa un Auto.
        Args:
            modelo (str): nombre o modelo del vehículo.
            tiempo_reparacion (int): tiempo necesario para reparar (segundos).
        """
        self.modelo = modelo
        self.tiempo_reparacion = tiempo_reparacion
        # orden asignado según el contador de clase (preserva llegada)
        self.orden = Auto._contador
        Auto._contador += 1



    def __lt__(self, otro):
        """Comparador menor que para ordenar por tiempo de reparación.

        Si hay empate en tiempo, gana el que llegó primero (menor orden).
        """
        if self.tiempo_reparacion == otro.tiempo_reparacion:
            return self.orden < otro.orden
        return self.tiempo_reparacion < otro.tiempo_reparacion



    def __str__(self):
        #Representación legible del Auto.
        return f"{self.modelo} ({self.tiempo_reparacion}s)"





    def to_dict(self):
        """Convierte el Auto a un diccionario JSON-serializable.

        Devuelve:
            dict: Diccionario con las propiedades del Auto.
        """
        return {
            "modelo": self.modelo,
            "tiempo_reparacion": self.tiempo_reparacion,
        }
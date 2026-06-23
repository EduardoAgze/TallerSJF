class Cliente:
    _contador = 0   # cuenta cuántos clientes se han creado

    def __init__(self, platillo: str, tiempo: int):
        self.platillo = platillo
        self.tiempo = tiempo
        self.orden = Cliente._contador   # guarda en qué orden llegó
        Cliente._contador += 1

    def __lt__(self, otro):
        if self.tiempo == otro.tiempo:
            return self.orden < otro.orden   # empate: gana quien llegó primero
        return self.tiempo < otro.tiempo

    def __str__(self):
        return f"{self.platillo} ({self.tiempo}s)"
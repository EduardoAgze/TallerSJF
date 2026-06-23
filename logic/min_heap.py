class MinHeap:
    # Montículo mínimo con capacidad limitada.

    MAX = 10  # límite de autos en cola

    def __init__(self):
        """Inicializa una nueva instancia de MinHeap.

        Se crea una lista donde se almacenarán los elementos del montículo.
        """

        self._data = []

    """
    esta_vacio: Devuelve True si el montículo está vacío, False en caso contrario.
    obtener_autos: Devuelve una lista de los autos en el montículo.
    
    """
    def esta_vacio(self):
        return len(self._data) == 0
    
    def obtener_autos(self):
        return list(self._data)



    def insertar(self, auto):
        """Inserta un elemento en el montículo.

        Parámetros:
            auto: Valor a insertar de la clase Auto.

        Devuelve:
            bool: True si la inserción tuvo éxito; False si se alcanzó
            la capacidad máxima (MAX).
        """

        if len(self._data) >= self.MAX:
            return False

        self._data.append(auto)
        self._flotar(len(self._data) - 1)
        return True



    def extraer_min(self):
        """Extrae y devuelve el elemento mínimo del montículo.

        Devuelve None si el montículo está vacío.
        """

        if self.esta_vacio():
            return None

        if len(self._data) == 1:
            return self._data.pop()

        minimo = self._data[0]
        # Mover el último elemento a la raíz y reordenar.
        self._data[0] = self._data.pop()
        self._sumergir(0)
        return minimo





    
    def _flotar(self, i):
        """Reordena hacia arriba (flotar) desde el índice i para mantener
        la propiedad de montículo mínimo.
        """

        while i > 0:
            padre = (i - 1) // 2
            if self._data[i] < self._data[padre]:
                self._data[i], self._data[padre] = (
                    self._data[padre], self._data[i]
                )
                i = padre
            else:
                break




    def _sumergir(self, i):
        """Reordena hacia abajo (sumergir) desde el índice i para mantener
        la propiedad de montículo mínimo.
        """

        n = len(self._data)
        while True:
            menor = i
            izq = 2 * i + 1
            der = 2 * i + 2

            if izq < n and self._data[izq] < self._data[menor]:
                menor = izq

            if der < n and self._data[der] < self._data[menor]:
                menor = der

            if menor == i:
                break

            self._data[i], self._data[menor] = (
                self._data[menor], self._data[i]
            )
            i = menor
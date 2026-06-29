class Auto:
    """Representa un auto con su nombre, falla y tiempo de ejecución.

    Posee un atributo adicional `orden_llegada` para mantener el orden de llegada.
    """

    def __init__(self, nombre, falla, tiempo_ejecucion):
        """Inicializa un auto con nombre, falla y tiempo de ejecución."""
        self.nombre = nombre
        self.falla = falla
        self.tiempo_ejecucion = tiempo_ejecucion
        self.orden_llegada = 0  

    def __lt__(self, otro):
        """Compara autos según tiempo de ejecución y orden de llegada."""
        if self.tiempo_ejecucion == otro.tiempo_ejecucion:
            return self.orden_llegada < otro.orden_llegada

        return self.tiempo_ejecucion < otro.tiempo_ejecucion

    def __str__(self):
        """Devuelve una representación legible de cada elemento."""
        return f"{self.nombre} (Falla: {self.falla}, Tiempo de ejecución: {self.tiempo_ejecucion}hrs)"



class MinHeap:
    # Montículo mínimo

    MAX = 10  # límite de autos en cola

    def __init__(self):
        """Inicializa una nueva instancia de MinHeap.

        Se crea una lista donde se almacenarán los elementos del montículo.
        """

        self._data = []
        self._contador = 0 


    def obtener_lista(self):
        """Devuelve la lista interna del min-heap."""
        return self._data
    
    def esta_vacio(self):
        """Verifica si el montículo está vacío."""
        return len(self._data) == 0




    def insertar(self, auto):
        """Inserta un elemento en el montículo.

        Parámetros:
            auto: Valor a insertar de la clase Auto.
            
        Devuelve True si la inserción fue exitosa, o False si el montículo
        ya estaba lleno.
        """

        if len(self._data) >= self.MAX:
            return False

        self._contador += 1
        auto.orden_llegada = self._contador
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
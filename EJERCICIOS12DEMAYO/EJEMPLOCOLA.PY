#CONTIENE LOS MODEULOS PARA IMPLEMENTAR UNA COLA

# Creando la clase Nodo
class Nodo:
    def __init__(self, data):
        self.dato = data
        self.siguiente = None

# Creando la clase Cola y sus métodos: Insertar, eliminar, imprimir
class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    # Método insertar
    def Insertar(self, data):
        nuevo = Nodo(data)
        if self.final is None:
            # Si está vacía
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
        print(f"Elemento '{data}' insertado")
        # Método eliminar
    def Eliminar(self):     
        if self.frente is None:
            print("Cola vacía")
            return
        eliminado = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        print(f"Elemento '{eliminado}' eliminado")             
        # Método imprimir
    def Imprimir(self):
        if self.frente is None:
            print("Cola vacía")
            return
        actual = self.frente
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()
        # Método verificar si está vacía
    def Vacia(self):
        return self.frente is None
        # Método obtener el tamaño
    def Tamano(self):
        actual = self.frente
        contador = 0
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador
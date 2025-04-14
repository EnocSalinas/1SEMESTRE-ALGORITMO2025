# Clase Nodo - representa un nodo de la lista
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Clase ListaEnlazada - gestiona la lista y sus operaciones
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Insertar un nuevo valor al final de la lista
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # Insertar un nuevo valor al inicio de la lista
    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    # Eliminar el primer nodo que contenga el valor
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True  # Valor eliminado
            anterior = actual
            actual = actual.siguiente

        return False  # Valor no encontrado

    # Método para buscar un valor en la lista
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    # Método que imprime los valores de la lista
    def imprimir(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía")
            return
        print("Lista enlazada:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    # Método que cuenta la cantidad de nodos
    def cantidad_nodos(self):
        actual = self.cabeza
        contador = 0
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    # Método que suma los valores de los nodos
    def suma_valores(self):
        actual = self.cabeza
        suma = 0
        while actual:
            suma += actual.valor
            actual = actual.siguiente
        return suma

    # Método que imprime el primer valor de la lista
    def primer_valor(self):
        if self.cabeza:
            print(f"El primer valor es: {self.cabeza.valor}")
        else:
            print("La lista está vacía.")

if __name__ == "__main__":
    lista = ListaEnlazada()  # Creando el objeto lista

    # Leer datos que se insertarán
    datos = [int(x) for x in input("Introduce los valores a insertar, separados por espacio: ").split()]
    for dato in datos:
        lista.insertar(dato)
    
    lista.imprimir()  # Imprimir la lista

    # Insertar al inicio
    lista.insertar_inicio(5)
    lista.imprimir()  # Lista después de insertar al inicio

    # Contar nodos
    print(f"La cantidad de nodos es: {lista.cantidad_nodos()}")

    # Sumar los valores
    print(f"La suma de los valores es: {lista.suma_valores()}")

    # Imprimir el primer valor
    lista.primer_valor()

    # Realizar algunas operaciones de eliminación
    lista.eliminar(10)
    lista.imprimir()  # Lista después de eliminar
    lista.eliminar(5)
    lista.imprimir()  # Lista después de eliminar el primer valor insertado al inicio

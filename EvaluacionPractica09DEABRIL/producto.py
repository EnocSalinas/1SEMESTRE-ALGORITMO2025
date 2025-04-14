class Producto:
    def __init__(self, nombre, categoria, precio, stock):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def agregar_stock(self, cantidad):
        """Agrega stock al producto."""
        self.stock += cantidad

    def retirar_stock(self, cantidad):
        """Retira stock del producto si hay suficiente."""
        if cantidad <= self.stock:
            self.stock -= cantidad
        else:
            print("No hay suficiente stock para retirar.")

    def mostrar_info(self):
        """Muestra la información del producto."""
        total_inventario = self.precio * self.stock
        print(f"Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}, Stock: {self.stock}, Total en inventario: {total_inventario}")
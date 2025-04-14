def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\nMenu:")
    print("1. Registrar un nuevo producto")
    print("2. Agregar stock a un producto existente")
    print("3. Retirar stock de un producto")
    print("4. Mostrar información de un producto")
    print("5. Salir")

def validar_entero(mensaje):
    """Valida que la entrada sea un número entero positivo."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= 0:
                return valor
            else:
                print("Por favor, ingrese un número entero positivo.")
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")

def validar_flotante(mensaje):
    """Valida que la entrada sea un número flotante positivo."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor >= 0:
                return valor
            else:
                print("Por favor, ingrese un número flotante positivo.")
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")

def buscar_producto(nombre, lista_productos):
    """Busca un producto por su nombre en la lista de productos."""
    for producto in lista_productos:
        if producto.nombre.lower() == nombre.lower():
            return producto
    return None
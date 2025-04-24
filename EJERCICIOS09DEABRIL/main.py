# main.py
from producto import Producto
from funciones import mostrar_menu, validar_entero, validar_flotante, buscar_producto

def main():
    productos = []  # Lista

    while True:
        mostrar_menu()
        opcion = validar_entero("Seleccione una opción: ")

        if opcion == 1:
            nombre = input("Ingrese el nombre del producto: ")
            categoria = input("Ingrese la categoría del producto: ")
            precio = validar_flotante("Ingrese el precio del producto: ")
            stock = validar_entero("Ingrese el stock inicial del producto: ")
            nuevo_producto = Producto(nombre, categoria, precio, stock)
            productos.append(nuevo_producto)
            print("Producto registrado exitosamente.")

        elif opcion == 2:
        
            nombre = input("Ingrese el nombre del producto: ")
            producto = buscar_producto(nombre, productos)
            if producto:
                cantidad = validar_entero("Ingrese la cantidad a agregar: ")
                producto.agregar_stock(cantidad)
                print("Stock actualizado.")
            else:
                print("Producto no encontrado.")

        elif opcion == 3:

            nombre = input("Ingrese el nombre del producto: ")
            producto = buscar_producto(nombre, productos)
            if producto:
                cantidad = validar_entero("Ingrese la cantidad a retirar: ")
                producto.retirar_stock(cantidad)
                print("Stock actualizado.")
            else:
                print("Producto no encontrado.")

        elif opcion == 4:
            nombre = input("Ingrese el nombre del producto: ")
            producto = buscar_producto(nombre, productos)
            if producto:
                producto.mostrar_info()
            else:
                print("Producto no encontrado.")

        elif opcion == 5:
            
            
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
def calcular_factura(precio_unitario, cantidad):
    subtotal = precio_unitario * cantidad
    iva = subtotal * 0.15
    total = subtotal + iva

        if subtotal > 1000:
        descuento = subtotal * 0.12
        total -= descuento
    else:
        descuento = 0

    return subtotal, iva, descuento, total

def main():
    while True:
        print("\n--- Factura de Compra ---")
        
        # Como necesitamos datos para trabajar aqui los pedimos 
        precio_unitario = float(input("Ingrese el precio unitario del artículo: "))
        cantidad = int(input("Ingrese la cantidad de artículos: "))
        
        # Aqui basicamente es calcular factura
        subtotal, iva, descuento, total = calcular_factura(precio_unitario, cantidad)
        
        # Ensenar la factura
        print("\n--- Detalle de la Factura ---")
        print(f"Subtotal: {subtotal:.2f} córdobas")
        print(f"IVA (15%): {iva:.2f} córdobas")
        if descuento > 0:
            print(f"Descuento (12%): {descuento:.2f} córdobas")
        print(f"Total a pagar: {total:.2f} córdobas")
        
        # Para que sea ciclo preguntamos si el usuario va a hacer otra compra
        continuar = input("\n¿Desea realizar otra compra? (s/n): ").lower()
        if continuar != 's':
            print("Gracias por su compra. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()

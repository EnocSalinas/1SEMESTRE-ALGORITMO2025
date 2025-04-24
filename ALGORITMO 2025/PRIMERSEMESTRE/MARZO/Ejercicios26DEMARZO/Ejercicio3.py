def calcular_compra(precio_por_docena, docenas):
    # Calcular el total de la compra que se va a realizar
    monto_total = precio_por_docena * docenas
    
    # Calculamos el descuento
    if docenas > 3:
        descuento = monto_total * 0.15
        obsequios = docenas - 3  # Una unidad por cada docena en exceso
    else:
        descuento = monto_total * 0.10
        obsequios = 0

    # Calcular el monto que vamos a pagar
    monto_a_pagar = monto_total - descuento

    return monto_total, descuento, monto_a_pagar, obsequios

def main():
    while True:
        print("\n--- Compra de Productos al por Mayor ---")
        
        # Pedimos datos de la compra a realizar
        precio_por_docena = float(input("Ingrese el precio por docena del producto: "))
        docenas = int(input("Ingrese la cantidad de docenas a comprar: "))
        
        # Calcular la compra
        monto_total, descuento, monto_a_pagar, obsequios = calcular_compra(precio_por_docena, docenas)
        
        # Mostrar el resumen de la compra realizada
        print("\n--- Resumen de la Compra ---")
        print(f"Monto total: {monto_total:.2f} córdobas")
        print(f"Monto del descuento: {descuento:.2f} córdobas")
        print(f"Monto a pagar: {monto_a_pagar:.2f} córdobas")
        print(f"Número de unidades de obsequio: {obsequios}")
        
        # Para que sea ciclo, preguntamos si desea realizar otra compra
        continuar = input("\n¿Desea realizar otra compra? (s/n): ").lower()
        if continuar != 's':
            print("Gracias por su compra. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()

def calcular_importe(vehiculo, distancia=0, toneladas=0):
    if vehiculo == "bicicleta":
        return 100
    elif vehiculo in ["moto", "carro"]:
        return 30 * distancia
    elif vehiculo == "camión":
        return (30 * distancia) + (25 * toneladas)

def main():
    while True:
        print("\nTipos de vehículos:")
        print("1. Bicicleta")
        print("2. Moto")
        print("3. Carro")
        print("4. Camión")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == '5':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        
        vehiculo = ""
        if opcion == '1':
            vehiculo = "bicicleta"
            importe = calcular_importe(vehiculo)
            print(f"El importe a pagar por la bicicleta es: {importe} córdobas.")
        elif opcion in ['2', '3']:
            vehiculo = "moto" if opcion == '2' else "carro"
            distancia = float(input("Ingrese la distancia en Km: "))
            importe = calcular_importe(vehiculo, distancia)
            print(f"El importe a pagar por la {vehiculo} es: {importe} córdobas.")
        elif opcion == '4':
            vehiculo = "camión"
            distancia = float(input("Ingrese la distancia en Km: "))
            toneladas = float(input("Ingrese el peso en toneladas: "))
            importe = calcular_importe(vehiculo, distancia, toneladas)
            print(f"El importe a pagar por el {vehiculo} es: {importe} córdobas.")
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()

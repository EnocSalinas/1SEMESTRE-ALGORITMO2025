import math

def calcular_area_cuadrado(lado):
    return lado ** 2

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_trapecio(base_menor, base_mayor, altura):
    return ((base_menor + base_mayor) * altura) / 2

def main():
    while True:
        print("\n--- Cálculo de Áreas ---")
        print("1. Cuadrado")
        print("2. Rectángulo")
        print("3. Círculo")
        print("4. Triángulo")
        print("5. Trapecio")
        print("6. Salir")
        
        opcion = int(input("Seleccione una opción (1-6): "))
        
        if opcion == 1:
            lado = float(input("Ingrese el lado del cuadrado: "))
            area = calcular_area_cuadrado(lado)
            print(f"El área del cuadrado es: {area:.2f}")
        elif opcion == 2:
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            area = calcular_area_rectangulo(base, altura)
            print(f"El área del rectángulo es: {area:.2f}")
        elif opcion == 3:
            radio = float(input("Ingrese el radio del círculo: "))
            area = calcular_area_circulo(radio)
            print(f"El área del círculo es: {area:.2f}")
        elif opcion == 4:
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = calcular_area_triangulo(base, altura)
            print(f"El área del triángulo es: {area:.2f}")
        elif opcion == 5:
            base_menor = float(input("Ingrese la base menor del trapecio: "))
            base_mayor = float(input("Ingrese la base mayor del trapecio: "))
            altura = float(input("Ingrese la altura del trapecio: "))
            area = calcular_area_trapecio(base_menor, base_mayor, altura)
            print(f"El área del trapecio es: {area:.2f}")
        elif opcion == 6:
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()

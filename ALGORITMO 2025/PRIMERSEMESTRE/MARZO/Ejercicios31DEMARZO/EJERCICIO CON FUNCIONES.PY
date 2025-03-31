def pedir_numero():
    while True:
        num = int(input("Escribe un número impar entre 1 y 19: "))
        if num % 2 == 1 and 1 <= num <= 19:
            return num
        print("Número inválido. Intenta de nuevo.")

def generar_lista_impares(n):
    lista = []
    for i in range(1, n + 1, 2):
        lista.append(i)
    return lista

def sumar_lista(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

def multiplicar_lista(lista):
    total = 1
    for numero in lista:
        total *= numero
    return total

def menu():
    numero = 0
    lista = []
    while True:
        print("\nMenú:")
        print("1. Ingresar número impar entre 1 y 19")
        print("2. Sumar números impares hasta ese número")
        print("3. Multiplicar números impares hasta ese número")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            numero = pedir_numero()
            lista = generar_lista_impares(numero)
        elif opcion == "2":
            if lista:
                print("Suma:", sumar_lista(lista))
            else:
                print("Primero debes ingresar un número.")
        elif opcion == "3":
            if lista:
                print("Multiplicación:", multiplicar_lista(lista))
            else:
                print("Primero debes ingresar un número.")
        elif opcion == "4":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Iniciar programa
menu()

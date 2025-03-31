def es_palindromo(numero):
    # Para invertirlo necesitamos convertir el numero a cadena
    numero_str = str(numero)
    return numero_str == numero_str[::-1]

def main():
    while True:
        print("\n--- Verificación de Palíndromo ---")
        
        # Aqui hacemos que sea un numero de 3 digitos
        numero = int(input("Ingrese un número de tres cifras: "))
        
        # Aqui validamos que el numero tenga 3 digitos
        if 100 <= numero <= 999:
            if es_palindromo(numero):
                print(f"El número {numero} es igual al revés.")
            else:
                print(f"El número {numero} NO es igual al revés.")
        else:
            print("Por favor, ingrese un número válido de tres cifras (100-999).")
        
        # Finalmente preguntamos si desea realizar otra verificación
        continuar = input("\n¿Desea verificar otro número? (s/n): ").lower()
        if continuar != 's':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()

from ejercicio_1 import imprimir_resultado as imprimir_monedas
from ejercicio_2 import imprimir_resultado as imprimir_knapsack
from ejercicio_3 import imprimir_resultado as imprimir_nokia


def ejecutar_ejercicio_1():
    print("\nEJERCICIO 1: Cambio de monedas")
    monto = int(input("Ingrese el monto en centavos: "))
    imprimir_monedas(monto)


def ejecutar_ejercicio_2():
    print("\nEJERCICIO 2: Knapsack fraccionado")

    cantidad = int(input("Ingrese la cantidad de articulos: "))
    articulos = []

    for i in range(cantidad):
        print(f"\nArticulo {i + 1}")
        precio = float(input("Ingrese el precio: "))
        peso = float(input("Ingrese el peso disponible: "))
        articulos.append((precio, peso))

    capacidad = float(input("\nIngrese la capacidad maxima de la bolsa: "))
    imprimir_knapsack(articulos, capacidad, "Caso ingresado por el usuario")


def ejecutar_ejercicio_3():
    print("\nEJERCICIO 3: Combinaciones Nokia")
    n = int(input("Ingrese la cantidad de digitos: "))
    imprimir_nokia(n)


def mostrar_menu():
    print("\n" + "=" * 45)
    print(" MENU PRINCIPAL")
    print("=" * 45)
    print("1. Ejecutar ejercicio 1 - Cambio de monedas")
    print("2. Ejecutar ejercicio 2 - Knapsack fraccionado")
    print("3. Ejecutar ejercicio 3 - Combinaciones Nokia")
    print("4. Salir")
    print("=" * 45)


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            ejecutar_ejercicio_1()
        elif opcion == "2":
            ejecutar_ejercicio_2()
        elif opcion == "3":
            ejecutar_ejercicio_3()
        elif opcion == "4":
            print("\nPrograma finalizado.")
            break
        else:
            print("\nOpcion invalida. Intente nuevamente.")


if __name__ == "__main__":
    main()
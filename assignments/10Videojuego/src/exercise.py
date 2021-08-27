def main():
    # escribe tu código abajo de esta línea
    nuevos = int(input("Dame la cantidad de juegos nuevos: "))*1000
    usados = int(input("Dame la cantidad de juegos usados: "))*350
    total = nuevos + usados
    print("El total de la compra es: ", total)


if __name__ == '__main__':
    main()

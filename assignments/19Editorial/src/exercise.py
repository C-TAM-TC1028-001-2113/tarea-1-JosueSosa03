def main():
    # escribe tu código abajo de esta línea
    import math
    num_palabras = int(input("Dame el numero de palabras: "))
    num_pag =math.ceil(num_palabras/475)
    costo_publicacion = (num_pag)*60
    precio_total = (costo_publicacion) *.9
    print("El costo de la publicación es:", precio_total)


if __name__ == '__main__':
    main()

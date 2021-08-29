def main():
    # escribe tu código abajo de esta línea
    saldo = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el número de cheques: "))
    saldo_total = (saldo + ingresos)-(egresos + (cheques)*(13))
    interes = saldo_total * 0.075
    saldo_final = (saldo_total - interes)
    print("El saldo final de la cuenta es:",saldo_final)
    #Este print da el resultado del saldo final
if __name__ == '__main__':
    main()

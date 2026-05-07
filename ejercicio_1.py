def hacer_sencillo(monto_centavos):
    
    denominaciones = [25, 10, 5, 1]
    resultado = {}
    restante = monto_centavos

    for moneda in denominaciones:
        if restante >= moneda:
            cantidad = restante // moneda
            resultado[moneda] = cantidad
            restante -= cantidad * moneda
        else:
            resultado[moneda] = 0

    return resultado, sum(resultado.values())


def imprimir_resultado(monto_centavos):
    monedas, total = hacer_sencillo(monto_centavos)
    nombres = {25: "Q0.25", 10: "Q0.10", 5: "Q0.05", 1: "Q0.01"}
    print(f"\n{'='*45}")
    print(f"  Monto: Q{monto_centavos/100:.2f}")
    print(f"{'─'*45}")
    for denom, cant in monedas.items():
        if cant > 0:
            print(f"  {nombres[denom]}: {cant} moneda(s)")
    print(f"  Total de monedas: {total}")
    print(f"{'='*45}")



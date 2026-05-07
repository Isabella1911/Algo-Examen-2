def nokia_combinaciones(n):
    """
    Cuenta combinaciones de n dígitos en teclado Nokia 3230.
    Solo movimientos adyacentes (arriba/abajo/izq/der).
    Excluye * y #.
    """
    vecinos = {
        0: [8],
        1: [2, 4],
        2: [1, 3, 5],
        3: [2, 6],
        4: [1, 5, 7],
        5: [2, 4, 6, 8],
        6: [3, 5, 9],
        7: [4, 8],
        8: [7, 5, 9, 0],
        9: [6, 8]
    }

    # Caso base: secuencias de longitud 1
    dp = {d: 1 for d in range(10)}

    for _ in range(n - 1):
        nuevo_dp = {}
        for d in range(10):
            nuevo_dp[d] = sum(dp[v] for v in vecinos[d])
        dp = nuevo_dp

    total = sum(dp.values())
    return total, dp


def imprimir_resultado(n):
    total, dp = nokia_combinaciones(n)
    print(f"\n{'='*50}")
    print(f"  n = {n} dígitos")
    print(f"{'─'*50}")
    print(f"  Combinaciones por dígito final:")
    for d in range(10):
        print(f"    f({n}, {d}) = {dp[d]}")
    print(f"{'─'*50}")
    print(f"  TOTAL combinaciones: {total}")
    print(f"{'='*50}")



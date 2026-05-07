def knapsack_fraccionado(articulos, W):

    # Ordenar por razón precio/peso descendente
    indexados = [(i, p, w) for i, (p, w) in enumerate(articulos)]
    indexados.sort(key=lambda x: x[1] / x[2], reverse=True)

    valor_total = 0.0
    capacidad_restante = W
    solucion = []

    for i, precio, peso in indexados:
        if capacidad_restante == 0:
            break
        tomar = min(peso, capacidad_restante)
        valor = tomar * (precio / peso)
        solucion.append((i + 1, tomar, valor))
        valor_total += valor
        capacidad_restante -= tomar

    return solucion, valor_total


def imprimir_resultado(articulos, W, nombre_caso=""):
    print(f"\n{'='*50}")
    if nombre_caso:
        print(f"  {nombre_caso}")
    print(f"  Capacidad W = {W} u")
    for i, (p, w) in enumerate(articulos):
        print(f"  Artículo {i+1}: precio=${p}, peso={w}u, razón={p/w:.2f}")
    print(f"{'─'*50}")
    solucion, valor = knapsack_fraccionado(articulos, W)
    for idx, unidades, val in solucion:
        print(f"  Tomar {unidades}u del artículo {idx}  →  valor=${val:.2f}")
    print(f"  Valor total obtenido: ${valor:.2f}")
    print(f"{'='*50}")



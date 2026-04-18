"""
Módulo matrix.py
Contém funções para manipulação de matrizes representadas como listas de listas.
"""


def transpor_matriz(matriz):
    """
    Transpõe uma matriz M x N, transformando linhas em colunas e vice-versa.

    Parâmetros:
        matriz (list[list]): Matriz de entrada com M linhas e N colunas.

    Retorna:
        list[list]: Nova matriz N x M transposta.
    """
    if not matriz or not matriz[0]:
        return []

    num_linhas = len(matriz)
    num_colunas = len(matriz[0])

    transposta = []
    for j in range(num_colunas):
        nova_linha = []
        for i in range(num_linhas):
            nova_linha.append(matriz[i][j])
        transposta.append(nova_linha)

    return transposta


def multiplicar_matriz(matriz_a, matriz_b):
    """
    Realiza a multiplicação matricial clássica (Linha por Coluna) entre duas matrizes.

    Parâmetros:
        matriz_a (list[list]): Primeira matriz (M x K).
        matriz_b (list[list]): Segunda matriz (K x N).

    Retorna:
        list[list]: Matriz resultante (M x N), ou None se as dimensões forem incompatíveis.
    """
    if not matriz_a or not matriz_b:
        return None

    linhas_a = len(matriz_a)
    colunas_a = len(matriz_a[0])
    linhas_b = len(matriz_b)
    colunas_b = len(matriz_b[0])

    # Validação: número de colunas de A deve ser igual ao número de linhas de B
    if colunas_a != linhas_b:
        print(
            f"Erro: número de colunas de A ({colunas_a}) "
            f"diferente do número de linhas de B ({linhas_b}). "
            "Multiplicação não é possível."
        )
        return None

    # Inicializa a matriz resultado com zeros
    resultado = [[0] * colunas_b for _ in range(linhas_a)]

    # Cálculo da multiplicação: linha por coluna
    for i in range(linhas_a):
        for j in range(colunas_b):
            for k in range(colunas_a):
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]

    return resultado

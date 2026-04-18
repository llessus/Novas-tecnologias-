def transpor_matriz(matriz):
    if not matriz or not matriz[0]:
        return []

    num_linhas = len(matriz)
    num_colunas = len(matriz[0])

    # Cria uma nova matriz com dimensões N x M preenchida com zeros
    matriz_transposta = [[0 for _ in range(num_linhas)] for _ in range(num_colunas)]

    for i in range(num_linhas):
        for j in range(num_colunas):
            matriz_transposta[j][i] = matriz[i][j]
            
    return matriz_transposta

def multiplicar_matriz(matriz_a, matriz_b):
    """
    Realiza a multiplicação matricial clássica (Linha por Coluna).

    Args:
        matriz_a (list[list]): A primeira matriz.
        matriz_b (list[list]): A segunda matriz.

    Returns:
        list[list]: Uma matriz resultante da multiplicação, ou None se as dimensões forem incompatíveis.
    """
    if not matriz_a or not matriz_b:
        return None

    num_colunas_a = len(matriz_a[0])
    num_linhas_b = len(matriz_b)

    # Validação: o número de colunas de A deve ser igual ao número de linhas de B
    if num_colunas_a != num_linhas_b:
        print("Erro: O número de colunas da Matriz A deve ser igual ao número de linhas da Matriz B para multiplicação.")
        return None

    num_linhas_a = len(matriz_a)
    num_colunas_b = len(matriz_b[0])

    # Inicializa a matriz resultante com zeros
    matriz_resultante = [[0 for _ in range(num_colunas_b)] for _ in range(num_linhas_a)]

    # Realiza a multiplicação
    for i in range(num_linhas_a): # Itera sobre as linhas da matriz A
        for j in range(num_colunas_b): # Itera sobre as colunas da matriz B
            for k in range(num_colunas_a): # Itera sobre as colunas da matriz A (e linhas da matriz B)
                matriz_resultante[i][j] += matriz_a[i][k] * matriz_b[k][j]

    return matriz_resultante

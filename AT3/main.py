"""
Arquivo main.py
Demonstra o uso do módulo matrix.py com os exemplos da Atividade 3.
"""

from matrix import transpor_matriz, multiplicar_matriz


# ──────────────────────────────────────────────
# Exemplo 1: Transposição de Matriz
# ──────────────────────────────────────────────
print("=" * 40)
print("TRANSPOSIÇÃO DE MATRIZ")
print("=" * 40)

A = [[1, 2], [3, 4], [5, 6]]
print(f"Matriz original (3x2):\n{A}")

transposta = transpor_matriz(A)
print(f"\nMatriz transposta (2x3):\n{transposta}")
# Saída esperada: [[1, 3, 5], [2, 4, 6]]


# ──────────────────────────────────────────────
# Exemplo 2: Multiplicação de Matrizes
# ──────────────────────────────────────────────
print("\n" + "=" * 40)
print("MULTIPLICAÇÃO DE MATRIZES")
print("=" * 40)

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(f"Matriz A (2x2):\n{A}")
print(f"\nMatriz B (2x2):\n{B}")

resultado = multiplicar_matriz(A, B)
print(f"\nResultado A x B (2x2):\n{resultado}")
# Saída esperada: [[19, 22], [43, 50]]


# ──────────────────────────────────────────────
# Exemplo 3: Validação de dimensões incompatíveis
# ──────────────────────────────────────────────
print("\n" + "=" * 40)
print("VALIDAÇÃO DE DIMENSÕES INCOMPATÍVEIS")
print("=" * 40)

C = [[1, 2, 3], [4, 5, 6]]   # 2x3
D = [[1, 2], [3, 4]]          # 2x2  (incompatível: colunas de C ≠ linhas de D)
print(f"Matriz C (2x3):\n{C}")
print(f"\nMatriz D (2x2):\n{D}")

resultado_invalido = multiplicar_matriz(C, D)
print(f"\nResultado: {resultado_invalido}")

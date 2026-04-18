from matrix import transpor_matriz, multiplicar_matriz

def main():
    # Simulação do main.py

    # Exemplo de Transposição
    A_transpor = [[1, 2], [3, 4], [5, 6]]
    resultado_transp = transpor_matriz(A_transpor)
    print("--- Transposição ---")
    print(f"Entrada: {A_transpor}")
    print(f"Saída:   {resultado_transp}")

    # Exemplo de Multiplicação
    A_mult = [[1, 2], [3, 4]]
    B_mult = [[5, 6], [7, 8]]
    resultado_mult = multiplicar_matriz(A_mult, B_mult)
    print("\n--- Multiplicação ---")
    print(f"Matriz A: {A_mult}")
    print(f"Matriz B: {B_mult}")
    print(f"Saída:    {resultado_mult}")

if __name__ == "__main__":
    main()

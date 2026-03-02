from .truth_table import print_truth_table


def main():
    expr = input("Digite a expressão lógica: ").strip()
    try:
        print_truth_table(expr)
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()
from .truth_table import print_truth_table
from .predicate_expand import expand_predicates


def main():
    expr = input("Digite a expressão lógica: ").strip()

    try:
        # Se detectar quantificadores, faz expansão em domínio finito
        if "forall" in expr.lower() or "exists" in expr.lower():
            propositional = expand_predicates(expr, domain=["a", "b"])
            print("\nExpressão (Predicados):", expr)
            print("Domínio finito:", "{a, b}")
            print("Após expansão (Proposicional):", propositional, "\n")
            print_truth_table(propositional)
        else:
            print_truth_table(expr)

    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()
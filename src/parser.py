from typing import List
from .tokenizer import Token, tokenize
from .ast_nodes import Node, Var, Not, BinOp

PRECEDENCE = {
    "NOT": 5,
    "AND": 4,
    "OR":  3,
    "IMPLIES": 2,
    "IFF": 1,
}

RIGHT_ASSOC = {"IMPLIES"}  # implicação associa à direita


def to_rpn(tokens: List[Token]) -> List[Token]:
    """Converte lista de tokens para RPN (notação pós-fixa) com shunting-yard."""
    output: List[Token] = []
    stack: List[Token] = []

    prev = None
    for t in tokens:
        if t.kind == "VAR":
            output.append(t)

        elif t.kind in PRECEDENCE:
            # Validação de entrada restrita (evita coisas como: p & & q)
            if t.kind != "NOT":
                if prev is None or prev.kind in PRECEDENCE or prev.kind == "LPAREN":
                    raise ValueError(f"Operador binário {t.value!r} em posição inválida.")
            # NOT pode aparecer em posições mais livres

            while stack and stack[-1].kind in PRECEDENCE:
                top = stack[-1].kind

                if (top not in RIGHT_ASSOC and PRECEDENCE[top] >= PRECEDENCE[t.kind]) or \
                   (top in RIGHT_ASSOC and PRECEDENCE[top] > PRECEDENCE[t.kind]):
                    output.append(stack.pop())
                else:
                    break

            stack.append(t)

        elif t.kind == "LPAREN":
            stack.append(t)

        elif t.kind == "RPAREN":
            while stack and stack[-1].kind != "LPAREN":
                output.append(stack.pop())
            if not stack:
                raise ValueError("Parênteses desbalanceados: faltou '('")
            stack.pop()  # remove '('

        else:
            raise ValueError(f"Token inesperado: {t}")

        prev = t

    while stack:
        if stack[-1].kind in ("LPAREN", "RPAREN"):
            raise ValueError("Parênteses desbalanceados.")
        output.append(stack.pop())

    return output


def rpn_to_ast(rpn: List[Token]) -> Node:
    """Converte RPN em AST."""
    st: List[Node] = []
    for t in rpn:
        if t.kind == "VAR":
            st.append(Var(t.value))
        elif t.kind == "NOT":
            if not st:
                raise ValueError("Negação sem operando.")
            st.append(Not(st.pop()))
        else:
            if len(st) < 2:
                raise ValueError("Operador binário sem operandos suficientes.")
            b = st.pop()
            a = st.pop()
            st.append(BinOp(t.kind, a, b))

    if len(st) != 1:
        raise ValueError("Expressão inválida.")
    return st[0]


def parse(expr: str) -> Node:
    tokens = tokenize(expr)
    rpn = to_rpn(tokens)
    return rpn_to_ast(rpn)
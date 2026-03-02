from typing import Dict
from .ast_nodes import Node, Var, Not, BinOp


def eval_ast(node: Node, env: Dict[str, bool]) -> bool:
    if isinstance(node, Var):
        if node.name not in env:
            raise KeyError(f"Variável {node.name!r} não encontrada no ambiente.")
        return env[node.name]

    if isinstance(node, Not):
        return not eval_ast(node.child, env)

    if isinstance(node, BinOp):
        a = eval_ast(node.left, env)
        b = eval_ast(node.right, env)

        if node.op == "AND":
            return a and b
        if node.op == "OR":
            return a or b
        if node.op == "IMPLIES":
            return (not a) or b
        if node.op == "IFF":
            return a == b

        raise ValueError(f"Operador desconhecido: {node.op}")

    raise TypeError("Nó AST desconhecido.")
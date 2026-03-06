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

        operations = {
            "AND": lambda x, y: x and y,
            "OR": lambda x, y: x or y,
            "IMPLIES": lambda x, y: (not x) or y,
            "IFF": lambda x, y: x == y,
        }

        if node.op not in operations:
            raise ValueError(f"Operador desconhecido: {node.op}")

        return operations[node.op](a, b)

    raise TypeError(f"Nó AST desconhecido: {type(node).__name__}")
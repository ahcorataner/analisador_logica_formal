from dataclasses import dataclass


class Node:
    """Nó base da AST."""
    pass


@dataclass(frozen=True)
class Var(Node):
    name: str


@dataclass(frozen=True)
class Not(Node):
    child: Node


@dataclass(frozen=True)
class BinOp(Node):
    op: str   # AND, OR, IMPLIES, IFF
    left: Node
    right: Node
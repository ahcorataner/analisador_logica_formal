import itertools
from typing import Dict, List, Set, Tuple
from .ast_nodes import Node, Var, Not, BinOp
from .parser import parse
from .evaluator import eval_ast


def collect_symbols(node: Node, vars_set: Set[str], ops_set: Set[str]) -> None:
    if isinstance(node, Var):
        vars_set.add(node.name)
    elif isinstance(node, Not):
        ops_set.add("NOT")
        collect_symbols(node.child, vars_set, ops_set)
    elif isinstance(node, BinOp):
        ops_set.add(node.op)
        collect_symbols(node.left, vars_set, ops_set)
        collect_symbols(node.right, vars_set, ops_set)


def generate_truth_table(expr: str) -> Tuple[List[str], List[Dict[str, bool]], List[bool], Set[str]]:
    ast = parse(expr)

    vars_set: Set[str] = set()
    ops_set: Set[str] = set()
    collect_symbols(ast, vars_set, ops_set)

    vars_list = sorted(vars_set)

    envs: List[Dict[str, bool]] = []
    results: List[bool] = []

    for bits in itertools.product([False, True], repeat=len(vars_list)):
        env = dict(zip(vars_list, bits))
        envs.append(env)
        results.append(eval_ast(ast, env))

    return vars_list, envs, results, ops_set


def print_truth_table(expr: str) -> None:
    vars_list, envs, results, ops_set = generate_truth_table(expr)

    print("Proposições:", ", ".join(vars_list) if vars_list else "(nenhuma)")
    print("Conectivos:", ", ".join(sorted(ops_set)) if ops_set else "(nenhum)")
    print()

    header = vars_list + [expr]
    widths = [max(1, len(h)) for h in header]

    def fmt_row(values):
        return " | ".join(str(v).rjust(w) for v, w in zip(values, widths))

    print(fmt_row(header))
    print("-" * (sum(widths) + 3 * (len(widths) - 1)))

    for env, res in zip(envs, results):
        row = [("T" if env[v] else "F") for v in vars_list] + [("T" if res else "F")]
        print(fmt_row(row))
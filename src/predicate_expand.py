import re
from typing import List


_QUANT_RE = re.compile(r"^(forall|exists)\s+([a-z])\s*\.\s*(.+)$", re.IGNORECASE)

# Predicado do tipo P(x), Q(a,b), Foo(x,y)
_ATOM_RE = re.compile(r"\b([A-Z][A-Za-z0-9_]*)\s*\(\s*([a-zA-Z0-9_,\s]+)\s*\)")

# Predicado sem argumentos (opcional): P, Q, R  (maiúsculos isolados)
_ATOM0_RE = re.compile(r"\b([A-Z][A-Za-z0-9_]*)\b")


def _safe_substitute_var(body: str, var: str, const: str) -> str:
    """
    Substitui a variável var por uma constante const com segurança (por palavra inteira).
    Ex.: x -> a, mas não altera 'x1' nem 'max'.
    """
    return re.sub(rf"\b{re.escape(var)}\b", const, body)


def _encode_atom(name: str, args: List[str]) -> str:
    """
    Converte um átomo de predicados (ex.: P(a,b)) para uma variável proposicional válida (minúscula).
    Ex.: P(a) -> p_a
         Q(a,b) -> q_a_b
         Foo(a) -> foo_a
    """
    base = name.lower()
    args_clean = [a.strip().lower() for a in args]
    return base + "_" + "_".join(args_clean)


def _replace_atoms_with_props(expr: str) -> str:
    """
    Troca predicados por variáveis proposicionais.
    P(a) vira p_a; Q(a,b) vira q_a_b.
    Também remove predicados 0-ários (maiúsculos isolados) transformando em minúsculos (P -> p).
    """

    # 1) Troca átomos com argumentos
    def repl(m: re.Match) -> str:
        name = m.group(1)
        args = [x.strip() for x in m.group(2).split(",")]
        return _encode_atom(name, args)

    out = _ATOM_RE.sub(repl, expr)

    # 2) Troca predicados sem argumentos (maiúsculos isolados) por minúsculos
    # Cuidado: não mexer em palavras reservadas.
    reserved = {"FORALL", "EXISTS"}
    def repl0(m: re.Match) -> str:
        w = m.group(1)
        if w.upper() in reserved:
            return w
        return w.lower()

    out = _ATOM0_RE.sub(repl0, out)

    return out


def expand_predicates(expr: str, domain: List[str] = None) -> str:
    """
    Expande quantificadores em domínio finito e converte átomos de predicados em variáveis proposicionais.
    Retorna uma expressão proposicional (com tokens ~ & | -> <-> e variáveis minúsculas).
    """
    if domain is None:
        domain = ["a", "b"]  # domínio padrão

    s = expr.strip()

    # Enquanto houver quantificador na frente, expande (suporta encadeamento: forall x. exists y. ...)
    while True:
        m = _QUANT_RE.match(s)
        if not m:
            break

        quant = m.group(1).lower()
        var = m.group(2)
        body = m.group(3).strip()

        # Expande o corpo recursivamente primeiro (se o corpo também começar com quantificador)
        # (Isso permite: forall x. exists y. P(x,y))
        body_expanded = expand_predicates(body, domain)

        pieces = []
        for c in domain:
            pieces.append(_safe_substitute_var(body_expanded, var, c))

        joiner = " & " if quant == "forall" else " | "
        s = "(" + joiner.join(pieces) + ")"

    # Depois de expandir quantificadores, converte predicados em proposições
    s = _replace_atoms_with_props(s)

    return s
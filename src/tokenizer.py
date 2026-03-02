from dataclasses import dataclass
import re
from typing import List


@dataclass(frozen=True)
class Token:
    kind: str
    value: str


TOKEN_SPEC = [
    ("SKIP",      r"[ \t\r\n]+"),
    ("IFF",       r"(<->|↔)"),
    ("IMPLIES",   r"(->|→)"),
    ("NOT",       r"(~|!|¬)"),
    ("AND",       r"(&|\^|∧)"),
    ("OR",        r"(\||v|∨)"),
    ("LPAREN",    r"\("),
    ("RPAREN",    r"\)"),
    ("VAR",       r"[a-z][a-z0-9_]*"),
    ("MISMATCH",  r"."),
]

_token_re = re.compile("|".join(f"(?P<{k}>{p})" for k, p in TOKEN_SPEC))


def tokenize(expr: str) -> List[Token]:
    tokens: List[Token] = []
    for m in _token_re.finditer(expr):
        kind = m.lastgroup
        val = m.group()

        if kind == "SKIP":
            continue
        if kind == "MISMATCH":
            raise ValueError(f"Caractere inválido: {val!r}")

        tokens.append(Token(kind, val))
    return tokens
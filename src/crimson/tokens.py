
from dataclasses import dataclass
from enum import Enum, auto


class TokenType(Enum):
    # Single char
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()
    MOD = auto()

    # Literals
    INTEGER = auto()

@dataclass
class Token:
    type: TokenType
    lexeme: str
    line: int
    col: int

    def __repr__(self):
        return f"({self.token_type}, {self.lexeme!r}, {self.line}, {self.col})"



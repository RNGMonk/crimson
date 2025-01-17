# %% 
from fastcore.basics import patch

from crimson.tokens import Token, TokenType


# %% 
class Lexer:
  def __init__(self, source: str):
    self.source = source
    self.processed = 0
    self.cursor = 0
    self.line = 1
    self.column = 0
    self.tokens = []

# %%

@patch
def add_token(self: Lexer, type: TokenType):
   self.tokens.append(Token(type, self.source[self.processed:self.cursor], self.line, self.column))

# %%

@patch
def tokenize(self: Lexer):
  while self.cursor < len(self.source):
    self.processed = self.cursor

    ch = self.source[self.cursor]
    self.cursor += 1
    self.column += 1
    

    match ch:
      case " " | "\t" | "\r": pass
      case "\n": self.line += 1; self.column = 0

      case "+": self.add_token(TokenType.ADD)
      case "-": self.add_token(TokenType.SUB)
      case "*": self.add_token(TokenType.MUL)
      case "/": self.add_token(TokenType.DIV)
      case "%": self.add_token(TokenType.MOD)

  return self.tokens
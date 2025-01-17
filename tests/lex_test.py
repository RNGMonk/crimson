from crimson.lex import Lexer
from crimson.tokens import Token, TokenType


def test_simple():
  source ="""
  +\t\r
  -\r 
  *
  /\r
  %
  """

  tokens = Lexer(source).tokenize()

  assert tokens[0] == Token(TokenType.ADD, "+", 2, 3)
  assert tokens[1] == Token(TokenType.SUB, "-", 3, 3)
  assert tokens[2] == Token(TokenType.MUL, "*", 4, 3)
  assert tokens[3] == Token(TokenType.DIV, "/", 5, 3)
  assert tokens[4] == Token(TokenType.MOD, "%", 6, 3)
import re

# Token types
TOKEN_INTEGER = 'INTEGER'
TOKEN_FLOAT = 'FLOAT'
TOKEN_PLUS = 'PLUS'
TOKEN_MINUS = 'MINUS'
TOKEN_MULTIPLY = 'MULTIPLY'
TOKEN_DIVIDE = 'DIVIDE'
TOKEN_LPAREN = 'LPAREN'
TOKEN_RPAREN = 'RPAREN'
TOKEN_VARIABLE = 'VARIABLE'
TOKEN_ASSIGN = 'ASSIGN'
TOKEN_EOF = 'EOF'

# Regular expression patterns
INTEGER_PATTERN = re.compile(r'\d+')
FLOAT_PATTERN = re.compile(r'[-+]?([0-9]*(\,|\.)[0-9]+|[0-9]+)')
VARIABLE_PATTERN = re.compile(r'[a-zA-Z][a-zA-Z0-9_]*')
WHITESPACE_PATTERN = re.compile(r'\s+')

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )


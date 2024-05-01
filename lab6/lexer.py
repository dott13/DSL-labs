from tokens import *

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def error(self):
        raise Exception('Invalid character')

    def get_next_token(self):
        text = self.text

        # If we've reached the end of the input text
        if self.pos >= len(text):
            return Token(TOKEN_EOF, None)

        function_match = FUNCTION_PATTERN.match(text, self.pos)
        if function_match:
            function_str = function_match.group()
            # Extracting function name and arguments
            function_name, arguments = function_str.split('(')
            arguments = arguments[:-1]  # Removing the closing parenthesis
            self.pos = function_match.end()
            return Token(TOKEN_FUNCTION, (function_name, arguments))
        
        float_match = FLOAT_PATTERN.match(text, self.pos)
        if float_match:
            float_str = float_match.group()
            self.pos = float_match.end()
            if '.' in float_str or ',' in float_str:
                float_str = float_str.replace(',', '.')
                return Token(TOKEN_FLOAT, float(float_str))
            else:
                return Token(TOKEN_INTEGER, int(float_str))
            
        variable_match = VARIABLE_PATTERN.match(text, self.pos)
        if variable_match:
            variable_str = variable_match.group()
            self.pos = variable_match.end()
            return Token(TOKEN_VARIABLE, variable_str)

        # Match operators
        current_char = text[self.pos]
        if current_char == '+':
            self.pos += 1
            return Token(TOKEN_PLUS, '+')
        elif current_char == '-':
            self.pos += 1
            return Token(TOKEN_MINUS, '-')
        elif current_char == '*':
            self.pos += 1
            return Token(TOKEN_MULTIPLY, '*')
        elif current_char == '/':
            self.pos += 1
            return Token(TOKEN_DIVIDE, '/')
        elif current_char == '(':
            self.pos += 1
            return Token(TOKEN_LPAREN, '(')
        elif current_char == ')':
            self.pos += 1
            return Token(TOKEN_RPAREN, ')')
        elif  current_char == '=':
            self.pos +=1
            return Token(TOKEN_ASSIGN, '=')

        # Skip whitespace
        whitespace_match = WHITESPACE_PATTERN.match(text, self.pos)
        if whitespace_match:
            self.pos = whitespace_match.end()
            return self.get_next_token()
        
    def tokenize(self):
        tokens = []
        while True:
            token = self.get_next_token()
            tokens.append(token)
            if token.type == TOKEN_EOF:
                break
        return tokens

        # Invalid character
        self.error()
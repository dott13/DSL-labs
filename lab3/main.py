from lexer import Lexer
from tokens import TOKEN_EOF

if __name__ == '__main__':
    lexer = Lexer('2 + 3 * 4 - (5 / 2.52) * 3,14')
    while True:
        token = lexer.get_next_token()
        if token.type == TOKEN_EOF:
            break
        print(token)
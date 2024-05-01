from lexer import Lexer
from tokens import *
from ASTNode import ASTNode

class Parser:
    def __init__(self, text):
        self.tokens = Lexer(text).tokenize()
        self.current_token = None
        self.token_index = 0

    def error(self):
        raise Exception('Invalid syntax')

    def advance(self):
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
        else:
            self.current_token = Token(TOKEN_EOF, None)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.advance()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        if token.type == TOKEN_INTEGER:
            self.eat(TOKEN_INTEGER)
            return ASTNode('INTEGER', token.value)
        elif token.type == TOKEN_FLOAT:
            self.eat(TOKEN_FLOAT)
            return ASTNode('FLOAT', token.value)
        elif token.type == TOKEN_VARIABLE:
            self.eat(TOKEN_VARIABLE)
            return ASTNode('VARIABLE', token.value)
        elif token.type == TOKEN_FUNCTION:
            return self.function_call()
        elif token.type == TOKEN_LPAREN:
            self.eat(TOKEN_LPAREN)
            node = self.expression()
            self.eat(TOKEN_RPAREN)
            return node

    def term(self):
        node = self.factor()

        while self.current_token.type in (TOKEN_MULTIPLY, TOKEN_DIVIDE):
            token = self.current_token
            if token.type == TOKEN_MULTIPLY:
                self.eat(TOKEN_MULTIPLY)
            elif token.type == TOKEN_DIVIDE:
                self.eat(TOKEN_DIVIDE)

            node = ASTNode(token.value, left=node, right=self.factor())

        return node

    def expression(self):
        node = self.term()

        while self.current_token.type in (TOKEN_PLUS, TOKEN_MINUS):
            token = self.current_token
            if token.type == TOKEN_PLUS:
                self.eat(TOKEN_PLUS)
            elif token.type == TOKEN_MINUS:
                self.eat(TOKEN_MINUS)

            node = ASTNode(token.value, left=node, right=self.term())

        return node

    def parse(self):
        self.current_token = self.tokens[self.token_index]
        return self.expression()
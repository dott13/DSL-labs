from my_parser import Parser
if __name__ == "__main__":
    text = '3 + 4 * (2 - 1)'
    parser = Parser(text)
    ast = parser.parse()
    print(ast)
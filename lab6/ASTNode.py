class ASTNode:
    def __init__(self, type, value=None, args=None, left=None, right=None):
        self.type = type
        self.value = value
        self.args = args
        self.left = left
        self.right = right

    def __str__(self):
        return f'ASTNode(type={self.type}, value={self.value}, args={self.args}, left={self.left}, right={self.right})'

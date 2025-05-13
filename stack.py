class Stack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def __str__(self):
        return str(self.stack)

    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return True if self.stack == [] else False
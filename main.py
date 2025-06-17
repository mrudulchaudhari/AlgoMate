class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        if self.items:
            return self.items.pop()
        return ""
    
    def peek(self):
        return self.items[-1] if self.items else ""
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __str__(self):
        return str(self.items)

    

def is_operator(c):
    return c in "+-*/^"


precedence = {'-': 1, '+': 2, "/": 3, "*": 4, "^":5}

  
def prefix_to_postfix_debug(expression):
    stack = Stack()
    steps= []
    for symbol in reversed(expression):
        if is_operator(symbol):
            op1 = stack.pop()
            op2 = stack.pop()
            new_expr = op1 + op2 + symbol
            stack.push(new_expr)

        else:
            stack.push(symbol)
        steps.append(f"Read: {symbol}, Stack: {stack}")
    return stack.pop(), steps


def prefix_to_infix_debug(expression):
    stack = Stack()
    steps = []

    for symbol in reversed(expression):
        if is_operator(symbol):
            op1 = stack.pop()
            op2 = stack.pop()
            new_expr = f"({op1}{symbol}{op2})"
            stack.push(new_expr)
        else:
            stack.push(symbol)
        
        steps.append(f"Read: {symbol}, Stack: {stack}")

    return stack.pop(), steps


def postfix_to_infix_debug(expression):
    pass


def postfix_to_prefix_debug(expression):
    pass


def infix_to_postfix_debug(expression):
    pass

def infix_to_prefix_debug(expression):
    pass
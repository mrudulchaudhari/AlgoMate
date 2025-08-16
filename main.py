# The Stack class is a reusable data structure.
# It's good practice to keep it as a standalone class.
import math


class Stack:
    """A simple Stack implementation."""

    def __init__(self):
        """Initializes an empty stack."""
        self.items = []

    def push(self, value):
        """Adds an item to the top of the stack."""
        self.items.append(value)

    def pop(self):
        """Removes and returns the top item of the stack."""
        if self.items:
            return self.items.pop()
        return ""

    def peek(self):
        """Returns the top item of the stack without removing it."""
        return self.items[-1] if self.items else ""

    def is_empty(self):
        """Checks if the stack is empty."""
        return len(self.items) == 0

    def __str__(self):
        """Provides a string representation of the stack."""
        return str(self.items)


# The new ExpressionConverter class encapsulates all conversion logic.
class ExpressionConverter:
    """
    A class to handle conversions between different
    mathematical expression notations (infix, prefix, postfix).
    """

    # Corrected precedence for standard order of operations.
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    _operators = set("+-*/^")

    def __init__(self):
        """The constructor for the class."""
        pass

    @staticmethod
    def _is_operator(char):
        """
        A static method to check if a character is an operator.
        """
        return char in ExpressionConverter._operators


    def prefix_to_postfix_debug(self, expression):
        """Converts a prefix expression to postfix with step-by-step debugging info."""
        stack = Stack()
        steps = []
        # Iterate through the expression in reverse.
        for symbol in reversed(expression):
            # Check if the symbol is an operator using our static method.
            if ExpressionConverter._is_operator(symbol):
                # Pop two operands from the stack.
                op1 = stack.pop()
                op2 = stack.pop()
                # Concatenate them in the correct order for postfix and push back.
                new_expr = op1 + op2 + symbol
                stack.push(new_expr)
            else:
                # If it's an operand, push it onto the stack.
                stack.push(symbol)

            # Record the state for debugging purposes.
            steps.append(f"Read: {symbol}, Stack: {stack}")

        # The final result is the only item left on the stack.
        return stack.pop(), steps

    def prefix_to_infix_debug(self, expression):
        """Converts a prefix expression to infix with step-by-step debugging info."""
        stack = Stack()
        steps = []

        for symbol in reversed(expression):
            if ExpressionConverter._is_operator(symbol):
                op1 = stack.pop()
                op2 = stack.pop()
                # Create the infix expression with parentheses and push back.
                new_expr = f"({op1}{symbol}{op2})"
                stack.push(new_expr)
            else:
                stack.push(symbol)

            steps.append(f"Read: {symbol}, Stack: {stack}")

        return stack.pop(), steps

    def postfix_to_infix_debug(self, expression):
        """Converts postfix to infix with step-by-step debugging info."""
        stack = Stack()
        steps = []

        for symbol in expression:
            if ExpressionConverter._is_operator(symbol):
                op2 = stack.pop()
                op1 = stack.pop()
                new_expr = f"({op1}{symbol}{op2})"
                stack.push(new_expr)
            else:
                stack.push(symbol)

            steps.append(f"Read: {symbol}, Stack: {stack}")

        return stack.pop(), steps

    def postfix_to_prefix_debug(self, expression):
        """Converts a postfix expression to prefix with step-by-step debugging info."""
        stack = Stack()
        steps = []

        for symbol in expression:
            if ExpressionConverter._is_operator(symbol):
                op2 = stack.pop()
                op1 = stack.pop()
                new_expr = symbol + op1 + op2
                stack.push(new_expr)
            else:
                stack.push(symbol)

            steps.append(f"Read: {symbol}, Stack: {stack}")

        return stack.pop(), steps

    def infix_to_postfix_debug(self, expression):
        """Converts infix to postfix with step-by-step debugging info using the Shunting Yard algorithm."""
        stack = Stack()
        output = []
        steps = []

        for symbol in expression:
            if symbol.isalnum():
                output.append(symbol)
            elif symbol == '(':
                stack.push(symbol)
            elif symbol == ')':
                while not stack.is_empty() and stack.peek() != '(':
                    output.append(stack.pop())
                stack.pop()  # pop '('
            elif ExpressionConverter._is_operator(symbol):
                while (not stack.is_empty() and
                       stack.peek() != '(' and
                       self.precedence.get(symbol, 0) <= self.precedence.get(stack.peek(), 0)):
                    output.append(stack.pop())
                stack.push(symbol)

            steps.append(f"Read: {symbol}, Stack: {stack}, Output: {''.join(output)}")

        while not stack.is_empty():
            output.append(stack.pop())
            steps.append(f"Draining Stack: Stack: {stack}, Output: {''.join(output)}")

        return ''.join(output), steps

    def infix_to_prefix_debug(self, expression):
        """Converts infix to prefix with step-by-step debugging info."""
        # Reverse expression, swapping parentheses
        reversed_expression = expression[::-1].replace('(', '_').replace(')', '(').replace('_', ')')

        # Get the postfix of the reversed expression
        postfix, steps1 = self.infix_to_postfix_debug(reversed_expression)

        # Reverse the postfix to get the prefix
        prefix = postfix[::-1]

        # Combine steps for a complete debug trail
        steps = [f"Reversed Infix with swapped parentheses: {reversed_expression}"]
        steps.extend(steps1)
        steps.append(f"Reversed Postfix (Prefix): {prefix}")

        return prefix, steps


class MathFunctions:
    """A class for various mathematical calculations."""

    def __init__(self):
        pass

    def factorial(self, num):
        """Calculates the factorial of a number."""
        if num < 0:
            return "Factorial is not defined for negative numbers."
        if num == 0:
            return 1
        # Using an iterative approach to avoid recursion depth limits
        res = 1
        for i in range(1, num + 1):
            res *= i
        return f"The factorial of {num} is {res}"

    def fibonacci(self, num):
        """Calculates the nth Fibonacci term."""
        if num <= 0:
            return "Please enter a positive integer."
        if num == 1:
            return "The 1st Fibonacci term is 0"

        a, b = 0, 1
        for _ in range(num - 1):
            a, b = b, a + b
        return f"The {num}th Fibonacci term is {a}"


    def is_prime(self, num):
        """Checks if a number is prime."""
        if num <= 1:
            return f"{num} is not a prime number."

        if num <= 3:
            return f"{num} is a prime number."

        if num % 2 == 0 or num % 3 == 0:
            return f"{num} is not a prime number."

        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return f"{num} is not a prime number."
            i += 6
        return f"{num} is a prime number."


    def next_prime(self, num):
        """Finds the next prime number after the given number."""
        prime = num + 1
        while True:
            if self._is_prime_check(prime):
                return f"The next prime after {num} is {prime}"
            prime += 1

    def _is_prime_check(self, n):
        """Helper function to check for primality, returns boolean."""
        if n <= 1: return False
        if n <= 3: return True
        if n % 2 == 0 or n % 3 == 0: return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True


    def lcm(self, a, b):
        """Calculates the least common multiple of two numbers."""

        return a*b // math.gcd(a, b)


    def hcf(self, a, b):
        return math.gcd(a, b)
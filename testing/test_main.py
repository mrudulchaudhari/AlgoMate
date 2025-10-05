import unittest

from main import MathFunctions

class TestMathFunctions(unittest.TestCase):
    def setUp(self):
        self.math = MathFunctions()

    def test_factorial(self):
        self.assertEqual(self.math.factorial(1), "The factorial of 1 is 1")
        self.assertEqual(self.math.factorial(2), "The factorial of 2 is 2")
        self.assertEqual(self.math.factorial(3), "The factorial of 3 is 6")
        self.assertEqual(self.math.factorial(6), "The factorial of 6 is 720")

    def test_fibonacci(self):
        self.assertEqual(self.math.fibonacci(1), "The 1st Fibonacci term is 0")
        self.assertEqual(self.math.fibonacci(2), "The 2th Fibonacci term is 1")
        self.assertEqual(self.math.fibonacci(5), "The 5th Fibonacci term is 3")
        self.assertEqual(self.math.fibonacci(10), "The 10th Fibonacci term is 34")


if __name__ == '__main__':
    unittest.main()


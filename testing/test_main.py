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

    def test_is_prime(self):
        self.assertEqual(self.math.is_prime(2), "2 is a prime number.")
        self.assertEqual(self.math.is_prime(3), "3 is a prime number.")
        self.assertEqual(self.math.is_prime(9), "9 is not a prime number.")
        self.assertEqual(self.math.is_prime(45), "45 is not a prime number.")
        self.assertEqual(self.math.is_prime(47), "47 is a prime number.")

    def test_next_prime(self):
        self.assertEqual(self.math.next_prime(2), "The next prime after 2 is 3")
        self.assertEqual(self.math.next_prime(3), "The next prime after 3 is 5")
        self.assertEqual(self.math.next_prime(45), "The next prime after 45 is 47")
        self.assertEqual(self.math.next_prime(47), "The next prime after 47 is 53")
        self.assertEqual(self.math.next_prime(99), "The next prime after 99 is 101")


if __name__ == '__main__':
    unittest.main()


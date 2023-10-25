import unittest
import program

class TestMultiplyFunction(unittest.TestCase):
    def test_multiply_positive_numbers(self):
        result = program.multiply(2, 5)
        self.assertEqual(result, 10)

if __name__ == "__main__":
    unittest.main()
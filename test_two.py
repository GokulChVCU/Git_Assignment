import program
import unittest

class TestMultiplyFunction(unittest.TestCase):
    def test_multiply_negative_numbers(self):
        result = program.multiply(-3, 4)
        self.assertEqual(result, -12)

if __name__ == "__main__":
    unittest.main()
    
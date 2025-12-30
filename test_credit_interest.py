import unittest
from credit_interest import calculate_interest


class TestCreditInterest(unittest.TestCase):

    def test_correct_calculation(self):
        self.assertEqual(calculate_interest(10000, 10), 1000)

    def test_zero_amount(self):
        self.assertEqual(calculate_interest(0, 10), 0)

    def test_negative_amount_raises_exception(self):
        with self.assertRaises(ValueError):
            calculate_interest(-5000, 10)

    def test_negative_rate_raises_exception(self):
        with self.assertRaises(ValueError):
            calculate_interest(5000, -5)


if __name__ == "__main__":
    unittest.main()

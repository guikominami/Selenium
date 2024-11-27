import unittest
from calculator import sum_2_values

class TestCalculadora(unittest.TestCase):
    def test_sum_5_and_5_values_return_10(self):
        self.assertEqual(sum_2_values(5, 5), 10)

    def test_sum_to_return_zero(self):
        self.assertEqual(sum_2_values(5, -5), 0)

    def test_mass(self):
        test_data = (
            (4, 5, 9),
            (-4, 5, 1),
            (1.5, 2.5, 4),
            (13, 25, 38),
            (100, 100, 200),
        )
        for test_data_item in test_data:
            with self.subTest(test_data_item=test_data_item):
                value1, value2, result = test_data_item
                self.assertEqual(sum_2_values(value1, value2), result)

    def test_x_not_valid(self):
        with self.assertRaises(AssertionError):
            sum_2_values('5', -5)

    def test_y_not_valid(self):
        with self.assertRaises(AssertionError):
            sum_2_values(5, '-5')        

unittest.main(verbosity=2)
    
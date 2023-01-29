import unittest
from src.algorithms.count import count
from src.algorithms.postfix import to_postfix


class Test_Count(unittest.TestCase):

    def setUp(self):

        self.test = count
    
    # test correct value for addition
    def test_count_addition(self):

        result = self.test(to_postfix('5+5+10+4'))

        self.assertEqual(result, 24)

    # test correct value for subtraction
    def test_count_subtraction(self):

        result = self.test(to_postfix('8+10-4'))

        self.assertEqual(result, 14)

    # test correct value for multiplication and division
    def test_count_multiplication_and_division(self):

        result = self.test(to_postfix('2+5*10-4/2'))

        self.assertEqual(result, 50)
    
    # test correct value for power of
    def test_count_power_of(self):

        result = self.test(to_postfix('2+4*10+2^2^2+4/2'))

        self.assertEqual(result, 60)
    
    # test correct value for equation with parentheses
    def test_count_parentheses(self):

        result = self.test(to_postfix('(1+2)*(10/2)^(2+1)'))

        self.assertEqual(result, 375)

print(count(to_postfix('5+5+5+5')))
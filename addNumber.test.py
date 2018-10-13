import unittest
from addNumber import get_str_number, add_big_number


class TestAddNumber(unittest.TestCase):
    def test_file_reader(self):
        number = get_str_number('number1.txt')
        self.assertEqual(number, '1289732164789647892314134908798079804190843190270489321743908471023784021'
                                 '3740342124123423414320911234891234')

    def test_file_not_found_error(self):
        self.assertRaises(FileNotFoundError, get_str_number, 'none_exist_file.txt')

    def test_number_not_valid_error(self):
        self.assertRaises(ValueError, get_str_number, 'wrongNumber.txt')

    def test_number_more_than_one(self):
        self.assertRaises(ValueError, get_str_number, 'numbers.txt')

    def test_add_number(self):
        num1 = '11111111111111111'
        num2 = '12345678987654321'
        number = add_big_number(num1, num2)
        self.assertAlmostEquals(number, '23456790098765432')

    def test_add_number_zero(self):
        num1 = '0'
        num2 = '111'
        number = add_big_number(num1, num2)
        self.assertAlmostEquals(number, '111')

    def test_add_number_add_one(self):
        num1 = '999'
        num2 = '1'
        number = add_big_number(num1, num2)
        self.assertAlmostEquals(number, '1000')

    def test_add_number_long(self):
        num1 = '111111111111122222222222222222222222223333333333333333333333333333333333333333333334444444444'
        num2 = '111111111111122222222222222222222222223333333333333333333333333333333333333333333334444444444'
        num3 = '222222222222244444444444444444444444446666666666666666666666666666666666666666666668888888888'
        number = add_big_number(num1, num2)
        self.assertAlmostEquals(number, num3)

if __name__ == '__main__':
    unittest.main()

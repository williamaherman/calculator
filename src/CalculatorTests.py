import unittest

from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_method_calculator_success(self):
        self.assertEqual(self.calculator.add(1.36,2.78), 4.14)

    def test_add_method_calculator_zero(self):
        self.assertEqual(self.calculator.add(-1.11, 1.11), 0)

    def test_subtract_method_calculator_success(self):
        self.assertEqual(self.calculator.subtract(4, 10), 6)

    def test_subtract_method_calculator_zero(self):
        self.assertEqual(self.calculator.subtract(4, 4), 0)

    def test_multiply_method_calculator_success(self):
        self.assertEqual(self.calculator.multiply(5, 5), 25)

    def test_multiply_method_calculator_zero(self):
        self.assertEqual(self.calculator.multiply(5, 0), 0)

    def test_divide_method_calculator_success(self):
        self.assertEqual(self.calculator.divide(5, 20), 4)

    def test_divide_method_calculator_zero(self):
        self.assertEqual(self.calculator.divide(5, 0), 0)

    def test_square_method_calculator_success(self):
        self.assertEqual(self.calculator.square(5), 25)

    def test_square_method_calculator_negative(self):
        self.assertEqual(self.calculator.square(-5), 25)

    def test_square_root_method_calculator_success(self):
        self.assertEqual(self.calculator.square_root(25), 5)

    def test_square_root_method_calculator_success_decimal(self):
        self.assertEqual(self.calculator.square_root(39.99), 6.3237647)

    def test_subtraction(self):
        test_data = CsvReader("Tests/Data/UnitTestSubtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_addition(self):
        test_data = CsvReader("Tests/Data/UnitTestAddition.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiplication(self):
        test_data = CsvReader("Tests/Data/UnitTestMultiplication.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_division(self):
        test_data = CsvReader("Tests/Data/UnitTestDivision.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square(self):
        test_data = CsvReader("Tests/Data/UnitTestSquare.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square_root(self):
        test_data = CsvReader("Tests/Data/UnitTestSquareRoot.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square_root(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)


if __name__ == '__main__':
    unittest.main()
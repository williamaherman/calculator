import unittest

from Calculator import Calculator
from CsvReader import CsvReader, ClassFactory


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

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
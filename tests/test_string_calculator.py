import pytest
from src.string_calculator import StringCalculator

class TestStringCalculator:
    @pytest.fixture
    def stringCalculator(self):
        return StringCalculator()

    def test_empty_string_returns_zero(self, stringCalculator):
        assert stringCalculator.calculate("") == 0

    def test_number_as_input(self, stringCalculator):
        input_string = "123"    
        assert stringCalculator.calculate(input_string) == 123

    def test_sum_with_comma(self, stringCalculator):
        input_string = "5,4"
        assert stringCalculator.calculate(input_string) == 9

    def test_sum_with_newline(self, stringCalculator):
        input_string = "23\n6"
        assert stringCalculator.calculate(input_string) == 29

    def test_sum_with_comma_or_newline(self, stringCalculator):

        arr = ["4,5,3", "4\n5\n3", "4,5\n3", "4\n5,3"]

        for el in arr:
            assert stringCalculator.calculate(el) == 12

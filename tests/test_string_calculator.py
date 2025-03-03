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

import pytest
from src.string_calculator import StringCalculator

class TestStringCalculator:
    @pytest.fixture
    def calculator(self):
        return StringCalculator()
   
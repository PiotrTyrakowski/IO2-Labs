import re

class StringCalculator:
    def calculate(self, numbers_str: str):
        if not numbers_str:
            return 0
        
        if ',' not in numbers_str and '\n' not in numbers_str:
            return int(numbers_str)
        
        numbers_str = numbers_str.replace('\n', ',')
        
        splitted = numbers_str.split(',')
        numbers = [int(num) for num in splitted]
        
        return sum(numbers)
    
        
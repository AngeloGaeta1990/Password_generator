import random


class Mixin:
    """
    This class contain methods which can be used by all classes
    """
    def generate_random_numbers(self, amount):
        numbers = [random.randint(0,9) for n in range(amount)]
        return numbers
        
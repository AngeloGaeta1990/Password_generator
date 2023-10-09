import random
import string


class NumbersMixin():
    """
    Mixin subclass for generating random numbers.
    """
    def generate_random_numbers(self, amount):
        """
        generates a list of random numbers
        """
        numbers = [random.randint(0, 9) for n in range(amount)]
        return numbers


class SpecialCharactersMixin():
    """
    Mixin subclass for generating random special characters.
    """
    def generate_random_special_characters(self, amount):
        """
        generates a list of special characters
        """
        all_special_characters = ['!', '@', '#', '$', '%', '^', '&', '*',
                                  '(', ')', '-', '_', '=', '+', '[', ']',
                                  '{', '}', ';', ':', '<', '>', ',', '.',
                                  '/', '?', '|', '\\', '`', '~']
        special_characters = random.choices(all_special_characters, k=amount)
        return special_characters


class UpperCaseLettersMixin():
    """
    Mixin subclass for generating random uppercase letters.
    """
    def generate_random_upper_case_letters(self, amount):
        """
        generates a list of random uppercase letters
        """
        letters = string.ascii_uppercase
        random_letters = random.choices(letters, k=amount)
        return random_letters


class LowerCaseLettersMixin():
    """
    Mixin subclass for generating random lowercase letters.
    """
    def generate_random_lower_case_letters(self, amount):
        """
        generates a list of random lowercase letters
        """
        letters = string.ascii_lowercase
        random_letters = random.choices(letters, k=amount)
        return random_letters

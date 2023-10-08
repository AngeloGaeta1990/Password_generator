import random
import hashlib
import requests
from .mixin import NumbersMixin
from .mixin import SpecialCharactersMixin
from .mixin import UpperCaseLettersMixin
from .mixin import LowerCaseLettersMixin


class Password (NumbersMixin, SpecialCharactersMixin,
                UpperCaseLettersMixin, LowerCaseLettersMixin):
    """
    Password class contains all the info required to build password
    """
    PWNED_API_URL = "https://api.pwnedpasswords.com/range/"

    def __init__(self, length=10, numbers_length=2,
                 special_characters_length=2, upper_case_length=2):
        self.length = length
        self.numbers_length = numbers_length
        self.special_characters_length = special_characters_length
        self.upper_case_length = upper_case_length
        self.lower_case_length = self.length - \
            (self.special_characters_length +
             self.numbers_length + self.upper_case_length)
        self.pwd = None
        self.numbers_list = None
        self.special_characters_list = None
        self.upper_case_list = None
        self.lower_case_list = None
        self.hash_code = None
        self.prefix = None

    def add_numbers_list(self):
        """
        generates a list of random numbers each value between 0 and 9
        the length of the list is equal to self.numbers value
        """
        self.numbers_list = self.generate_random_numbers(self.numbers_length)

    def add_special_characters(self):
        """
        generates a list of random special characters the length of the list
        is equal to self.special_characters value
        """
        self.special_characters_list = self.generate_random_special_characters(
            self.special_characters_length)

    def add_upper_case_letters(self):
        """
        generates a list of upper case letter  the length of the list is equal
        to upper_case_letters value
        """
        self.upper_case_list = self.generate_random_upper_case_letters(
            self.upper_case_length)

    def add_lower_case_letters(self):
        """
        generates a list of lower case letters the length of the list is equal
        to
        self.length-(self.special_characters+self.numbers+self.upper_case_letters)
        """
        self.lower_case_list = self.generate_random_lower_case_letters(
            self.lower_case_length)

    def generate_password(self):
        """
        merges  self.numbers_list, self.special_characters_list
        self.upper_case_list and self.lower_case_list
        into a single list,
        shuffles the elements and joins them into a single string
        """
        all_characters = self.numbers_list + self.special_characters_list + \
            self.upper_case_list + self.lower_case_list
        all_characters_shuffled = random.sample(
            all_characters, len(all_characters))
        self.pwd = "".join(map(str, all_characters_shuffled))

    def generate_hash_code(self):
        """
        turns the password into an hash code
        """
        self.hash_code = hashlib.sha1(self.pwd.encode()).hexdigest().upper()
        self.prefix = self.hash_code[:5]

    def check_hacked_password(self):
        """
        Sends hash code to Pwned Passwords API and
        verifies if API has been hacked
        """
        print("Reaching Pwned Password API")
        try:
            response = requests.get(
                f"{self.PWNED_API_URL}{self.prefix}")
            if response.status_code == 200:
                suffix = self.hash_code[5:]
                for line in response.text.splitlines():
                    if line.startswith(suffix):
                        self.secure = False
                        break
                    else:
                        self.secure = True
                if not self.secure:
                    print(f"The password '{self.pwd}' has been exposed"
                          f"{line.split(':')[1]} times in data breaches.")
                elif self.secure:
                    print(f"The password '{self.pwd}' has not been found"
                          f"in data breaches.")
            else:
                print("Warning: Unable to connect to the API. I can not check"
                      " if your password has already been exposed")
        except requests.exceptions.RequestException as e:
            print(f"API request error: {e}")

    def builder(self):
        """
        joins methods add_numbers_list(), add_special_characters(),
        add_upper_case_letters(), add_lower_case_letters(),
        generate_password()
        """
        self.add_numbers_list()
        self.add_special_characters()
        self.add_upper_case_letters()
        self.add_lower_case_letters()
        self.generate_password()

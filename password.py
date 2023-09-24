from mixin import Mixin

class Password(Mixin):
    """
    Password class contains the following:
      self.length = int() lenght of the password default 10
      self.numbers = int() amount of numbers to include in the password default 2
      self.special_characters = int() amount of special characther to include in the password default 2
      self.upper_case_letters = int() amount of upper case letter to include in the password default 2
      self.letters = int() amount of letter to include in password = self.length - (self.numbers + self.special_characters)
      self.pwd = str() password returned to user
      aelf.number_list = list() list of 1 digit integers to include in password e.g. [2,7,3]
      self.special_characters_list = list() list of special characters to include in password e.g. ["@",".","!"] 
      self.upper_case_letters_list = list() list of upper case letters to include in password e.g. ["A","G"]
      self.lower_case_letters_list = list() list of lower case letters to include in password e.g. ["d","f","t"]
    """
    def __init__(self, length=10, numbers=2, special_characters=2, upper_case_letters = 2):
        self.length = length
        self.numbers = numbers
        self.special_characters = special_characters
        self.upper_case_letters = upper_case_letters
        self.lower_case_letters = self.length - (self.special_characters + self.numbers + self.upper_case_letters)
        self.pwd = None
        self.numbers_list = None
        self.special_characters_list = None
        self.upper_case_letters_list = None
        self.lower_case_letters_list = None
        
    
    def add_numbers_list(self):
      """
      generates a list of random numbers each value between 0 and 9
      the lenght of the list is equal to self.numbers value
      """
      self.numbers_list = self.generate_random_numbers(self.numbers)
        
    def add_special_charaters(self):
      """
      generates a list of random special characters the lenght of the list is equal to self.special_characters value
      """
      self.special_characters_list = self.generate_random_special_characters(self.special_characters)
      
    def add_upper_case_letters(self):
      """
      generates a list of upper case letter  the lenght of the list is equal to upper_case_letters value
      """
      self.upper_case_letters_list = self.generate_random_upper_case_letters(self.upper_case_letters)
      
    def add_lower_case_letters(self):
      """
      generates a list of lower case letters the lenght of the list is equal to self.length - (self.special_characters + self.numbers + self.upper_case_letters)
      """
      if self.lower_case_letters > 0:
        self.lower_case_letters_list = self.generate_random_lower_case_letters(self.lower_case_letters)
      
   
        
from mixin import Mixin
import random

class Password(Mixin):
    """
    Password class contains the following:
      self.length = int() lenght of the password default 10
      self.numbers_length = int() amount of numbers to include in the password default 2
      self.special_characters_length = int() amount of special characther to include in the password default 2
      self.upper_case_length = int() amount of upper case letter to include in the password default 2
      self.lower_case_length = int() amount of lower case letter to include in password = 
      self.length - (self.numbers_legnth + self.special_characters_length + self.upper_case_length)
      self.pwd = str() password returned to user
      aelf.number_list = list() list of 1 digit integers to include in password e.g. [2,7,3]
      self.special_characters_list = list() list of special characters to include in password e.g. ["@",".","!"] 
      self.upper_case_list = list() list of upper case letters to include in password e.g. ["A","G"]
      self.lower_case_list = list() list of lower case letters to include in password e.g. ["d","f","t"]
    """
    def __init__(self, length=10, numbers_length=2, special_characters_length=2, upper_case_length=2):
        self.length = length
        self.numbers_length = numbers_length
        self.special_characters_length = special_characters_length
        self.upper_case_length = upper_case_length
        self.lower_case_length = self.length - (self.special_characters_length + self.numbers_length + self.upper_case_length)
        self.pwd = None
        self.numbers_list = None
        self.special_characters_list = None
        self.upper_case_list = None
        self.lower_case_list = None
        
    
    def add_numbers_list(self):
      """
      generates a list of random numbers each value between 0 and 9
      the lenght of the list is equal to self.numbers value
      """
      self.numbers_list = self.generate_random_numbers(self.numbers_length)
      print(self.numbers_list)
        
    def add_special_charaters(self):
      """
      generates a list of random special characters the lenght of the list is equal to self.special_characters value
      """
      self.special_characters_list = self.generate_random_special_characters(self.special_characters_length)
      print(self.special_characters_list)
      
    def add_upper_case_letters(self):
      """
      generates a list of upper case letter  the lenght of the list is equal to upper_case_letters value
      """
      self.upper_case_list = self.generate_random_upper_case_letters(self.upper_case_length)
      print(self.upper_case_list)
      
    def add_lower_case_letters(self):
      """
      generates a list of lower case letters the lenght of the list is equal to 
      self.length - (self.special_characters + self.numbers + self.upper_case_letters)
      """
      self.lower_case_list = self.generate_random_lower_case_letters(self.lower_case_length)
      print(self.lower_case_list)
      
      
    def generate_password(self):
      """
      merges  self.numbers_list, self.special_characters_list, self.upper_case_list and self.lower_case_list 
      into a single list, shuffles the elements and joins them into a single string
      """
      all_characters = self.numbers_list + self.special_characters_list + self.upper_case_list + self.lower_case_list
      all_characters_shuffled = random.sample(all_characters, len(all_characters))
      self.pwd = "".join(map(str,all_characters_shuffled))
      print(self.pwd)
      
   
        
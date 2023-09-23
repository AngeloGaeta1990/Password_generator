from mixin import Mixin

class Password(Mixin):
    """
    Password class contains the following:
      self.length = int() lenght of the password default 10
      self.numbers = int() amount of numbers to include in the password default 2 
      self.special_characters = int() amount of special characther to include in the password default 2
      self.pwd = str() password returned to user
      aelf.number_list = list() numbers which will be included in password
      
    
    """
    def __init__(self, length=10, numbers=2, special_characters=2):
        self.length = length
        self.numbers = numbers
        self.special_characters = special_characters
        self.pwd = None
        self.numbers_list = None
        
    
    def add_numbers_list(self):
        self.numbers_list = self.generate_random_numbers(self.numbers)
        
        
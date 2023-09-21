class Password():
    """
    Password class contains the following:
      self.length = int() lenght of the password default 10
      self.numbers = int() amount of numbers to include in the password default 2 
      self.special_characters = int() amount of special characther to include in the password default 2 
      
    
    """
    def __init__(self, length=10, numbers=2, special_characters=2):
        self.length = length
        self.numbers = numbers
        self.special_characters = special_characters
        self.pwd = None 
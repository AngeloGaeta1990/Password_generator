# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import requests
import hashlib
from account import Account
from password import Password

PASSWORD_CHARACTERS = 10
PASSWORD_NUMBERS = 2
PASSWORD_SPECIAL_CHARACTERS = 2


def get_account_data():
    """
    Creates the account class taking input from the user
    """
    while True:
        (print("Welcome to the Secure Password Generator"))
        (print("Please enter the service for which you need the password"))
        (print("Example: Netflix"))
        
        service = input("Enter the name of the service here:\n")
        
        (print("Please enter the username"))
        (print("Example: my_email@provider.com"))
        username =  input("Enter the username here:\n")
        
        (print(f"You are a creating a password for {service} and your username is {username}"))
        #TODO add lowercase
        approval =(input("Are the service and username correct ? (yes or no)\n")).lower()
        if approval == "yes":
            account = Account(service, username)
            return account
        else:
            print(f"You entered {approval} you should type yes or no")
            print("Please try again")
        
def get_password_info():
    """
    Generates password instance
    """
    no_confirmation = True
    while no_confirmation:
        print("This script will generate a random password including:\n") 
        print(f"{PASSWORD_CHARACTERS} characters in total \n")
        print(f"{PASSWORD_NUMBERS} numbers \n")
        print(f"{PASSWORD_SPECIAL_CHARACTERS} special characters \n")
        #TODO add lower case
        approval =  input("Do you want to keep this settings? (yes/no)\n").lower()
        if approval == "yes":
            no_confirmation = False
            password = Password()
        elif approval == "no":
             password = edit_password_default()
             if password:
                 no_confirmation = False
        else:
            print(f"You entered {approval} you should type yes or no")
    
    return password
    
def edit_password_default():
    """
    if user disagrees with default password setting edit them
    """
    validation = False
    while not validation:
        try:
            password_length = input((f"How many total characters do you want in your password? (enter a number e.g.10)\n" ))
            password_length_int = int(password_length)
        except ValueError:
            print(f"You entered {password_length}, you should enter a number e.g.  10\n")
            print("Let's try again.")
            break
        
        try:
            numbers = input((f"How many numbers do you want in your password? (enter a number e.g.2)\n" ))
            numbers_int = int(numbers)
        except ValueError:
            print(f"You entered {numbers}, you should enter a number e.g. 10")
            print("Let's try again.")
            break
        try:
            special_characters = input((f"How many special characters do you want in your password? (enter a number e.g.2)\n" ))
            special_characters_int = int(numbers)
        except ValueError:
            print(f"You entered {special_characters}, you should enter a number e.g. 10")
            print("Let's try again.")
            break
        validation = validate_new_password_settings(password_length_int, numbers_int, special_characters_int)
        password= Password(password_length_int, numbers_int, special_characters_int)
        return password
        
        
def validate_new_password_settings(password_length_int, numbers_int, special_characters_int):
    """
    checks if the special characters + numbers < password length
    """
    if numbers_int + special_characters_int <= password_length_int:
        return True
    else:
        print(f"You have selected {numbers_int} numbers and {special_characters_int} special characters\n")
        print(f"resulting in a total of {numbers_int + special_characters_int} characthers\n") 
        print(f"this exceeds the desired password length of {password_length_int} characthers\n")
        print("Please try again")
        return False
                      
    

def main():
    account = get_account_data()
    password = get_password_info()
    

main()
# # Define your password
# password = "hello123"

# # Create a SHA-1 hash of the password
# password_hash = hashlib.sha1(password.encode()).hexdigest().upper()
# print("pwd_hash",password_hash)

# # Take the first 5 characters of the hash
# prefix = password_hash[:5]
# print("prefix",prefix)

# # Make a GET request to the "Pwned Passwords" API
# url = f"https://api.pwnedpasswords.com/range/{prefix}"
# response = requests.get(url)
# print(response.text)

# if response.status_code == 200:
#     # Check if the remaining part of the hash exists in the API response
#     suffix = password_hash[5:]
#     for line in response.text.splitlines():
#         if line.startswith(suffix):
#             print(f"The password '{password}' has been exposed {line.split(':')[1]} times in data breaches.")
#             break
#     else:
#         print(f"The password '{password}' has not been found in data breaches.")
# else:
#     print("Error: Unable to connect to the API.")
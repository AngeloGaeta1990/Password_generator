# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import requests
import hashlib
from account import Account
from password import Password




def get_account_data():
    """
    Creates the account class taking input from the user
    """
    while True:
        (print("Welcome to the secure password generator"))
        (print("Please enter the service you need the password for"))
        (print("Example: Netflix"))
        
        service = input("Enter the name of the service here:\n")
        
        (print("Please enter the username"))
        (print("Example: my_email@provider.com"))
        username =  input("Enter the username here:\n")
        
        (print(f"You are a creating a password for {service} and your username is {username}"))
        approval =(input("Are the service and username correct ? (yes/or no) "))
        if approval == "yes":
            account = Account(service, username)
            return account
        
def get_password_info():
    """
    takes user input required to generate password
    """
    pass


def main():
    account = get_account_data()
    

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
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from account import Account
from password import Password

PASSWORD_CHARACTERS = 10
PASSWORD_NUMBERS = 2
PASSWORD_SPECIAL_CHARACTERS = 2
PASSWORD_UPPER_CASE_CHARACTERS = 2


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
        print(f"{PASSWORD_UPPER_CASE_CHARACTERS} capital letters \n")
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
            numbers_length = input((f"How many numbers do you want in your password? (enter a number e.g.2)\n" ))
            numbers_int = int(numbers_length)
        except ValueError:
            print(f"You entered {numbers_length}, you should enter a number e.g. 10")
            print("Let's try again.")
            break
        try:
            special_characters_length = input((f"How many special characters do you want in your password? (enter a number e.g.2)\n" ))
            special_characters_int = int(special_characters_length)
        except ValueError:
            print(f"You entered {special_characters_length}, you should enter a number e.g. 10")
            print("Let's try again.")
            break
        try:
            upper_case_length = input((f"How many upper case letters do you want in your password? (enter a number e.g.2)\n" ))
            upper_case_letters_int = int(upper_case_length)
        except ValueError:
            print(f"You entered {upper_case_length}, you should enter a number e.g. 10")
            print("Let's try again.")
            break
           
        validation = validate_new_password_settings(password_length_int, numbers_int, special_characters_int, upper_case_letters_int)
        password= Password(password_length_int, numbers_int, special_characters_int, upper_case_letters_int)
        return password
        
        
def validate_new_password_settings(password_length_int, numbers_int, special_characters_int, upper_case_letters_int):
    """
    checks if the special characters + numbers < password length
    """
    if numbers_int + special_characters_int + special_characters_int <= password_length_int:
        return True
    else:
        print(f"You have selected {numbers_int} numbers, {special_characters_int} special characters and {upper_case_letters_int} upper case letters\n")
        print(f"resulting in a total of {numbers_int + special_characters_int + upper_case_letters_int} characthers\n") 
        print(f"this exceeds the desired password length of {password_length_int} characthers\n")
        print("Please try again")
        return False
                      
def generate_password(password):
    """
    generate the password string, it generates numbers, special characters, upper and lower case letters list
    then shuffles the characters, show to the user the password and asks if it should be kept or a new one should
    be generated
    """
    print("Generating password...")
    user_like = False
    while not user_like:
        password.builder()
        print(f"The password generated is\n {password.pwd}")
        user_decision = input("Do you want to keep this password? (yes/no)\n(If 'no' a new password will be generated)\n").lower()
        if user_decision == "yes":
            user_like = True
    return password
        
def api_verification (password):
    """
    turns password into hash code and checks if password has been hacked
    """
    password.generate_hash_code()
    password.check_hacked_password()
    return password

def main():
    account = get_account_data()
    password_info = get_password_info()
    password = generate_password(password_info)
    password_api = api_verification(password)
    
main()

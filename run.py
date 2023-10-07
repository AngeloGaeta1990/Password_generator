# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import csv
import os
from account import Account
from password import Password

PASSWORD_CHARACTERS = 10
PASSWORD_NUMBERS = 2
PASSWORD_SPECIAL_CHARACTERS = 2
PASSWORD_UPPER_CASE_CHARACTERS = 2
MAX_PASSWORD_CHARATERS = 100
ASCII_ART =   """
                                                ███████║███████╗███████╗██╗   ██║██████╗ ███████╗                            
                                                ██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗██╔════╝                            
                                                ███████╗█████╗  ██║     ██║   ██║██████╔╝█████╗                              
                                                ╚════██║██╔══╝  ██║     ██║   ██║██╔══██╗██╔══╝                              
                                                ███████║███████╗╚██████╗╚██████╔╝██║  ██║███████╗                            
            .--------.                          ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
           / .------. \ 
          / /        \ \               ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗           
          | |        | |               ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗   
         _| |________| |_              ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    
       .' |_|        |_| '.            ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
       '._____ ____ _____.'            ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝ 
       |     .'____'.     |            ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
       '.__.'.'    '.'.__.'
       '.__  |      |  __.'      ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
       |   '.'.____.'.'   |     ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
       '.____'.____.'____.'     ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
       '.________________.'     ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗                    
                                ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║    
                                 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   
                                                                                                                                                                                                                                                                                                               
        """
    
def show_intro():
    """
    Show ASCII art and tool instructions and centers them
    """
    terminal_width = os.get_terminal_size().columns
    # ASCII_ART
    print(ASCII_ART)
    # Tool instructions
    prompt_instructions = "Press I for instructions, or press Enter to start"
    padding_instructions = (terminal_width - len(prompt_instructions)) // 2
    centered_prompt_instructions = " " * padding_instructions + prompt_instructions
    start_tool = (input(centered_prompt_instructions + "\n"))
    start_tool = start_tool.lower()
    if start_tool == "i":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""
        This tool will generate a secure password for the account of your choice, e.g., Netflix. 
        The generated password will not be saved in the cloud to enhance security. \n
        
        By default the password generated will have the different features:\n
        
        {PASSWORD_CHARACTERS} characters in total (max 100)\n 
        {PASSWORD_NUMBERS} numbers \n
        {PASSWORD_SPECIAL_CHARACTERS} special characters \n
        {PASSWORD_UPPER_CASE_CHARACTERS} capital letters \n
        
        These settings can be edited according to the user's preferences.\n
        After generation, the password will be converted into a hash code. 
        The hash code will be sent to the PWNED API to verify that the password has not been found in data breaches.\n
        Follow the steps in the Terminal to generate the password
        """
        )
        prompt_continue = "press Enter to continue"
        padding_continue = (terminal_width - len(prompt_instructions)) // 2
        centered_prompt_continue = " " * padding_continue + prompt_continue
        input(centered_prompt_continue + "\n")

def get_account_data():
    """
    Creates the account class taking input from the user
    """
    while True:
        print("Welcome to the Secure Password Generator")
        print("Please enter the service for which you need the password")
        print("Example: Netflix")
        
        service = input("Enter the name of the service here:\n")
        
        print("Please enter the username")
        print("Example: my_email@provider.com")
        username =  input("Enter the username here:\n")
        
        print(f"You are a creating a password for {service} and your username is {username}")
        else_account_approval = True
        while else_account_approval:
            approval =input(f"Are the service {service} and username {username} correct ? (yes or no)\n").lower()
            if approval == "yes":
                account = Account(service, username)
                else_account_approval = False
                return account
            elif approval == "no":
                 else_account_approval = False
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
            print(f"You entered {password_length}, you should enter an integer number e.g.  10\n")
            print("Let's try again.")
            break
        
        try:
            numbers_length = input((f"How many numbers do you want in your password? (enter a number e.g.2)\n" ))
            numbers_int = int(numbers_length)
        except ValueError:
            print(f"You entered {numbers_length}, you should enter an integer number e.g. 10\nLet's try again.")
            break
        try:
            special_characters_length = input((f"How many special characters do you want in your password? (enter a number e.g.2)\n" ))
            special_characters_int = int(special_characters_length)
        except ValueError:
            print(f"You entered {special_characters_length}, you should enter an integer number e.g. 10\nLet's try again.")
            break
        try:
            upper_case_length = input((f"How many upper case letters do you want in your password? (enter a number e.g.2)\n" ))
            upper_case_letters_int = int(upper_case_length)
        except ValueError:
            print(f"You entered {upper_case_length}, you should enter a number e.g. 10\nLet's try again.")
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
        else:
            print(f"You entered {user_decision}, please enter yes or no")
    return password
        
def api_verification(password):
    """
    turns password into hash code and checks if password has been hacked
    """
    password.generate_hash_code()
    password.check_hacked_password()
    return password

def update_account(account, password):
    """
    Adds password and secure info to account instance
    """
    account.password = password.pwd
    if password.secure == True:
        account.secure = "Verified" 
    return account

def show_output_in_terminal(account):
    #TODO: write meaningful indication on how to store password info
    """
    Print account info on the terminal 
    """
    print(f"The data for the {account.service} account are below ")
    print(account.print_account())
    print("Please store this data in a secure and confidential location.")
    

def create_password_file(account, filename = "secure_passwords.csv"):
    """
    takes an account object in input
    and creates a .csv file listing Account, User name, Password and security 
    """
    account_dict = account.account_dict()
    headers = account_dict.keys()
    account_list = [account_dict]
    
    file_exists = False
    try:
        with open(filename, 'r') as csvfile:
            existing_headers = next(csv.reader(csvfile))
            if existing_headers == list(headers):
                file_exists = True
                file_writing_mode = 'a' 
    except FileNotFoundError:
            file_writing_mode = 'w'
    
    
    with open(filename,file_writing_mode, newline='') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=headers)
        
        if not file_exists:
            csv_writer.writeheader()
        csv_writer.writerows(account_list)

def main():
    show_intro()
    account = get_account_data()
    password_info = get_password_info()
    password = generate_password(password_info)
    password_api = api_verification(password)
    updated_account = update_account(account,password_api)
    show_output_in_terminal(updated_account)
    create_password_file(updated_account)
    
main()

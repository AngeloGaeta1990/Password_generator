import csv
import os
from classes.account import Account
from classes.password import Password

PASSWORD_CHARACTERS = 10
PASSWORD_NUMBERS = 2
PASSWORD_SPECIAL_CHARACTERS = 2
PASSWORD_UPPER_CASE_CHARACTERS = 2
MAX_PASSWORD_CHARACTERS = 100
ASCII_ART = r"""
███████║███████╗███████╗██╗   ██║██████╗ ███████╗
██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗██╔════╝
███████╗█████╗  ██║     ██║   ██║██████╔╝█████╗
╚════██║██╔══╝  ██║     ██║   ██║██╔══██╗██╔══╝
███████║███████╗╚██████╗╚██████╔╝██║  ██║███████╗
╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝
██████╗  ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
"""


def show_intro():
    """
    Show ASCII art and tool instructions and centers them
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    # ASCII_ART
    print(ASCII_ART)
    # Tool instructions
    prompt_instructions = "Press I for instructions, or press Enter to start"
    start_tool = (input(prompt_instructions + "\n"))
    start_tool = start_tool.lower()
    prompt_continue = "press Enter to continue"
    if start_tool == "i":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""
This tool will generate a secure password for the account of your
choice, e.g., Netflix.
The generated password will not be saved in the cloud to enhance
security. \n
By default the password generated will have the different features:\n
{PASSWORD_CHARACTERS} characters in total (max 100)\n
{PASSWORD_NUMBERS} numbers \n
{PASSWORD_SPECIAL_CHARACTERS} special characters \n
{PASSWORD_UPPER_CASE_CHARACTERS} capital letters \n
""")
        input(prompt_continue + "\n")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
These settings can be edited according to the user's preferences.\n
After generation, the password will be converted into a hash code.
The hash code will be sent to the PWNED API to verify that the
password has not been found in data breaches.\n
Follow the steps in the Terminal to generate the password
""")
        input(prompt_continue + "\n")


def get_account_data():
    """
    Creates the account class taking input from the user
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("Welcome to the Secure Password Generator")
        print("Please enter the service for which you need the password")
        print("Example: Netflix")
        service = input("Enter the name of the service here:\n")
        service = "Not provided" if len(service) < 1 else service
        print("Please enter the username")
        print("Example: my_email@provider.com or SecureUser")
        username = input("Enter the username here:\n")
        username = "Not provided" if len(username) < 1 else username
        print(f"You are a creating a password for {service} and your username"
              f"is {username}")
        else_account_approval = True
        os.system('cls' if os.name == 'nt' else 'clear')
        while else_account_approval:
            approval = input(f"Are the service {service} and username"
                             f" {username} correct? (yes or no)\n").lower()
            if approval == "yes" or approval == "y":
                account = Account(service, username)
                else_account_approval = False
                return account
            elif approval == "no" or approval == "n":
                else_account_approval = False
            else:
                print(f"You entered {approval} you should type yes or no")
                print("Please try again")


def get_password_info():
    """
    Generates password instance
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    no_confirmation = True
    print("This script will generate a random password including:\n")
    print(f"{PASSWORD_CHARACTERS} characters in total \n")
    print(f"{PASSWORD_NUMBERS} numbers \n")
    print(f"{PASSWORD_SPECIAL_CHARACTERS} special characters \n")
    print(f"{PASSWORD_UPPER_CASE_CHARACTERS} capital letters \n")
    while no_confirmation:
        approval = input("Do you want to keep the default"
                         " settings? (yes/no)\n").lower()
        if approval == "yes" or approval == "y":
            no_confirmation = False
            password = Password()
        elif approval == "no" or approval == "n":
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
            password_length = input(("How many total characters do you want"
                                     " in your password?"
                                     " (enter a number e.g.10)\n"
                                     " A maximum of 100 characters is allowed."
                                     " if your value is >100,\n"
                                     " a password of"
                                     " 100 characters characters will be"
                                     " generated\n"))
            password_length_int = int(password_length)
            password_length_int = (100 if password_length_int >
                                   100 else password_length_int)
        except ValueError:
            print(f"You entered {password_length},"
                  f" you should enter an integer number e.g. 10\n"
                  f" Let's try again.")
            break
        try:
            numbers_length = input(("How many numbers do you want in your"
                                    " password? (enter a number e.g.2)\n"))
            numbers_int = int(numbers_length)
        except ValueError:
            print(f"You entered {numbers_length},"
                  f" you should enter an integer number"
                  f" e.g. 10\nLet's try again.")
            break
        try:
            special_characters_length = input(("How many special characters"
                                               " do you want in your password?"
                                               " (enter a number e.g.2)\n"))
            special_characters_int = int(special_characters_length)
        except ValueError:
            print(f"You entered {special_characters_length},"
                  f" you should enter an integer number e.g. 10\n"
                  f" Let's try again.")
            break
        try:
            upper_case_length = input(("How many upper case letters"
                                       " do you want in your password?"
                                       " (enter a number e.g.2)\n"))
            upper_case_letters_int = int(upper_case_length)
        except ValueError:
            print(f"You entered {upper_case_length},"
                  f" you should enter a number e.g. 10\nLet's try again.")
            break
        validation = validate_new_password_settings(password_length_int,
                                                    numbers_int,
                                                    special_characters_int,
                                                    upper_case_letters_int)
        password = Password(password_length_int, numbers_int,
                            special_characters_int,
                            upper_case_letters_int) if validation else None
        return password


def validate_new_password_settings(password_length_int, numbers_int,
                                   special_characters_int,
                                   upper_case_letters_int):
    """
    checks if the special characters + numbers < password length
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    total_characters = (numbers_int +
                        special_characters_int +
                        upper_case_letters_int)
    if (total_characters <= password_length_int):
        return True
    else:
        print(f"You have selected {numbers_int} numbers, "
              f" {special_characters_int} special characters and "
              f" {upper_case_letters_int} upper case letters\n")
        print(f" resulting in a total of {total_characters} characters\n")
        print(f" this exceeds the desired password length of "
              f" {password_length_int} characters\n")
        print("Please try again")
        return False


def generate_password(password):
    """
    generate the password string, it generates numbers, special characters,
    upper and lower case letters list
    then shuffles the characters, show to the user the password and
    asks if it should be kept or a new one should be generated
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Generating password...")
    user_like = False
    while not user_like:
        password.builder()
        print(f"The password generated is\n {password.pwd}")
        user_decision = input("Do you want to keep this password? (yes/no)\n"
                              "(If 'no' a new password will be generated)"
                              "\n").lower()
        if user_decision == "yes" or user_decision == "y":
            user_like = True
        elif user_decision == "no" or user_decision == "n":
            pass
        else:
            while not (user_decision == "yes" or user_decision == "y" or
                       user_decision == "no" or user_decision == "n"):
                print(f"You entered {user_decision}, please enter yes or no")
                user_decision = input(f"Do you want to keep the password"
                                      f"{password.pwd}?"
                                      f" (yes/no)\n"
                                      f" (If 'no' a new password"
                                      f" will be generated)"
                                      f"\n").lower()
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
    if password.secure:
        account.secure = "Verified"
    return account


def show_output_in_terminal(account):
    """
    Print account info on the terminal
    """
    print(f"The data for the {account.service} account are below ")
    print(account.print_account())
    print("Please store this data in a secure and confidential location.")
    quit_input = input("Press Enter to generate a password"
                       " for a new Account or Q to quit\n").lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    quit_generator = True if quit_input == "q" else False
    return quit_generator


def create_password_file(account, filename="secure_passwords.csv"):
    """
    takes an account object in input
    and creates a .csv file listing Account, User name, Password and security
    """
    account_dict = account.account_dict()
    headers = account_dict.keys()
    account_list = [account_dict]
    file_exists = False
    try:
        with open(filename, 'r') as csv_file:
            existing_headers = next(csv.reader(csv_file))
            if existing_headers == list(headers):
                file_exists = True
                file_writing_mode = 'a'
    except FileNotFoundError:
        file_writing_mode = 'w'
    with open(filename, file_writing_mode, newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
        if not file_exists:
            csv_writer.writeheader()
        csv_writer.writerows(account_list)


def main():
    """
    Main function
    """
    quit_generator = True
    while True:
        show_intro() if quit_generator else None
        account = get_account_data()
        password_info = get_password_info()
        password = generate_password(password_info)
        password_api = api_verification(password)
        updated_account = update_account(account, password_api)
        quit_generator = show_output_in_terminal(updated_account)
        create_password_file(updated_account)


main()

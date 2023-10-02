# Secure Password Generator
---
## Site Overview:
----
The "Secure Password Generator" is a robust tool designed to empower users with the capability to generate exceptionally strong and highly secure passwords, all while addressing the growing concerns around password security in an increasingly digital age.

While services like LastPass and Google Passwords offer secure password storage, they inherently rely on online platforms, which can potentially be vulnerable to cyberattacks. The Secure Password Generator, on the other hand, provides an offline solution for users who prioritize ultimate security and control over their password creation process.

Live link to [Secure Password Generator](https://git.heroku.com/secure-password-generator.git)


![Secure Password Generator first prompt](/media/first_prompt.png)


## Table of Contents
---
- [Secure Password Generator](#secure-password-generator)
    - [Site Overview](#site-overview)
    - [Key Features and Benefits](#key-features-and-benefits)
    - [How to Generate a password](#how-to-generate-a-password)

---
## How to Generate a password
The user at first enters the account and the username 
As user name and account the user can add strings with no threshold to the length.
No verification is performed on this input as length and type of account can take which ever input type and leght,
![Account and user name promt](/media/user_and_account.png)

It then ask the user to verify that the info entered are correct.
The user input will be turned in lower case therefore `YES`, `Yes` and `yes` will all prompt the next step.

![Account and user name veirification](/media/user_and_account_verification.png)

if the answer is `no` or different from `YES`, `Yes`, or `yes` the user will be propted to re enter the service and user name.
Furthemore is the anwers is different from `yes` or `no`, the algorithm will tell the user that the options added are incorrect, will show the user the option inserted and will ask him to re-enter the username and service.
If instead the user just selects `no`, then no error will be shown, but the algorithm will prompt to reenter service and user name. 

![User name and service re-prompt](/media/username_and_service_reprompt.png)

if the user answer is yes then the tool will ask if the user wants to generate a passowrd with the defaul settings: 

- `10` total characters
- `2` numbers
- `2` special character
- `2` upper case letter

![Password with default settings](/media/default_password.png)

As per before the input of the user will be turned into lower case.
This time if the user selects yes then algorithm will generate a password with the default settings.

The user can choose if to keep this password or not.
As per before the user input is capitalized, then if the answer is yes the algorithm will proceed to the next steps if instead answer is no a new password will be generated with the same settings.

![Regenerate password](/media/regenerate_password.png)

if the user decide to not keep the default settings :
- total characters 
- numbers
- special character
- upper case letter

can be changed:


![Edit default settings](/media/change_default_settings.png)
Even in this case the use can choose if to keep the password or regenerate one using the same settings.
When setting are edited the algorithm verifies that sum of special charaters + numbers + upper case letters is <= than the total characters provided.
The lower case charaters to add are calculated as follows:
total chatacters - (special charaters + numbers + upper case letters)

if the condition special charaters + numbers + upper case letters is <= than the total characters is not met, and error is promptes showing the user which values have been used in input. 
Moreover, it also shows why the condition is not met.

![Invalid custom settings](/media/invalid_custom_settings.png)


## Key Features and Benefits:

- **Local Execution**: This tool operates exclusively at the local level, ensuring that your password generation process remains impervious to online threats. By running it locally on your own device, you eliminate the risk of your password data being exposed to the internet.

- **Python-Based Implementation**: The tool is meticulously crafted using the Python programming language, a renowned choice for its reliability and security. This ensures that the entire process is transparent, trustworthy, and under your direct supervision.

- **Enhanced Password Complexity**: By default, the Secure Password Generator crafts passwords with a length of 10 characters, comprising 2 numbers, 2 special characters, and 2 uppercase letters. This combination of character types and their random arrangement significantly amplifies password security.

- **Randomness and Unpredictability**: The tool ensures the unpredictability of generated passwords. It selects character types (lowercase/uppercase letters, numbers, special characters) and their order entirely at random, eliminating patterns that attackers could exploit.

- **Customization Options**: Users have the flexibility to tailor password settings to their unique requirements. You can easily adjust password length, the quantity of numbers, special characters, and uppercase letters to match specific service requirements or personal preferences.

- **Validation Checks**: The tool performs rigorous validation checks to ensure the correctness of user inputs. It verifies that the chosen password length is greater than or equal to the sum of special characters, numbers, and uppercase letters.

- **Hashed Password Verification**: To further bolster security, the generated password is converted into a hash code. Only the first 5 characters of this hash code are transmitted to the PWNED API, which offers a method to verify if a password has been compromised in data breaches. This process ensures your passwords remain untainted by known security breaches.

- **Error Handling**: The tool is equipped to handle contingencies gracefully. It will notify you if the API connection fails or if the password has been compromised in data breaches. You have the option to regenerate a new password for added peace of mind.

- **User-Friendly Output**: Upon generating a secure password, the tool exports the results to a .csv file named "secure_password.csv." This file contains fields for the account (e.g., Netflix), user identifier (user or user@mail.com), the generated password (e.g., mY_r8nd0m_pwd!), and a verification status indicating whether the password has been PWNED or not.

- **Ultimate Privacy**: Rest assured that the generated .csv file remains completely confidential and is not accessible on Heroku or any online platform, ensuring your password data is for your eyes only.
---

## Bugs fixing
---
1. **Error**: If the user enters the wrong setting in "How many total characters?", it moves to the next question.
**Solution**: Added a break statement at the end of each try.

2. **Error**: Formulation of "Please enter the service you need the password for."
**Solution**: Corrected the wording.

3. **Error**: Formulation of "You selected 8 numbers and 8 special characters. 8 numbers + 8 special characters are 16 total characters. 16 total characters are longer than the password length of 1."
**Solution**: Corrected to: "You have selected 8 numbers and 8 special characters, resulting in a total of 16 characters. This exceeds the desired password length of 1 character."

4. **Error**: Infinite loop if the user edits password settings.
**Solution**: If a password is returned, no_confirmation becomes false.

5. **Error**: TypeError: Mixin.generate_random_numbers() takes 1 positional argument but 2 were given.
**Solution**: Added self into def generate_random_numbers(self, amount).

6. **Error**: def generate_random_special_characters in mixin returns a boolean rather than values.
**Solution**: Replaced list comprehension with random.sample.

7. **Error**: The developer forgot to differentiate between lowercase and uppercase letters for passwords.
**Solution**: Uppercase letters will be added to customization alongside special characters and numbers, which have already been added.

8. **Error**: During input acquisition, the special characters variable was set to take input from the number variable.
**Solution**: Assigned the variable to special_characters correctly.

9. **Error**: account_dict = account.account_dict() AttributeError: 'function' object has no attribute 'account_dict'.
**Solution**: Rather than a variable, a function was set as input.

10. **Error**: heroku module not found.
**Solution**: Update requirements.txt.

11. **Error**: secure_passwords.csv reported in GitHub.
**Solution**: The .gitignore file contains a typo in the filename.

12. **Error**: Even if invalid settings are provided a password is generated
    **Solution**: To move password variable otuside the while caused the password to be generated only if validation criteria are met

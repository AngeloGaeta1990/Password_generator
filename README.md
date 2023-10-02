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

1. ### Enter Account and Username
   The user begins by entering their account name and username. These fields can accept strings of any length and type without verification.
   ![Account and Username Prompt](/media/user_and_account.png)  

2. ### Verify Input:
   The tool asks the user to verify that the entered information is correct. The user's response is converted to lowercase, so `YES`, `Yes`, and `yes` are all accepted.

   ![Verification](/media/user_and_account_verification.png)

   If the answer is anything other than `yes`, the user is prompted to re-enter the service and username. If the response is neither `yes` nor `no`, the algorithm informs the user of the incorrect option, displays the options inserted, and asks for a username and service re-entry.
   If the answer is `no`, no error message is displayed, but the tool prompts the user to re-enter the service and username.

3. ### Generate Password with Default Settings:

     If the user's response is `yes`, the tool asks if the user wants to generate a password with default settings:

     - `10` total characters
     - `2` numbers
     - `2` special characters
     - `2` uppercase letters

     ![Default password settings](/media/default_password.png)  

     - If the user selects "yes" again, the algorithm generates a password with the default settings.
     - The user can choose whether to keep this password. If they answer "yes," the algorithm proceeds to the next steps. If they answer "no," a new password is generated with the same default settings.

4. ### Edit Default Settings:

   If the user decides not to keep the default settings, they can edit the following parameters:

   - Total characters
   - Number of numbers
   - Number of special characters
   - Number of uppercase letters


    ![Edit default settings](/media/change_default_settings.png)  

  - Even in this case, the user can choose whether to keep the edited password settings.
  - When settings are edited, the algorithm checks that the sum of special characters, numbers, and uppercase letters does not exceed the total character count.
  - The lowercase characters to add are calculated as follows: `total characters - (special characters + numbers + uppercase letters)`
  - If the condition `special characters + numbers + uppercase letters <= total characters` is not met, an error is prompted, showing the user the input values and the reason for the error.

    ![Invalid custom settings](/media/invalid_custom_settings.png)

5. ### Password Security Check: 
    If the user decides to keep the password, the algorithm queries the Pwned API. It generates a hash code containing only the first 5 characters of the password and searches the API results for a matching prefix.

    - If the suffix of the password appears in the API results, a message indicating that the password has been breached is displayed.
    - If no suffix is found in the results, a message stating that the password is secure is shown.
    - If there is an error reaching the API, the algorithm reports that the API could not be reached, and the password is not flagged as secure.


    ![Secure password](/media/secure_password_generated.png)

6. ### Save Password Information

    Finally, the service, username, password, and password validation are saved to a .csv file named "secure_password.csv." If the file doesn't exist, a new one is created. If "secure_password.csv" already exists, a new line is added to the file.

    ![secure_password.csv](/media/secure_password_csv.png)

    - Note that the file may not be accessible via a live link due to the deployment on Heroku. Users who clone the repository on their device will be able to view and manipulate the file.


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

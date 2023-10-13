# Secure Password Generator

---

## Site Overview

---
The "Secure Password Generator" is a robust tool designed to empower users with the capability to generate strong and highly secure passwords, all while addressing the growing concerns around password security in an increasingly digital age.

While services like LastPass and Google Passwords offer secure password storage, they inherently rely on online platforms, which can potentially be vulnerable to cyber-attacks.On the other hand, the Secure Password Generator provides an offline solution for users who prioritize ultimate security and control over their password creation process.

Live link to [Secure Password Generator](https://secure-password-generator-618a9b17c80c.herokuapp.com/)

![Secure Password Generator logo ASCII art](/media/logo_ascii_art.png)

## Table of Contents

---

- [Secure Password Generator](#secure-password-generator)
  - [Site Overview](#site-overview)
  - [Table of Contents](#table-of-contents)
  - [Planning Phase](#planning-phase)
    - [Target Audience](#target-audience)
    - [Aim](#aim)
    - [Achievements](#achievements)
    - [Flow chart](#flow-chart)
  - [Features](#features)
    - [How to Generate a password](#how-to-generate-a-password)
  - [Key Features and Benefits](#key-features-and-benefits)
  - [Future-Enhancements](#future-enhancements)
  - [Data model](#data-model)
    - [Classes](#classes)
    - [Account Class](#account-class)
    - [Password Class](#password-class)
    - [Mixins Classes](#mixins-classes)
  - [Libraries](#libraries)
  - [Testing](#testing)
  - [Bugs fixing](#bugs-fixing)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
    - [Local](#local)
  - [Credits](#credits)

 ---

## Planning Phase

---

### Target Audience

- Users who lack confidence in online password management services like LastPass or Google Password.
- Users who are concerned about sending their credentials online and prefer to store them locally on their devices
- Users who are already familiar with using Github.
- Users can generate a limited number of strong passwords, particularly for sensitive accounts like bank accounts while relying on services like LastPass or Google Password for less critical services.

### Aim

1. Enhance password generation customization: Enable users to specify password length, character types (e.g., letters, numbers, symbols), and other criteria to create passwords that meet their specific security requirements.
1. Offline mode: Allow users to generate passwords even when not connected to the internet, ensuring the tool's functionality in offline environments.
1. Develop a reliable command-line interface (CLI) tool for effective user input handling and validation.
1. Establish API integration: Create a tool that can interact seamlessly with external APIs to enhance functionality.

### Achievements

1. The user can fully customize the password by changing its length, amount of numbers, special characters, and upper and lower case letters.
1. The user can deploy the repository locally and save the password and the username for the service of choice in a .csv file.
1. The tool checks if the password is in the data breach list by using the PWNED API method.
1. The tool is responsive and provides an easy walkthrough to the user. It handles errors efficiently and guides the user in the resolution.

### Flow chart

![Algorithm flow chart](/media/pwd_generator.png)

## Features

### How to Generate a password

1. ### First Screen

    At first, the user can see the *Secure Password Generator* ASCII art logo.
    ![Secure Password Generator logo ASCII art](/media/logo_ascii_art.png)  
    Then, the algorithm prompts the user to type I or i to see the instructions

    ![Instructions part1](/media/instructions_part_1.png)  
    ![Instructions part2](/media/instructions_part_2.png)  
    or to press `Enter`to start generating a password.

2. ### Enter Account and Username

   The user has to enter their account name and username. These fields can accept strings of any length and type without verification.
   ![Account and Username Prompt](/media/user_and_account.png)  

3. ### Verify Input

   The tool asks the user to verify that the entered information is correct. It converts the user response to lowercase, so `YES`, `Yes`, `yes` and `y` are all accepted.

   ![Verification](/media/user_and_account_verification.png)

   If the answer is anything other than `yes`, the user is prompted to re-enter the service and username. If the response is neither `yes` nor `no`, the algorithm informs the user of the incorrect option, displays the options inserted, and asks for a username and service re-entry.
   If the answer is `no`, no error message is displayed, but the tool prompts the user to re-enter the service and username.

4. ### Generate Password with Default Settings

     If the user's response is `yes`, the tool asks if the user wants to generate a password with default settings:

     - `10` total characters
     - `2` numbers
     - `2` special characters
     - `2` uppercase letters

     ![Default password settings](/media/default_password.png)  

     - If the user selects `yes` again, the algorithm generates a password with the default settings.
     - The user can choose whether to keep this password. If they answer `yes`, the algorithm proceeds to the next steps. If they answer `no`, a new password is generated with the same default settings.

5. ### Edit Default Settings

   If the user decides not to keep the default settings, they can edit the following parameters:

   - Total characters
   - Number of numbers
   - Number of special characters
   - Number of uppercase letters

    ![Edit default settings](/media/change_default_settings.png)  

   - Even in this case, the user can keep the new settings.
   - When the user edits the settings, the algorithm checks that the sum of `special characters`, numbers, and uppercase letters does not exceed the total character count.
   - The lowercase characters to add are calculated as follows: `total characters - (special characters + numbers + uppercase letters)`
   - If the condition `special characters + numbers + uppercase letters <= total characters` is not met, the algorithm prompts an error, showing the user the input values and the reason for the error.

    ![Invalid custom settings](/media/invalid_custom_settings.png)

6. ### Password Security Check

    If the user decides to keep the password, the algorithm queries the Pwned API. It generates a hash code containing only the first five characters of the password and searches the API results for a matching prefix.

    - If the password suffix appears in the API results, a message indicating that the password is present in the list of unsafe passwords appears.
    - If the suffix is absent in the API results, the algorithm shows a message stating that the password is secure.
    - If the algorithm can not reach the PWNED API, it reports it and marks the password as "not verified".

    ![Secure password](/media/secure_password_generated.png)

7. ### Save Password Information

    Finally, the algorithm saves service, username, password, and password validation in a .csv file named "secure_password.csv." If the file doesn't exist, it creates a new one. If "secure_password.csv" already exists,  it adds a new line to the file.

    ![secure_password.csv](/media/secure_password_csv.png)

    - Note that the file may not be accessible via the live link due to the deployment on Heroku. Users who clone the repository on their device can view and manipulate the file.

8. ### Print Account Information

    The algorithm also prints the service, username, password, and password validation in a table format on the terminal.
    In this manner, even if the user does not deploy locally, he can still view the information clearly and copy-paste it to a secure location.
    ![Terminal output](/media/terminal_output.png)

## Key Features and Benefits

- **Local Execution**: This tool operates exclusively locally, ensuring that the user password generation process remains impervious to online threats. Therefore, it does not expose the password to the internet.

- **Python-Based Implementation**: I implemented this tool using Python as the programming language, renowned for its reliability and security. Therefore, the entire process is transparent, and trustworthy.

- **Enhanced Password Complexity**: By default, the Secure Password Generator generates a password with a ten-character length, including two numbers,  two "special characters", and two uppercase letters. This combination of character types and their random arrangement significantly amplifies password security.

- **Randomness and Unpredictability**: The tool ensures the unpredictability of generated passwords. It selects character types (lowercase/uppercase letters, numbers, special characters) and their order entirely at random, eliminating patterns that attackers could exploit.

- **Customization Options**: Users have the flexibility to tailor password settings to their unique requirements. They can easily adjust password length, the amount of numbers, special characters, and uppercase letters to match specific service requirements or personal preferences.

- **Validation Checks**: The tool performs rigorous validation checks to ensure the correctness of user inputs. It verifies that the chosen password length is greater than or equal to the sum of "special characters", numbers, and uppercase letters.

- **Hashed Password Verification**: The algorithm further bolsters security by converting the generated password into a hash code. It only transmits the first five characters of this hash code to the PWNED API, which offers a method to verify if a password is compromised. This process ensures user passwords remain untainted by known security breaches.

- **Error Handling**: The tool handles contingencies gracefully. It will notify the user if the API connection fails or the password is not secure. The user has the option to regenerate a new password.

- **User-Friendly Output**: Upon generating a secure password, the tool exports the results to a .csv file named "secure_password.csv." This file contains fields for the account (e.g., Netflix), a user identifier (user or [E-mail Address](user@mail.com)), the generated password (e.g., mY_r8nd0m_pwd!), and a verification status indicating whether the password is secure or not.

- **Ultimate Privacy**: Rest assured that the generated .csv file remains completely confidential and is not accessible on Heroku or any online platform, ensuring user password data is for the user's eyes only.

---

## Future-Enhancements

---

- Implement a system to assess password complexity.
- Provide the option to input data via command line arguments rather than relying solely on a command prompt.
- Integrate synchronization with Google Docs or OneDrive.

## Data model

---

### Classes

I decided to use a Python object-oriented programming approach, and I've used the following classes and attributes:

### Account Class

It represents an account for a service provider.

**Attributes:**

- `service` (str): name of the service provider.
- `username` (str): The username used to access the service. It can be an email address or not.
- `password` (str): The password generated by this algorithm (initialized as None).
- `secure` (str): A string that can have the values "Verified" or "Not verified," indicating whether the algorithm has checked the PWNED API for data breaches (initialized as "Not verified").

### Password Class

It represents a password and its generation parameters.

**Parameters:**

- `length` (int, optional): The length of the password (default 10).
- `numbers_length` (int, optional): The number of digits to include in the password (default 2).
- `special_characters_length` (int, optional): The number of "special characters" to include in the password (default 2).
- `upper_case_length` (int, optional): The number of uppercase letters to include in the password (default 2).

**Attributes:**

- `length` (int): The length of the password.
- `numbers_length` (int): The number of digits to include in the password.
- `special_characters_length` (int): The number of "special characters" to include in the password.
- `upper_case_length` (int): The number of uppercase letters to include in the password.
- `lower_case_length` (int): The number of lowercase letters to include in the password, calculated as `length - (numbers_length + special_characters_length + upper_case_length)`.
- `pwd` (str): The generated password (initialized as None).
- `number_list` (list): A list of 1-digit integers to include in the password (initialized as an empty list).
- `special_characters_list` (list): A list of special characters to include in the password (initialized as an empty list).
- `upper_case_list` (list): A list of uppercase letters to include in the password (initialized as an empty list).
- `lower_case_list` (list): A list of lowercase letters to include in the password (initialized as an empty list).
- `hash_code` (str): The password hashed into a code (initialized as None).
- `prefix` (str): The first five characters of the hash code (initialized as None).
- `secure` (bool): True if the API reported that the password is secure, False otherwise, and None if there is no API response.

### Mixins Classes

The mixins file contains a class for each function.
Each function is generic, and developers can import them outside this project context. It also simplifies future enhancements, as new classes can inherit them.

- **NumbersMixin**: Generates a list of random numbers
- **SpecialCharactersMixin**: Generates a list of random special characters
- **UpperCaseLettersMixin**: Generates a list of random upper-case letters
- **LowerCaseLettersMixin**: Generates a list of random lowercase letters

## Libraries

- **csv**: Utilized for creating the output file secure_passwords.csv, which contains information such as service name, username, password, and password security verification.

- **hashlib**: Utilized to convert passwords into hash codes, enhancing security.

- **os**: Used to clear terminal when appropriate.

- **random**: Employed to generate a random list of upper and lower case characters, numbers, and special characters.  

- **requests**: Used for making HTTP requests, especially to access the PWNED API for checking password breaches.

- **string**: Utilized to generate random "strings" composed of letters, often used for generating random passwords.  

- **tabulate**: Used to print the account, username, password, and password verification in the terminal in a table format.

## Testing

---

1. **Prompt**: Press I for instructions, or press Enter to start  
    **Tests**:
    - Letters different from `I` or `i`, numbers, and special characters did not trigger any action until the user pressed the `Enter` key.
    - The algorithm shows the instructions when the user presses `I` or `i` followed by the `Enter` key.
1. **Prompt**: Follow the steps in the Terminal to generate the password press Enter to continue.  
    **Tests**:
    - The developer tested different letters, numbers, and special characters. The algorithm shows the new prompt only when the user presses the `Enter` key.
1. **Prompt**: Enter the name of the service here: and Enter the name of the service here:
   **Tests**:
   - Tested with numbers, special characters, and spaces, it returned the expected behavior.
1. **Prompt**: Are the service s and username s correct? (yes or no)  
   **Tests**:
   - Special characters, spaces, and numbers caused the repetition of the prompt.
   - The new prompt was triggered only by `y`, `Y`, `YES`, `Yes`, and `yes`.
   - `n`, `N`, `NO`, `No`, and `no` triggered re-entering of the account and username.
1. **Prompt**: Do you want to keep the default settings? (yes/no)  
   **Tests**:
   - Special characters, spaces, and numbers caused the repetition of the prompt.
   - The inputs `y`, `Y`, `YES`, `Yes`, and `yes` caused the generation of a password.
   - `n`, `N`, `NO`, `No`, and `no` triggered editing of default settings  
1. **Prompt**: How many total characters do you want in your password?  
   **Tests**:
   - Set the total characters to `5000` and the special characters, numbers, and uppercase letters to `34`.  it resulted in validation failure due to: `34 * 3 = 102` and `102 > 100`.
   - Set the total characters, special characters, numbers, and uppercase letters to `0`. It resulted in an empty string password.  
   - Set the total characters to `100` and special characters, numbers, and uppercase letters to `25`. The algorithm generated the password as regular.
   - Set the total characters to `5000`, "special characters" to `40`, and numbers and uppercase letters to `10`.
    The algorithm generated a password of `100` characters, as expected.
   - Set the total characters to `30`, numbers to `30`, and special characters and uppercase letters to `0`. The algorithm generated a password of `30` numbers, as expected.
1. **Prompt**: Do you want to keep this password? (yes/no)  
   **Tests**:
     - Special characters, spaces, and numbers caused the repetition of the prompt.
     - `n`, `N`, `NO`, `No`, and `no` triggered editing of default settings and a new password generation.
     - `y`, `Y`, `YES`, `Yes`, and `yes` prompted API verification.
1. **Prompt**: Press Enter to generate a password for a new Account  
     **Test**:
     - Special characters, spaces, and numbers did not trigger any new prompts.
     - Pressing Enter caused the algorithm to restart as expected.

1. Test in Python Linter returned no issue.

## Bugs fixing

---

1. **Issue**: When the user enters an incorrect setting for "How many total characters?" The program proceeds to the next question.
**Solution**: The developer added a break statement at the end of each try block to prevent moving forward on incorrect input.
1. **Issue**: Incorrect wording of the sentence: "Please enter the service you need the password for."  
**Solution**: The developer clarified and corrected the wording for better user understanding.
1. **Issue**: Inaccurate message: "You selected 8 numbers and 8 special characters. 8 numbers + 8 special characters are 16 total characters. 16 total characters are longer than the desired password length of 1."  
**Solution**: Revised to: "You have chosen 8 numbers and 8 special characters, resulting in a total of 16 characters. This exceeds the specified password length of 1 character."
1. **Issue**: An infinite loop occurs when the user modifies password settings.  
**Solution**: The developer implemented a condition in the `get_password_info()` function that terminates the while loop once the algorithm generates a password.  
1. **Issue**: Calling `Mixin.generate_random_numbers()` resulted in the error:

    ```python
    TypeError: "Mixin.generate_random_numbers() takes 1 positional argument, but 2 were given."
    ```

    **Solution**: The developer updated the method signature to include self as the first argument: `def generate_random_numbers(self, amount)`.
1. **Issue**: Function `Mixin.generate_random_special_characters()` returns a boolean instead of a list of characters.  
**Solution**: The developer replaced list comprehension with `random.sample` to correctly generate special characters.
1. **Issue**: Lack of differentiation between lowercase and uppercase letters in generated passwords.  
 **Solution**: The developer added support for uppercase letters in password customization alongside special characters and numbers.  
1. **Issue**: Special characters were mistakenly receiving the input intended for the number of characters.  
**Solution**: The developer reassigned the variable to accept the input intended for special characters.
1. **Issue**: An error occurred when calling the `account_dict()` class method.:

    ```python
    account_dict = account.account_dict()
                    ^^^^^^^^^^^^^^^^^^^^
    AttributeError: 'function' object has no attribute 'account_dict'
    ```

    The error resulted from mistakenly treating `account_dict` as a variable rather than invoking it as a function.
**Solution**:  The developer corrected the usage by invoking the function as `account.account_dict()`.

1. **Issue**: When deploying on Heroku, the following error occurred: "Module not found."  
**Solution**: The developer updated the 'requirements.txt' file to include the necessary dependencies.
1. **Issue**: There was a mention of 'secure_passwords.csv' in GitHub, caused by a typo in the filename when added to the .gitignore file.  
**Solution**: The developer corrected the filename typo within the .gitignore file to prevent any reference to 'secure_passwords.csv' on GitHub.
1. **Issue**: The algorithm generates a password even if the user provides invalid settings,  e.g. the total length of the password is < numbers amount + special characters amount + upper case amount.  
**Solution**: The developer moved the password generation outside the while loop in the `edit_password_default()` function. Therefore, the algorithm generates the password only if there is validation.
1. **Issue**: When the function `self.account_dict` was called within the function `print_account`, the following error was returned:

    ```python
    Error:
        table = tabulate(table_data.items(), headers=["Field", "Value"], tablefmt="grid")
                            ^^^^^^^^^^^^^^^^
        AttributeError: 'function' object has no attribute 'items'
    ```

    **Solution**: The function was called as an attribute rather than as a function.
    To resolve the issue, replace `self.account_dict` with `self.account_dict()`.

1. **Issue**: After adding the tabulate module to the requirements.txt file and deploying the application on Heroku, the following error occurred:

    ```python
        ModuleNotFoundError: No module named 'tabulate'
    ```

    **Solution**:  The issue was caused by activating a virtual environment using Conda, which resulted in a local path added to requirements.txt. To resolve the issue, create a separate virtual environment using Python instead of Conda. The latter will ensure that requirements.txt lists all dependencies correctly, and Heroku will install them during the deployment without issues.
1. **Issue**: The following error was returned by the function `edit_password_default` when user input did not meet the criteria to generate a password, for example, when the number of characters exceeds the total password length:

    ```python
                Error:
                UnboundLocalError: cannot access local variable 'password_length_int' where it is not associated with a value
                when assigning letter to password length
    ```

    **Solution**:  In the `edit_password_default` function, the `password` variable is defined outside the `while` loop. Therefore, the algorithm generates it, even if there is no validation. To resolve the issue, the developer added an `if` statement to create a password only when there is a validation. The latter ensures that the `password` variable is only assigned a value when the criteria are satisfied.

1. **Issue**: There was too much space separating terminal prints.

    **Solution**: The issue was caused by using a backslash \ to separate long strings, resulting in extra space. To resolve it, you can either use a new f"" or close and start a new "", for example:

    ```python
        print("My very"
                " long string") 
    ```

1. **Issue**:  There was an infinite loop in the `generate_password function`. The developer implemented a while loop within the `else` statement to wait until the user's answer was either `yes` or `no` before generating or using a password. However, even if the user entered `yes` or `no`, the loop continued to repeat.  
**Solution**: Replace the following condition:

    ```python
        while (user_decision != "yes" or user_decision != "y" or
                        user_decision != "no" or user_decision != "n"):
    ```

    With this condition:

    ```python
        while not (user_decision == "yes" or user_decision == "y" or
                        user_decision == "no" or user_decision == "n"):
    ```

    The corrected condition ensures that the loop will exit when the user enters `yes`,`y`,`no`, or `n`, resolving the issue of the infinite loop.

1. **Issue**: Passwords were always showing as not verified.  
**Solution**: During the restyling of the code to meet flake8 rules, the developer in function `update_account`added `not password.secure` instead of just `password.secure`. To resolve the issue, remove the `not` keyword.
1. **Issue**: Selecting more than `30` special characters resulted in an error.  
**Solution**:  Replace `random.sample` with `random.choices` in the `generate_random_special_characters` function. Using `random.choices` allows the user to select more characters than the length of the list of special characters.
1. **Issue**: The developer cloned this repository on a different device. When he pushed the commit, he did not realize he had logged in to GitHub with a different account. Therefore, two contributors appeared in the repository.
**Solution**: The developer performed a git hard reset to the last commit of the repository contributor. After two days, two contributors still appeared in the repository, suggesting that the issue was unrelated to the GitHub cache. The developer deleted the second account from Github, and the second contributor disappeared.

## Deployment

---

### Heroku

The deployment has been performed on Heroku as follows:

1. **Create a Heroku Account:**
If you don't have a Heroku account, sign up for one at Heroku's website.
1. **Log In to Heroku:**
Log in to your Heroku account using your credentials.
1. **Access Heroku Dashboard:**
After logging in,  the website will direct you to your Heroku dashboard.
1. **Create a New App:**
To deploy your GitHub repository on Heroku, click the "New" button on the top right corner of the dashboard and select "Create new app."
1. **Name Your App:**
Choose a unique name for your app. If you have a specific one in mind, enter it in the "App name" field. Otherwise, Heroku will suggest a name for you.
1. **Choose a Region:**
Select the region closest to your intended audience or location. The latter determines the data centre where to host your app. Click the "Create app" button when you're ready.
1. **Connect to GitHub:**
In your app's dashboard, go to the "Deploy" tab. In the "Deployment method" section, choose "GitHub."
1. **Add Config Vars:**
On the "Deploy tab", navigate to the "Settings" tab.
Scroll down to the "Config Vars" section and click the "Reveal Config Vars" button, then add a new configuration variable by entering "port" as the key and "8000" as the value, then click "Add."
1. **Buildpacks**
On the "Settings" tab, scroll down to the "Buildpacks" section and click the "Add buildpack" button.
Select "Python" as the buildpack and save your changes.
Repeat this step and add "node.js" as the "buildpack" instead of Python.
1. **Buildpacks verification**
Ensure that the "buildpacks" are in the correct order. If "node.js" is listed first, you can drag "Python" upwards to make it the first "buildpack" in the list.
1. **Authorize Heroku to Access GitHub:**
On the "Deploy tab", click the "Connect to GitHub" button. Heroku will ask for permission to access your GitHub repositories. Authorize Heroku to access your GitHub account.
1. **Search for Your GitHub Repository:**
After authorization, you can search for your GitHub repository by entering its name in the search box. Once you find it, click the "Connect" button (next to your Github repo).
1. **Set Up Automatic or Manual Deployment:**
Heroku provides two deployment options:
    - **Automatic Deploys:** Heroku will deploy the latest version automatically whenever you push changes to your GitHub repository.
    - **Manual Deploy:** You can manually choose a branch to deploy. The latter helps in controlling when updates go live.
1. **Choose Your Deployment Branch**:
If you selected manual deployment, choose the branch you want to deploy from the dropdown menu.
1. **Deploy Branch:**
Click the "Deploy Branch" button (for manual deployment) or "Enable Automatic Deploys" (for automatic deployment). Heroku will initiate the deployment process, which may take a few minutes.
1. **View Deployment Logs:**
You can monitor the deployment process by clicking the "View" button in the "Build log" section.
1. **Access Your Deployed App:**
Once the deployment is successful, you can access your deployed app by clicking the "Open app" button at the top of the page.

### Local

Clone this repository locally to enable the generation of the 'secure_password.csv' file containing the list of created accounts and generated passwords.
To have this repository on your local machine, follow these steps:"  

1. **Open a Terminal (or Command Prompt)**:
On your local machine, open a terminal or command prompt. You'll use this to enter commands.
1. **Navigate to Your Desired Directory:**
Use the `cd` (change directory) command to navigate to the directory where you want to create the virtual environment and clone the GitHub repository. For example:

    ```cmd

    cd /path/to/your/directory
    ```

1. **Create a Virtual Environment:**
Use the following command to create a virtual environment.

    ```cmd
    python -m venv pwd_generator
    ```

    This command will create a virtual environment named `pwd_generator` in the current directory.
1. **Activate the Virtual Environment:**
To activate the virtual environment, use the appropriate command based on your operating system:
    - On Windows:

        ```cmd
        pwd_generator\Scripts\activate
        ```

    - On macOS and Linux

        ```bash
        source pwd_generator/bin/activate
        ```

1. **Install Git** (if not already installed):
    If you did not install Git on your system,  you can download and install it from the official Git website: [Git download](https://git-scm.com/downloads)  
1. **Clone the GitHub Repository:**
    Use the git clone command to clone the GitHub repository.

    ```cmd
    git clone https://github.com/AngeloGaeta1990/Password_generator.git
    ```

   This command will download the repository files to your current directory.
1. **Navigate to the Cloned Repository Directory:**
    Use the `cd` command to navigate into the cloned repository directory:
  
    ```cmd
    cd Password-generator
    ```

1. **Install Libraries from requirements.txt:**
    Use the `pip install -r` command to install the libraries listed in the requirements.txt file.

    ```cmd
    pip install -r requirements.txt
    ```

    This command will install all the required libraries and dependencies specified in the requirements.txt file within your virtual environment.
1. **Deactivate the Virtual Environment:**
    When you want to stop the virtual environment, you can deactivate it using the following command:

    ```cmd
    deactivate
    ```

    The latter will bring you back to the global Python environment.

## Credits

Great thanks to:

- [Lucidchart](https://www.lucidchart.com/pages/) for the generation of the Diagram
- [Code institute](https://codeinstitute.net/) for providing the template used in this project
- [Chatgpt](https://openai.com/blog/chatgpt) for assisting in troubleshooting and proofreading
- [PWNED](https://haveibeenpwned.com/) for providing the API method to verify if a password is secure.
- [textkool](https://textkool.com/en/ascii-art-generator?hl=default&vl=default&font=Red%20Phoenix&text=Your%20text%20here%20) for the generation of ASCII art.
- [David Bowers](https://github.com/dnlbowers) for assisting in shaping the project and providing the motivation to move forward.

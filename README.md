# Secure Password Generator
---
## Site Overview:
----
The "Secure Password Generator" is a robust tool designed to empower users with the capability to generate exceptionally strong and highly secure passwords, all while addressing the growing concerns around password security in an increasingly digital age.

While services like LastPass and Google Passwords offer secure password storage, they inherently rely on online platforms, which can potentially be vulnerable to cyberattacks. The Secure Password Generator, on the other hand, provides an offline solution for users who prioritize ultimate security and control over their password creation process.

Live link to [Secure Password Generator](https://secure-password-generator-618a9b17c80c.herokuapp.com/)


![Secure Password Generator first prompt](/media/first_prompt.png)


## Table of Contents
---
- [Secure Password Generator](#secure-password-generator)
    - [Site Overview](#site-overview)
- [Planning Phase](#planning-phase)
    - [Target audience](#target-audience)
    - [Aims](#aims)
    - [Flow chart](#flow-chart)
- [Features](#features)
    - [How to Generate a password](#how-to-generate-a-password)
    - [Key Features and Benefits](#key-features-and-benefits)
- [Future Enhancements](#future-enhancements)
- [Data Model](#data-model)
   - [Classes](#classes)
   - [Libraries](#libraries)
- [Testing](#testing)
- [Deployment](#deployment)
   - [Heroku](#heroku)
   - [Local](#local)
- [Credits](#credits)

    
       

 ---

## Planning Phase
---
### Target Audience
 - Users who lack confidence in online password management services like LastPass or Google Password.
- Users who have concerns about sending their credentials online and prefer to store them locally on their devices.
- Users who are already familiar with using Github.
- The tool can also be used solely for generating a limited number of strong passwords, particularly for sensitive accounts like bank accounts, while relying on services like LastPass or Google Password for less critical services.

### Aim
1. Enhance password generation customization: Enable users to specify password length, character types (e.g., letters, numbers, symbols), and other criteria to create passwords that meet their specific security requirements.
2. Offline mode: Allow users to generate passwords even when they are not connected to the internet, ensuring the tool's functionality in offline environments.
3. Develop a reliable command-line interface (CLI) tool for effective user input handling and validation.
4. Establish API integration: Create a tool that can interact seamlessly with external APIs to enhance its functionality

### Flow chart

![Algorithm flow chart](/media/pwd_generator.png)

## Features
### How to Generate a password

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

## Future-Enhancements
---
- Implement a system to assess password complexity.
- Provide the option to input data via command line arguments, rather than relying solely on a command prompt.
- Integrate synchronization with Google Docs or OneDrive.

## Data model
---
### Classes
I decided to use a Python object-oriented programming approach and I've used the following classes and attributes:
### Account Class

Represents an account for a service provider.

**Attributes:**

- `service` (str): The name of the service provider.
- `username` (str): The username used to access the service, which can be an email address or not.
- `password` (str): The password generated by this algorithm (initialized as None).
- `secure` (str): A string that can have the values "Verified" or "Not verified," indicating whether the algorithm has checked the PWNED API for data breaches (initialized as "Not verified").

### Password Class

Represents a password and its generation parameters.

**Parameters:**

- `length` (int, optional): The length of the password (default 10).
- `numbers_length` (int, optional): The number of digits to include in the password (default 2).
- `special_characters_length` (int, optional): The number of special characters to include in the password (default 2).
- `upper_case_length` (int, optional): The number of uppercase letters to include in the password (default 2).

**Attributes:**

- `length` (int): The length of the password.
- `numbers_length` (int): The number of digits to include in the password.
- `special_characters_length` (int): The number of special characters to include in the password.
- `upper_case_length` (int): The number of uppercase letters to include in the password.
- `lower_case_length` (int): The number of lowercase letters to include in the password, calculated as `length - (numbers_length + special_characters_length + upper_case_length)`.
- `pwd` (str): The generated password (initialized as None).
- `number_list` (list): A list of 1-digit integers to include in the password (initialized as an empty list).
- `special_characters_list` (list): A list of special characters to include in the password (initialized as an empty list).
- `upper_case_list` (list): A list of uppercase letters to include in the password (initialized as an empty list).
- `lower_case_list` (list): A list of lowercase letters to include in the password (initialized as an empty list).
- `hash_code` (str): The password hashed into a code (initialized as None).
- `prefix` (str): The first 5 characters of the hash code (initialized as None).
- `secure` (bool): True if the API reported that the password has not been found in data breaches, False otherwise, and None if there is no API response.

### Mixin Class

A mixin class with common methods that can be applied to other classes.

**Methods:**

- `common_method()`: A common method that can be used by other classes.
 
## Libraries
- **csv**: Utilized for creating the output file secure_passwords.csv, which contains information such as service name, username, password, and password security verification.

- **random**: Employed to generate a random list of both upper and lower case characters, numbers, and special characters.

- **hashlib**: Utilized to convert passwords into hash codes, enhancing security.

- **requests**: Used for making HTTP requests, especially to access the PWNED API for checking password breaches.

- **string**: Utilized to generate random strings composed of letters, often used for generating random passwords.

## Testing
---
## Bugs fixing
---
1. **Issue**: When the user enters an incorrect setting for "How many total characters?", the program proceeds to the next question.
**Solution**: Added a break statement at the end of each try block to prevent moving forward on incorrect input.
2. **Issue**: Incorrect wording in "Please enter the service you need the password for."
**Solution**: Clarified and corrected the wording for better user understanding.
3. **Issue**: Inaccurate message: "You selected 8 numbers and 8 special characters. 8 numbers + 8 special characters are 16 total characters. 16 total characters are longer than the desired password length of 1."
**Solution**: Revised to: "You have chosen 8 numbers and 8 special characters, resulting in a total of 16 characters. This exceeds the specified password length of 1 character."
4. **Issue**: An infinite loop occurs when the user modifies password settings.
**Solution**:  Implemented a condition in the `get_password_info()` function that terminates the while loop once a password is generated.
5. **Issue**: Calling `Mixin.generate_random_numbers()` resulted in a TypeError: "Mixin.generate_random_numbers() takes 1 positional argument, but 2 were given."
**Solution**: Updated the method signature to include self as the first argument: `def generate_random_numbers(self, amount)`.
6. **Issue**: function `Mixin.generate_random_special_characters()` returns a boolean instead of a list of characters.
**Solution**: Replaced list comprehension with random.sample to correctly generate special characters.
7. **Issue**: Lack of differentiation between lowercase and uppercase letters in generated passwords.
 **Solution**: Added support for uppercase letters in password customization alongside special characters and numbers.
8. **Issue**:  Special characters were mistakenly receiving the input intended for the number of characters instead of the correct input.
**Solution**:  Reassigned the variable to correctly accept the input intended for special characters.
9. **Issue**: An error occurred when attempting to call the account_dict() class method:`account_dict()` class method:
    ```
    account_dict = account.account_dict()
                    ^^^^^^^^^^^^^^^^^^^^
    AttributeError: 'function' object has no attribute 'account_dict'
    ```
   The error resulted from mistakenly treating `account_dict` as a variable rather than invoking it as a function, which should be done as `account.account_dict()`.
**Solution**: Corrected the usage by invoking the function as `account.account_dict()`.
10. **Issue**: When deploying on Heroku, the following error occurred: "module not found."
**Solution**: To resolve this, the 'requirements.txt' file was updated to include the necessary dependencies.
11. **Issue**: There was a mention of 'secure_passwords.csv' in GitHub, which was caused by a typo in the filename when added to the .gitignore file.
**Solution**:  Corrected the filename typo within the .gitignore file to prevent any reference to 'secure_passwords.csv' on GitHub.
12. **Issue**: Password generation even if invalid settings are provided. e.g. the total length of the password is < numers amount + special characters amount + upper case amount
**Solution**: Moved the password generation outside the while loop in function `edit_password_default()` to ensure it is generated only when the validation criteria are met.

## Deployment
---
### Heroku
The deployment has been performed on heroku as follows:

1. **Create a Heroku Account:**
    If you don't have a Heroku account, sign up for one at Heroku's website.

2. **Log In to Heroku:**
Log in to your Heroku account using your credentials.

3. **Access Heroku Dashboard:**
After logging in, you'll be directed to your Heroku dashboard.

4. **Create a New App:**
To deploy your GitHub repository on Heroku, click the "New" button on the top right corner of the dashboard and select "Create new app."

5. **Name Your App:**
Choose a unique name for your app. If you have a specific name in mind, enter it in the "App name" field. Otherwise, Heroku will suggest a name for you.

6. **Choose a Region:**
Select the region closest to your intended audience or location. This determines the data center where your app will be hosted. Click the "Create app" button when you're ready.

7. **Connect to GitHub:**
In your app's dashboard, go to the "Deploy" tab. In the "Deployment method" section, choose "GitHub."

8. **Add Config Vars:**
On the "Deploy tab", navigate to the "Settings" tab.
Scroll down to the "Config Vars" section and click the "Reveal Config Vars" button, then add a new configuration variable by entering "port" as the key and "8000" as the value, then click "Add."

9. **Buildpacks**
On the "settings" tab scroll down to the "Buildpacks" section and click the "Add buildpack" button.
Select "Python" as the buildpack and save your changes.
Repeat this step and this time add "node.js" as the buildpack instead of Python.

10. **Buildpacks verification**
Ensure that the buildpacks are in the correct order. If "node.js" is listed first, you can drag "Python" upwards to make it the first buildpack in the list.

11. **Authorize Heroku to Access GitHub:**
On the "Deploy tab" Click the "Connect to GitHub" button. Heroku will ask for permission to access your GitHub repositories. Authorize Heroku to access your GitHub account.

12. **Search for Your GitHub Repository:**
After authorization, you can search for your GitHub repository by entering its name in the search box. Once you find it, click the "Connect" button next to your repository.

13. **Set Up Automatic or Manual Deployment:**
Heroku provides two deployment options:

 - **Automatic Deploys:** Whenever you push changes to your GitHub repository, Heroku will automatically deploy the latest version.
 - **Manual Deploy:** You can manually choose a branch to deploy. This is useful for controlling when updates go live.
14. **Choose Your Deployment Branch**:
If you selected manual deployment, choose the branch you want to deploy from the dropdown menu.

15. **Deploy Branch:**
Click the "Deploy Branch" button (for manual deployment) or "Enable Automatic Deploys" (for automatic deployment). Heroku will initiate the deployment process, which may take a few minutes.

16. **View Deployment Logs:**
You can monitor the deployment process by clicking the "View" button in the "Build log" section.

17. **Access Your Deployed App:**
Once the deployment is successful, you can access your deployed app by clicking the "Open app" button at the top of the page.

### Local
Clone this repository locally to enable the generation of the 'secure_password.csv' file containing the list of created accounts and generated passwords.
To have this repository on your local machine, follow these steps:"  

1. **Open a Terminal (or Command Prompt)**:
On your local machine, open a terminal or command prompt. You'll use this to enter commands.

1. **Navigate to Your Desired Directory:**
Use the `cd` (change directory) command to navigate to the directory where you want to create the virtual environment and clone the GitHub repository. For example:
    ```
    cd /path/to/your/directory
    ```
1. **Create a Virtual Environment:**
Use the following command to create a virtual environment. 
    ```
    python -m venv pwd_generator
    ```
    This command will create a virtual environment named `pwd_generator` in the current directory.

1. **Activate the Virtual Environment:**
To activate the virtual environment, use the appropriate command based on your operating system:
- On Windows:
    ```
    pwd_generator\Scripts\activate
    ```
- On macOS and Linux
    ```
    source pwd_generator/bin/activate
    ```
  You'll see the virtual environment name in your command prompt, indicating that it's active. 

5. **Install Git** (if not already installed):
If Git is not installed on your system, you can download and install it from the official Git website: https://git-scm.com/downloads  

1. **Clone the GitHub Repository:**
Use the git clone command to clone the GitHub repository. 
    ```
    git clone https://github.com/AngeloGaeta1990/Password_generator.git
    ```
   This command will download the repository files to your current directory.

1. **Navigate to the Cloned Repository Directory:**
Use the `cd` command to navigate into the cloned repository directory:  
    ```
    cd Password-generator
    ```
1. **Install Libraries from requirements.txt:**
Use the `pip install -r` command to install the libraries listed in the requirements.txt file.
    ```
    pip install -r requirements.txt
    ``` 
    This command will install all the required libraries and dependencies specified in the requirements.txt file within your virtual environment.
1. **Deactivate the Virtual Environment:**
When you're done working in the virtual environment, you can deactivate it using the following command:
    ```
    deactivate
    ```
    This returns you to the global Python environment.
## Credits
- [Lucidchart](https://www.lucidchart.com/pages/) for the generation of the Diagram
- [Code institute](https://codeinstitute.net/) for providing the template used in this project
- [Chatgpt](https://openai.com/blog/chatgpt) for assisting in troubleshooting and proofreading
- [PWNED](https://haveibeenpwned.com/) for providing the API method to verify if a password has been used in data breaches
- Great thanks to [David Bowers](https://github.com/dnlbowers) for assisting in shaping the project and providing the motivation to move forward. 
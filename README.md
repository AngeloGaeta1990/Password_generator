# Secure Password Generator
---
## Site Overview:
----
The "Secure Password Generator" is a robust tool designed to empower users with the capability to generate exceptionally strong and highly secure passwords, all while addressing the growing concerns around password security in an increasingly digital age.

While services like LastPass and Google Passwords offer secure password storage, they inherently rely on online platforms, which can potentially be vulnerable to cyberattacks. The Secure Password Generator, on the other hand, provides an offline solution for users who prioritize ultimate security and control over their password creation process.

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





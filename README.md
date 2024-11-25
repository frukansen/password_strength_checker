# Password Checker

A simple Python project to check the strength of passwords and compare them with a database of commonly used weak passwords.

Version 2 introduces a functionality to compare user-provided passwords against a list of known weak passwords (rockyou.txt by default).
## Features
- Validates password strength based on:
  - Length (minimum 8 characters)
  - Presence of uppercase and lowercase letters
  - Inclusion of at least one digit
  - Inclusion of at least one special character

#### V2 Added Features:
- Loads weak passwords from a specified file (default: `rockyou.txt`).
- Checks if a given password is weak by comparing it to the loaded list.
- Simple and lightweight tool to improve password security.

#### About `rockyou.txt`:
The [`rockyou.txt`](https://github.com/frukansen/password_strength_checker/releases/tag/data) file is a popular password dataset derived from the [2009 RockYou data breach](https://techcrunch.com/2009/12/14/rockyou-hack-security-myspace-facebook-passwords/), where millions of plaintext passwords were leaked. This tool uses the dataset for educational purposes, such as demonstrating weak password detection.  
⚠️ **Ensure you have legal permission to use this dataset in your region.**

#### Setup Instructions:
1. Download and place the `rockyou.txt` file in the project directory (same folder as the script).
   - The file should contain one weak password per line.
   - The dataset can be found in publicly available security research repositories.
2. Run the script using Python 3.

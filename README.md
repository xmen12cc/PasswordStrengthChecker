# Project: Password Strength Checker (Python Script)

## Description
This Python script evaluates the strength of a given password based on several criteria, including:
- Length
- Use of uppercase letters
- Use of lowercase letters
- Inclusion of numbers
- Inclusion of special characters (e.g., !@#$%^&*)

The script checks these criteria and provides feedback on whether a password is strong, moderate, or weak. This promotes better password security practices by encouraging users to create stronger, more complex passwords.

## Purpose
The purpose of this script is to help users assess the strength of their passwords and improve their overall security practices. With an increasing number of online services requiring secure login credentials, using weak passwords can leave accounts vulnerable to unauthorized access. This script ensures that users are aware of the strength of their passwords and offers suggestions for improvement.

By checking passwords for key strength criteria, the script provides a simple way for users to ensure they are not using passwords that can easily be guessed or cracked.

## Features
- **Length Check**: Ensures that the password meets a minimum length requirement.
- **Uppercase Check**: Verifies the presence of at least one uppercase letter.
- **Lowercase Check**: Ensures at least one lowercase letter is used.
- **Numeric Check**: Ensures the password contains numbers.
- **Special Character Check**: Looks for at least one special character to increase complexity.

The script then categorizes the password into one of three strength categories:
- **Strong**: Meets all criteria.
- **Moderate**: Meets at least three criteria but could still be stronger.
- **Weak**: Fails to meet at least three of the required criteria.

## Steps to Use
1. **Download or Clone the Repository**
   - You can download or clone the repository using Git.
   
2. **Run the Script**
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the script using the following command:
     ```bash
     python password_checker.py
     ```

3. **Enter a Password**
   - The script will prompt you to enter a password. Type or paste your password into the terminal.
   
4. **Receive Feedback**
   - After entering the password, the script will check the password against the defined criteria.
   - It will print out the strength of the password, such as "Strong," "Moderate," or "Weak."
   - Suggestions for improvement may be provided if the password is found to be weak or moderate.

---

## Example Usage

### Examples: Strong Password, Moderate Password and Weak Password

```bash
$ python password_checker.py
Enter a password to check its strength: P@ssw0rd123
Password strength: Strong

$ python password_checker.py
Enter a password to check its strength: Passw0rd
Password strength: Moderate

$ python password_checker.py
Enter a password to check its strength: password
Password strength: Weak



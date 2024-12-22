import re

def check_password_strength(password):
    strength = 0
    # Check if password length is at least 8 characters
    if len(password) >= 8:
        strength += 1
    # Check for at least one uppercase letter
    if re.search(r"[A-Z]", password):
        strength += 1
    # Check for at least one lowercase letter
    if re.search(r"[a-z]", password):
        strength += 1
    # Check for at least one number
    if re.search(r"[0-9]", password):
        strength += 1
    # Check for at least one special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    # Return password strength based on the criteria
    if strength == 5:
        return "Strong"
    elif 3 <= strength < 5:
        return "Moderate"
    else:
        return "Weak"

if __name__ == "__main__":
    # Prompt the user to enter a password
    password = input("Enter a password to check its strength: ")
    # Check the password strength and display the result
    result = check_password_strength(password)
    print(f"Password strength: {result}")

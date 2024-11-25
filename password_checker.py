import re

# Global variable to store weak passwords
weak_passwords = set()

def load_weak_passwords(file_path):
    """
    Loads the weak password list from a file.
    """
    global weak_passwords
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            weak_passwords = set(line.strip() for line in file)
    except FileNotFoundError:
        print(f"Warning: {file_path} not found. Weak password check is disabled.")
    except Exception as e:
        print(f"Error: {e}")

def check_password_strength(password):
    """
    Checks the strength of a password.
    """
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."

    if not re.search(r"[A-Z]", password):
        return "Weak: Password must contain at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return "Weak: Password must contain at least one lowercase letter."

    if not re.search(r"[0-9]", password):
        return "Weak: Password must contain at least one digit."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Password must contain at least one special character."

    if password in weak_passwords:
        return "Weak: Password is too common and insecure!"

    return "Strong: Password looks good."

if __name__ == "__main__":
    # Load the weak password list
    load_weak_passwords("rockyou.txt")

    while True:
        user_password = input("Enter your password (type 'q' to quit): ")
        if user_password.lower() == 'q':
            break
        result = check_password_strength(user_password)
        print(result)

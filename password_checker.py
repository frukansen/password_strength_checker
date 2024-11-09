import re

def password_strength(password):
    strength = 0
    strength_criteria = [
        (r".{8,}", "Password must be at least 8 characters long."),
        (r"[A-Z]", "Password should include uppercase letters."),
        (r"[a-z]", "Password should include lowercase letters."),
        (r"[0-9]", "Password should include digits."),
        (r"[!@#$%^&*()_+]", "Password should include special characters.")
    ]
    
    # Check each criterion
    for regex, message in strength_criteria:
        if re.search(regex, password):
            strength += 1
        else:
            print(message)
    
    # Calculate strength level
    if strength == len(strength_criteria):
        return "Strong"
    elif strength == len(strength_criteria) - 1:
        return "Moderate"
    else:
        return "Weak"

# Main program
password = input("Enter your password: ")
strength = password_strength(password)
print(f"Password Strength: {strength}")

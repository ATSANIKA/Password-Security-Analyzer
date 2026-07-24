"""
Project Name : Password Security Analyzer

Developer : Sanika Patil

Description :
This module performs password security analysis,
calculates password score, entropy,
estimated crack time and suggestions.
"""

import math
import random
import string

# Function to check password length
def check_length(password):
    """
    Checks whether the password length is secure.

    Parameter:
        password (str): Password entered by the user.

    Returns:
        tuple:
            (True, message)  -> if password length is acceptable
            (False, message) -> if password is too short
    """

    # Minimum recommended password length
    minimum_length = 8

    # Check password length
    if len(password) >= minimum_length:
        return True, f"Password length is {len(password)} characters."

    return False, f"Password is too short. It should contain at least {minimum_length} characters."

# Function to check uppercase letters
def check_uppercase(password):
    """
    Checks whether the password contains at least one uppercase letter.
    """

    for character in password:
        if character.isupper():
            return True, "Contains uppercase letter."

    return False, "No uppercase letter found."

# Function to check lowercase letters
def check_lowercase(password):
    """
    Checks whether the password contains at least one lowercase letter.
    """

    for character in password:
        if character.islower():
            return True, "Contains lowercase letter."

    return False, "No lowercase letter found."

# Function to check numbers
def check_numbers(password):
    """
    Checks whether the password contains at least one number.
    """

    for character in password:
        if character.isdigit():
            return True, "Contains number."

    return False, "No number found."

# Function to check special characters
def check_special_character(password):
    """
    Checks whether the password contains at least one special character.
    """

    special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    for character in password:
        if character in special_characters:
            return True, "Contains special character."

    return False, "No special character found."

# Function to calculate password score
def calculate_score(length_ok, uppercase_ok, lowercase_ok, number_ok, special_ok):
    """
    Calculates the password security score.
    """

    score = 0

    if length_ok:
        score += 20

    if uppercase_ok:
        score += 20

    if lowercase_ok:
        score += 20

    if number_ok:
        score += 20

    if special_ok:
        score += 20

    return score

# Function to check common passwords
def check_common_password(password):
    """
    Checks whether the password exists in the common password list.
    """

    try:
        with open("common_passwords.txt", "r") as file:

            common_passwords = file.read().splitlines()

            if password.lower() in common_passwords:
                return False, "This is a common password."

            return True, "Password is not in the common password list."

    except FileNotFoundError:
        return True, "Common password file not found."

def calculate_entropy(password):
    """
    Calculates the approximate entropy of the password.
    """

    character_pool = 0

    if any(c.islower() for c in password):
        character_pool += 26

    if any(c.isupper() for c in password):
        character_pool += 26

    if any(c.isdigit() for c in password):
        character_pool += 10

    if any(not c.isalnum() for c in password):
        character_pool += 32

    if character_pool == 0:
        return 0

    entropy = len(password) * math.log2(character_pool)

    return round(entropy, 2)

def estimate_crack_time(entropy):
    """
    Estimates how long it might take to crack the password
    based on its entropy.
    """

    if entropy < 28:
        return "Instantly"

    elif entropy < 36:
        return "A few minutes"

    elif entropy < 60:
        return "A few days"

    elif entropy < 80:
        return "Several years"

    else:
        return "Hundreds of years"

def generate_suggestions(
    length_status,
    uppercase_status,
    lowercase_status,
    number_status,
    special_status,
    common_status
):
    """
    Generates security recommendations for improving the password.
    """

    suggestions = []

    if not length_status:
        suggestions.append("Increase password length to at least 8 characters.")

    if not uppercase_status:
        suggestions.append("Add at least one uppercase letter.")

    if not lowercase_status:
        suggestions.append("Add at least one lowercase letter.")

    if not number_status:
        suggestions.append("Add at least one number.")

    if not special_status:
        suggestions.append("Add at least one special character.")

    if not common_status:
        suggestions.append("Avoid using common passwords.")

    if len(suggestions) == 0:
        suggestions.append("Excellent! Your password follows the recommended security practices.")

    return suggestions

def generate_strong_password(length=12):
    """
    Generates a strong random password.
    """

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()_+-=[]{}"

    all_characters = lowercase + uppercase + digits + symbols

    # Ensure at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the remaining characters
    while len(password) < length:
        password.append(random.choice(all_characters))

    # Shuffle for randomness
    random.shuffle(password)

    return "".join(password)

# Main function to analyze the password
def analyze_password(password):

    # Perform all checks
    length_status, length_message = check_length(password)
    uppercase_status, uppercase_message = check_uppercase(password)
    lowercase_status, lowercase_message = check_lowercase(password)
    number_status, number_message = check_numbers(password)
    special_status, special_message = check_special_character(password)
    common_status, common_message = check_common_password(password)

    # Calculate score
    score = calculate_score(
        length_status,
        uppercase_status,
        lowercase_status,
        number_status,
        special_status
    )
    entropy = calculate_entropy(password)
    crack_time = estimate_crack_time(entropy)

    suggestions = generate_suggestions(
    length_status,
    uppercase_status,
    lowercase_status,
    number_status,
    special_status,
    common_status
    )

    # Decide strength
    if score >= 80:
        strength = "STRONG"
    elif score >= 60:
        strength = "MEDIUM"
    else:
        strength = "WEAK"

    # If the password is common, reduce security
    if not common_status:
        strength = "WEAK"

    return {
        "length": (length_status, length_message),
        "uppercase": (uppercase_status, uppercase_message),
        "lowercase": (lowercase_status, lowercase_message),
        "number": (number_status, number_message),
        "special": (special_status, special_message),
        "common": (common_status, common_message),
        "score": score,
        "entropy": entropy,
        "crack_time": crack_time,
        "suggestions": suggestions,
        "strength": strength
        
    }

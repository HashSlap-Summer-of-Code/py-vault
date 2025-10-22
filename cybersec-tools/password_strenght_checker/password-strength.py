#!/usr/bin/env python3

"""
A simple tool to check how strong your password is. It looks at things like:
- Password length
- Mix of different characters (uppercase, lowercase, numbers, symbols)
- Common password patterns to avoid
"""

import re
import sys
import argparse

# Common passwords that should be avoided
COMMON_PASSWORDS = {
    "123456", "password", "123456789", "12345", "12345678", "qwerty",
    "111111", "1234567", "abcdefg", "Password", "pass", "admin"
}

def evaluate_strength(password: str) -> tuple[int, list[str]]:
    """
    Checks how strong a password is and gives helpful tips.
    Returns a score and list of feedback messages.
    """
    score = 0
    feedback = []
    
    # Check password length
    length = len(password)
    if length < 8:
        feedback.append("Weak: Password should be at least 8 characters long.")
    elif length >= 12:
        score += 20
        feedback.append("Good: Password is 12 characters or longer.")
    else:
        score += 10
        feedback.append("OK: Password is at least 8 characters long.")

    # Check for different types of characters
    char_types = 0
    if re.search(r'[a-z]', password):
        score += 5
        char_types += 1
    else:
        feedback.append("Weak: Add lowercase letters.")

    if re.search(r'[A-Z]', password):
        score += 5
        char_types += 1
    else:
        feedback.append("Weak: Add uppercase letters.")

    if re.search(r'\d', password):
        score += 5
        char_types += 1
    else:
        feedback.append("Weak: Add numbers.")

    if re.search(r'[^a-zA-Z0-9]', password):
        score += 10
        char_types += 1
    else:
        feedback.append("Weak: Add special characters (e.g., !@#$%).")

    # Extra points for using multiple character types
    if char_types == 3:
        score += 10
        feedback.append("Good: Password uses three character types.")
    elif char_types == 4:
        score += 20
        feedback.append("Strong: Password uses all four character types.")

    # Check if it's a common password
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback = ["Very Weak: This is a very common password."]

    return score, feedback

def get_strength_level(score: int) -> str:
    """Converts the score into an easy-to-understand strength level."""
    if score >= 60:
        return "Very Strong"
    if score >= 45:
        return "Strong"
    if score >= 30:
        return "Medium"
    if score >= 15:
        return "Weak"
    return "Very Weak"

def main():
    """
    Runs the password checker from the command line.
    """
    parser = argparse.ArgumentParser(
        description="Check how strong your password is.",
        epilog="Example: python3 password-strength.py \"MyP@ssw0rd!\""
    )
    parser.add_argument(
        "password",
        type=str,
        help="Your password (use quotes if it contains special characters)"
    )
    args = parser.parse_args()

    password = args.password
    score, feedback = evaluate_strength(password)
    level = get_strength_level(score)

    print("--- Password Strength Report ---")
    print(f"Password: {'*' * len(password)}")
    print(f"Strength: {level} (Score: {score})")
    print("\nFeedback:")
    for item in feedback:
        print(f"- {item}")
    print("--------------------------------")

    if level in ("Very Weak", "Weak"):
        sys.exit(1)

if __name__ == "__main__":
    main()

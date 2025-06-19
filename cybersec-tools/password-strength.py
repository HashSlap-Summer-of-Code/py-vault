import re

def check_strength(password):
    length = len(password)
    score = 0
    suggestions = []

    if length >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r'\d', password):
        score += 1
    else:
        suggestions.append("Add digits.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        suggestions.append("Add special symbols.")

    common_passwords = ['password', '123456', 'qwerty', 'letmein']
    if password.lower() in common_passwords:
        suggestions.append("Avoid common passwords.")

    print("\nPassword Score:", score, "/ 5")
    if score == 5:
        print("✅ Strong password!")
    else:
        print("❌ Weak password. Suggestions:")
        for tip in suggestions:
            print("-", tip)

if __name__ == "__main__":
    pwd = input("Enter your password to check strength: ")
    check_strength(pwd)

# Password Strength Checker (`password-strength.py`)

A Python script to evaluate password strength based on length, character types (upper, lower, digit, special), and common password checks.

## Criteria

This tool scores a password based on:

* **Length:** Rewards passwords 12+ characters long.
* **Character Mix:** Awards points for using lowercase, uppercase, digits, and special characters.
* **Common Patterns:** Fails common passwords (e.g., "123456", "password").

## Usage

### Requirements

* Python 3.x (No external libraries needed)

### Running the script

Navigate to the `cybersec-tools` directory and run the script, passing the password as an argument.

**Important:** Wrap passwords in quotes (`"`) if they contain special characters.

```

# Example command

python3 password-strength.py "MyP@ssw0rd!_123"

```

### Example Outputs

**Strong:**

```
--- Password Strength Report ---
Password: *****************
Strength: Very Strong (Score: 65)
Feedback:

  - Good: Password is 12 characters or longer.
  - Strong: Password uses all four character types.

```

**Medium:**

```
--- Password Strength Report ---
Password: ***********
Strength: Medium (Score: 30)
Feedback:

  - OK: Password is at least 8 characters long.
  - Weak: Add special characters (e.g., \!@\#$%).
  - Good: Password uses three character types.

```

**Weak:**

```

--- Password Strength Report ---
Password: ********
Strength: Very Weak (Score: 0)
Feedback:

  - Very Weak: This is a very common password.

```
import re
import secrets
import string


# Some common passwords that should never be used
COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "qwerty123",
    "admin",
    "admin123",
    "letmein",
    "welcome",
    "abc123",
    "iloveyou"
}


def check_password(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Use at least 12 characters for better security.")
    else:
        feedback.append("Password should contain at least 8 characters.")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Check numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Check special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add a special character such as @, #, $, or !.")

    # Check if password is common
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("This is a commonly used password. Choose something unique.")

    # Check repeated characters
    if re.search(r"(.)\1\1", password):
        score -= 1
        feedback.append("Avoid repeating the same character multiple times.")

    # Check character variety
    unique_characters = len(set(password))

    if len(password) >= 8:
        if unique_characters < 5:
            score -= 1
            feedback.append("Use a wider variety of characters.")

    # Keep score within range
    score = max(0, min(score, 7))

    # Decide strength
    if score <= 2:
        strength = "Very Weak"
    elif score <= 4:
        strength = "Weak"
    elif score <= 5:
        strength = "Moderate"
    elif score == 6:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return score, strength, feedback


def generate_password(length=16):
    """Generate a random strong password."""

    if length < 8:
        length = 8

    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    # Make sure the generated password has different character types
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    # Fill the remaining positions
    for _ in range(length - 4):
        password.append(secrets.choice(characters))

    # Shuffle the password securely
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def main():
    print("=" * 45)
    print("       PASSWORD STRENGTH ANALYZER")
    print("=" * 45)

    while True:
        password = input("\nEnter your password: ")

        if not password:
            print("Password cannot be empty.")
            continue

        score, strength, feedback = check_password(password)

        print("\nPassword Analysis")
        print("-" * 25)
        print(f"Strength : {strength}")
        print(f"Score    : {score}/7")

        if feedback:
            print("\nSuggestions:")
            for suggestion in feedback:
                print(f"- {suggestion}")
        else:
            print("\nNo major issues found!")

        choice = input(
            "\nWould you like to generate a stronger password? (y/n): "
        ).lower()

        if choice == "y":
            new_password = generate_password()
            print(f"\nSuggested password: {new_password}")

        again = input("\nCheck another password? (y/n): ").lower()

        if again != "y":
            print("\nThanks for using Password Strength Analyzer!")
            break


if __name__ == "__main__":
    main()

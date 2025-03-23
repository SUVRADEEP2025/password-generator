import secrets
import string

def generate_password(length, use_lowercase, use_uppercase, use_symbols):
    # Define character sets based on user preferences
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_symbols:
        characters += string.punctuation
    characters += string.digits  # Always include digits

    if not characters:
        raise ValueError("At least one character set must be selected.")

    # Generate password using cryptographically secure random choices
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Get password length from user
while True:
    try:
        length = int(input("Enter the desired password length: "))
        if length < 1:
            print("Password length must be at least 1.")
            continue
        break
    except ValueError:
        print("Please enter a valid integer.")

# Get user preferences for character sets
use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

# Generate and display the password
try:
    password = generate_password(length, use_lowercase, use_uppercase, use_symbols)
    print("\nGenerated Password:", password)
except ValueError as e:
    print("\nError:", e)
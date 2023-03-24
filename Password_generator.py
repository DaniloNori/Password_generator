import random
import string

def generate_password(length=20, uppercase=True, lowercase=True, numbers=True, symbols=True):
    """Generate a random password with the specified length and character types."""
    if not any([uppercase, lowercase, numbers, symbols]):
        raise ValueError("At least one character type must be enabled.")

    # Define character sets
    charsets = []
    if uppercase:
        charsets.append(string.ascii_uppercase)
    if lowercase:
        charsets.append(string.ascii_lowercase)
    if numbers:
        charsets.append(string.digits)
    if symbols:
        charsets.append('%$^!()[]*^&@#;,.')  # removed duplicate semi-colon

    # Ensure password meets minimum length requirements
    min_length = sum([1 for charset in charsets if len(charset) > 0])
    if length < min_length:
        raise ValueError(f"Password must be at least {min_length} characters long.")

    # Generate password
    password = []
    for i in range(length):
        charset = random.choice(charsets)
        password.append(random.choice(charset))
    random.shuffle(password)
    return ''.join(password)

# Example usage
password = generate_password(length=20, uppercase=True, lowercase=True, numbers=True, symbols=True)
print(password)

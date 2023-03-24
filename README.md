Random Password Generator.

This is a Python module that generates a random password with specified characteristics.

Usage.

from generate_password import generate_password

# Generate a password with a length of 20 characters, including uppercase letters, lowercase letters, numbers, and symbols
password = generate_password(length=20, uppercase=True, lowercase=True, numbers=True, symbols=True)
print(password)

Arguments.
The generate_password() function takes the following arguments:

length: The length of the password to generate. Default is 20.
uppercase: Whether or not to include uppercase letters in the password. Default is True.
lowercase: Whether or not to include lowercase letters in the password. Default is True.
numbers: Whether or not to include numbers in the password. Default is True.
symbols: Whether or not to include symbols in the password. Default is True.
Exceptions
The generate_password() function can raise the following exceptions:

ValueError: If none of the character types (uppercase, lowercase, numbers, symbols) are enabled, or if the requested password length is less than the minimum required length.

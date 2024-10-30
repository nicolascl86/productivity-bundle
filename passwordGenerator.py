import random
import string

def generate_password(length=12):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure at least one of each character type is included
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Fill the rest of the password length with random choices from all character sets
    all_characters = lowercase + uppercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Join the list into a string and return it
    return ''.join(password)

# Generate a password
new_password = generate_password()
print(new_password)

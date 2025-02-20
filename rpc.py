import random
import string

def generate_password(length=12):
    # Define the character sets
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    # Combine all character sets
    all_chars = upper + lower + digits + special

    # Ensure the password has at least one character from each set
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_chars, k=length-4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)

if __name__ == "__main__":
    # Generate a random password of length 12
    password = generate_password(12)
    print(f"Your random password is: {password}")

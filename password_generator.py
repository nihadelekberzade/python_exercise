import random
import string

def generate_password(length=12):
    # Define characters to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure at least one character from each character set
    password = random.choice(string.ascii_lowercase) + \
               random.choice(string.ascii_uppercase) + \
               random.choice(string.digits) + \
               random.choice(string.punctuation)

    # Generate the remaining characters for the password
    for _ in range(length - 4):
        password += random.choice(characters)

    # Shuffle the characters to make the password random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

# Generate a 16-character password (you can specify a different length)
password = generate_password(16)
print(password)

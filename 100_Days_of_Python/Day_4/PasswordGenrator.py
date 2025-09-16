import random
import string

# Define password length
length = int(input("Enter desired password length: "))

# Define character pool
characters = string.ascii_letters + string.digits + string.punctuation

# Initialize empty password
password = ""

# Loop to generate password
for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)

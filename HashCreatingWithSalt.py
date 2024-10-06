
import crypt
import os

# Function to generate a random salt
def generate_salt(length=16):
    return os.urandom(length).hex()[:length]

# Ask user for plain-text password
clear_pass = input("What's your password: ")

# Generate a random salt or use user input
use_random_salt = input("Do you want to use a random salt? (y/n): ").strip().lower() == 'y'
salt = generate_salt() if use_random_salt else input("What is the salt (keep it to 16 characters): ")[:16]

# Print out hashes
print("MD5      : {0}".format(crypt.crypt(clear_pass, "$1$" + salt)))
print("Blowfish  : {0}".format(crypt.crypt(clear_pass, "$2$" + salt)))
print("Eksblowfish: {0}".format(crypt.crypt(clear_pass, "$2a$" + salt)))
print("SHA-256  : {0}".format(crypt.crypt(clear_pass, "$5$" + salt)))
print("SHA-512  : {0}".format(crypt.crypt(clear_pass, "$6$" + salt)))

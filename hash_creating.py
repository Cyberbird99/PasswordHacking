
import crypt

# Ask user for plain-text password
clear_pass = input("What's your password: ")

# Print out hashes with appropriate format
print(f"MD5:       {crypt.crypt(clear_pass, '$1$example$salt')}")
print(f"Blowfish:  {crypt.crypt(clear_pass, '$2a$12$salt_string_here')}")
print(f"ExBlowfish:{crypt.crypt(clear_pass, '$2y$12$salt_string_here')}")
print(f"SHA-256:   {crypt.crypt(clear_pass, '$5$some_salt')}")
print(f"SHA-512:   {crypt.crypt(clear_pass, '$6$another_salt')}")

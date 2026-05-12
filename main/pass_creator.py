from argon2 import PasswordHasher
ph = PasswordHasher()

hash = ph.hash(input("Enter password to hash: "))

with open("pass.txt", "w") as file:
    file.write(hash)
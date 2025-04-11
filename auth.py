import hashlib
import os

USERS_FILE = "users.txt"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    username = input("Enter a new username: ")
    password = input("Enter a password: ")
    hashed = hash_password(password)
    with open(USERS_FILE, "a") as f:
        f.write(f"{username},{hashed}\n")
    print("User registered successfully!")

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed = hash_password(password)
    with open(USERS_FILE, "r") as f:
        for line in f:
            u, p = line.strip().split(",")
            if u == username and p == hashed:
                print("Login successful!")
                return username
    print("Invalid username or password.")
    return None
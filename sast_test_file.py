
import sqlite3
import os
import pickle

# Hardcoded credentials (Issue: Sensitive Information Exposure)
USERNAME = "admin"
PASSWORD = "password123"

# SQL Injection vulnerability
user_input = input("Enter username: ")
connection = sqlite3.connect("example.db")
cursor = connection.cursor()
query = f"SELECT * FROM users WHERE username = '{user_input}'"
cursor.execute(query)
print(cursor.fetchall())

# Command Injection vulnerability
filename = input("Enter filename to list: ")
os.system(f"ls {filename}")

# Insecure deserialization
malicious_data = b"cos
system
(S'echo hacked'
tR."
pickle.loads(malicious_data)

# Weak cryptography
import hashlib
password = "mypassword"
hash_value = hashlib.md5(password.encode()).hexdigest()
print("MD5 hash:", hash_value)

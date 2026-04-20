# path_traversal_vuln.py
import os

BASE_DIR = "/var/www/files/"

def read_file(filename):
    # Vulnerable to path traversal
    filepath = os.path.join(BASE_DIR, filename)
    
    with open(filepath, "r") as f:
        return f.read()

if __name__ == "__main__":
    file = input("Enter filename: ")
    print(read_file(file))

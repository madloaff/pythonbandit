import os
import hashlib
import subprocess

# Hardcoded credentials (BAD PRACTICE)
USERNAME = "admin"
PASSWORD = "1234567"  # Vulnerability: Hardcoded password

def insecure_hash(data):
    """Uses an insecure hashing algorithm (MD5)"""
    return hashlib.md5(data.encode()).hexdigest()  # Vulnerability: Weak hash function

def run_command(user_input):
    """Executes a shell command unsafely"""
    command = f"echo {user_input}"  # Vulnerability: Potential command injection
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).communicate()[0]

# Testing the vulnerabilities
if __name__ == "__main__":
    print(f"User: {USERNAME}, Password: {PASSWORD}")
    
    hashed_password = insecure_hash(PASSWORD)
    print(f"Insecure Hash: {hashed_password}")

    user_input = input("Enter a command: ")
    print(run_command(user_input))

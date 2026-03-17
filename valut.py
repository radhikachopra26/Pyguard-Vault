import random
import string
import re

def check_strength(password):
    """Checks if a password is weak, medium, or strong."""
    strength = 0
    if len(password) >= 8: strength += 1
    if re.search("[a-z]", password) and re.search("[A-Z]", password): strength += 1
    if re.search("[0-9]", password): strength += 1
    if re.search("[!@#$%^&*]", password): strength += 1

    if strength == 4: return "💪 Strong"
    if strength >= 2: return "⚖️ Medium"
    return "⚠️ Weak"

def generate_password(length=12):
    """Generates a secure random password."""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    print("🛡️ Welcome to PyGuard Vault 🛡️")
    print("-" * 30)
    
    while True:
        print("\n1. 🔑 Generate New Password")
        print("2. 🔍 Check Password Strength")
        print("3. ❌ Exit")
        
        choice = input("\nSelect an option: ")
        
        if choice == '1':
            size = int(input("Enter password length (default 12): ") or 12)
            pwd = generate_password(size)
            print(f"✨ Generated Password: {pwd}")
        elif choice == '2':
            pwd = input("Enter password to check: ")
            print(f"Result: {check_strength(pwd)}")
        elif choice == '3':
            print("👋 Stay safe!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()

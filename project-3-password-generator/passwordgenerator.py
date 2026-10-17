import secrets
import string

def generate_password():
    print("--- 🔐 Enterprise Random Password Generator ---")
    
   
    try:
        length = int(input("Enter the desired password length (minimum 8 characters): "))
        if length < 8:
            print("Warning: For better security, a minimum length of 8 characters is recommended.")
    except ValueError:
        print("Error: Please enter a valid integer for the password length.")
        return

    
    character_pool = string.ascii_letters + string.digits + string.punctuation

    
    password_chars = [secrets.choice(character_pool) for _ in range(length)]
    secure_password = "".join(password_chars)

    
    print(f"\nGenerated Secure Password: {secure_password}")
    print("Status: Cryptographically secure entropy provision completed successfully!\n")

if __name__ == "__main__":
    generate_password()
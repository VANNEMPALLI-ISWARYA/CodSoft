import random
import string

def get_password_length():
    """Prompt the user for the desired password length with validation."""
    while True:
        try:
            length = int(input("Enter the desired length of the password (at least 4): "))
            if length < 4:
                print("Password length should be at least 4 to include all character types.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_character_types():
    """Prompt the user to select which character types to include in the password."""
    include_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    include_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    include_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
    
    # Create a character set based on user choices
    character_set = ''
    if include_lowercase:
        character_set += string.ascii_lowercase
    if include_uppercase:
        character_set += string.ascii_uppercase
    if include_digits:
        character_set += string.digits
    if include_special:
        character_set += string.punctuation

    if not character_set:
        print("You must select at least one character type.")
        return get_character_types()

    return character_set

def generate_password(length, character_set):
    """Generate a random password using the specified character set and length."""
    password = random.choices(character_set, k=length)
    return ''.join(password)

def main():
    """Main function to run the password generator."""
    print("Welcome to the Smart Password Generator!")
    
    length = get_password_length()
    character_set = get_character_types()
    
    password = generate_password(length, character_set)
    
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()

import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    """Generate a random password based on user-defined criteria."""
    character_set = ''
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("At least one character type must be selected.")

    return ''.join(random.choice(character_set) for _ in range(length))

def main():
    print("Welcome to the Password Generator!")

    try:
        # Prompt user for password length
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be a positive integer.")
            return

        # Prompt user for character type preferences
        use_letters = input("Include letters? (yes/no): ").strip().lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

        # Generate and display the password
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated password: {password}")

    except ValueError:
        print("Invalid input. Please enter valid values for length and character types.")

if __name__ == "__main__":
    main()

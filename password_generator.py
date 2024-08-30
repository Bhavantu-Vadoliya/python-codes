import random
import string

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        return "No characters available for the password."

    return ''.join(random.choice(characters) for _ in range(length))

def get_integer(prompt, min_value):
    while True:
        try:
            value = int(input(prompt))
            if value >= min_value:
                return value
            else:
                print(f"Please enter a value greater than or equal to {min_value}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    print("Password Generator")

    length = get_integer("Enter the length of the password: ", 1)
    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()

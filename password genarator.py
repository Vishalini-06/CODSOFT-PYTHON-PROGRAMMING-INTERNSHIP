import random
import string

while True:
    try:
        length = int(input("Enter the desired password length: "))
        if length > 0:
            # Define possible characters
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choices(characters, k=length))
    
            print(f"Your generated password is: {password}\n")
        else:
            print("Password length must be greater than 0.\n")
    except ValueError:
        print("Invalid input! Please enter a valid number.\n")
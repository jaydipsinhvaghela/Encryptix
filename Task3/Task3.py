import random
import string

while True:
    try:
        length = int(input("Enter password: "))
        if length < 1:
            print("Length must be at least 1. Please try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

characters = string.ascii_letters + string.digits 

password = ''
for i in range(length):
    password += random.choice(characters)

print(f"Generated Password: {password}")



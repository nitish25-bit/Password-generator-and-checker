import random
import string

input("Welcome to the Random Password Generator and password strength checker! Press Enter to continue...")
if input("Do you want to generate a password? or check your password strength (generate/check): ").lower() == "generate":
    password_length = int(input("Enter the desired password length: "))
    if password_length < 8:
        print("Password length should be at least 8 characters.")

    else: 
        password = ""
        while len(password) < password_length:
             password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        print(password)
        print("password generated successfully!")




elif input("Do you want to check your password strength? (yes/no): ").lower() == "yes":
    password = ""
    password = input("Enter the password you want to check: ")
    passwordstrength = 0
    if len(password) >= 15:
        passwordstrength += 4
    elif len(password) >= 12:
        passwordstrength += 3
    elif len(password) >= 10:
        passwordstrength += 2
    elif len(password) >= 8:
        passwordstrength += 1

    if any(char.islower() for char in password):
        passwordstrength += 1
    if any(char.isupper() for char in password):
        passwordstrength += 1
    if any(char.isdigit() for char in password):
        passwordstrength += 2
    if any(char in string.punctuation for char in password):
        passwordstrength += 2


    if passwordstrength >= 8:
        print("Password strength: Strong")
    elif passwordstrength >= 5:
        print("Password strength: Medium")
    else:
        print("Password strength: Weak")
    print("Password strength score: ",passwordstrength)

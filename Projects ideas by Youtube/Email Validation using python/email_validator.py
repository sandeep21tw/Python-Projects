# This program check is email entered is valid or not
# by Sandeep

# Version 1:


def validator():

    valid = False
    email = input("Type your email: ")

    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    dot_ = "."
    at_rate = "@"

    chars = letters + numbers + dot_ + at_rate

    for char in email:
        if char not in chars:
            print("Invalid Characters")
            break

    if (len(email) > 6):
        if email.count('@') == 1:
            if not ((email[0] in numbers) or (email[0] == ".")):
                left, right = email.split('@')
                if right.count('.') == 1:
                    valid = True
                    return email, valid

    return email, valid



while True:
    email, check = validator()
    if check:
        print("It's a valid email.")
        print(f"Welcome {email}!\n")
    else:
        print("Unvalid email id.")

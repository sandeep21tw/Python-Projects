# This program generates a unique password for the user.
# by Sandeep
# Completed from my side
# BY THE WAY! I HAVE TO SAY! WELL DONE :] THIS IS FULL FLEDGED THAT YOU COMPLETED AND COULD HAVE GAINED MANY INSIGHTS FROM THEM
# next make a password manager if you want






import random


# Note: here we are avoiding the character "<" and ">" cause it causes some problems in web browsers as passwords
characters = []

for i in range(32, 65):
    if (chr(i) != "<" and chr(i) != ">"):
        characters.append(chr(i))

uppercase = []
for i in range(65, 91):
    uppercase.append(chr(i))

lowercase = []
for i in range(97, 123):
    lowercase.append(chr(i))


"""
Rule: We are following

1) atleast 12 characters long
2) mixture of lowercase and uppercase
3) mixture of characters and numbers
4) no "<" and ">"
"""


def generate(pl):
    # pl is a dictionary containing the length for lowercase, uppercase and characters
    #lc = random.sample(lowercase, pl["l"])
    #uc = random.sample(uppercase, pl["u"])
    #char = random.sample(characters, pl["c"])

    # Couldn't use above lines as they are giving the error in case of 100 digits passwords because of random.sample method.
    # Error: ValueError: Sample larger than population or is negative
    # We will use List Comprehension

    lc = [random.choice(lowercase) for i in range(pl["l"])]
    uc = [random.choice(uppercase) for i in range(pl["u"])]
    char = [random.choice(characters) for i in range(pl["c"])]


    
    # quick ques: will someone be able to crack the password if knowing that 4 are uppercase, 4 are lowercase and 4 characters in password

    password = lc + uc + char
    random.shuffle(password)
    password = "".join(password)
    
    return password

def check_length(length):
    """
    length arguement is the length that user wants but we modify it and subtract the default limit and use it for our easy logic
    """
    
    if length > 12:
        length = length - 12        # default limit is 12
    else:
        print("")
        print("Default minimum secure password limit is 12.")
        print("Generating the password using that limit:")
        length = 0       # why not subtract 12 like above? will result in negative no and error. that's why!

    return length

        

def char_types_n_length(length):
    """
    This program decides how many uppercase, lowercase and characters should be present on password based on length.

    pass_len stands for password length containing length for lowercase, uppercase and characters.
    l = lowercase, u = uppercaes, c = characters

    
    """

    length = check_length(length)
        
    
    pass_len = {"l":4, "u":4, "c":4}        # default limit for splitting between lowercase, uppercase and characters

    """
    Logic is split the length into 3 equal parts using the python floor division operator(which leaves remainder
    then add the remainder randomly to either lowercase or uppercase or character length.
    """
    equal_3 = length // 3
    remainder = length % 3
    choose = random.choice(list(pass_len.keys()))

    for i in pass_len:
        pass_len[i] = pass_len[i] + equal_3

    for i in pass_len:
        if i == choose:
            pass_len[i] = pass_len[i] + remainder

    # print("Psst! Debugger: ",pass_len)    # debugger, check the length of the lowercase, uppercase and characters decided by this program.
    return pass_len
    

def password():
    print("This program will create a password for you!")
    print("Minimum characters limit is 12 but if you want you can generate a password higher than that limit")
    print("")
    print("Do you wanna generate higher than that?")
    res = input("'yes' or 'no' you can also type 'y' or 'n': ")

    if res.lower() in ['y', 'yes']:
        length = int(input("Please type the length in numbers: "))
    else:
        length = 12

    length = char_types_n_length(length)
    password = generate(length)

    print("=========================================")
    print(password)
    print("=========================================")
    

def main():
    password()


main()


# Good job :)
# I am proud of you!

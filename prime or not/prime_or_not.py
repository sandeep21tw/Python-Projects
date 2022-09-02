# This program tells whether a number is a prime number or not
# by Sandeep





def isprime(number):
    """
    how this works?

    we will iterate through all values and update the prime variable to
    False if number is divisible by any number before it.

    Note: we started from prime = True because we started from range(2)
    """
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    else:
        prime = True
    return prime







        
while True:
    number = int(input("Enter a number: "))
    if number > 0:
        print(isprime(number))
    else:
        print("Enter a valid number.")

import random
import string

X = int(input("Enter the length of password: "))
if (X < 6):
    print("password size should be at least 6 character!!! ")
else:
    symbol = "!@#$&_*"
    character = string.ascii_letters + string.digits + symbol
    password = ''.join(random.choice(character) for _ in range(X))
    print("Generated Pasword: ",password)
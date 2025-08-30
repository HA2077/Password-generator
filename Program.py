import random

print ("The password generator")
while (1 == 1):
    Length = int(input("Enter the length of the password (min 8 characters & max 32 characters): "))
    Lowercase = "abcdefghijklmnopqrstuvwxyz"
    Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Symbol = "!@#$%^&*()_+-=[]{}|;:,.<>?/~"
    Number = "0123456789"

    password_chars = [random.choice(Number), random.choice(Symbol), random.choice(Uppercase), random.choice(Uppercase), random.choice(Number), random.choice(Lowercase), random.choice(Lowercase), random.choice(Symbol)]
    if Length < 8:
        print("Password length should be at least 8 characters.")
    elif Length > 32:
        print("Password length should not exceed 32 characters.")
    else:
        for i in range(Length - 8):
            password_chars.append(random.choice(Lowercase + Uppercase + Symbol + Number))
        random.shuffle(password_chars)
        password = ''.join(password_chars)
        print("Generated password:", password)

    print("Do you want to generate another password? (yes/no)")
    if input().lower() != "yes":
        print ("--- Thank you for using the program ---")
        break
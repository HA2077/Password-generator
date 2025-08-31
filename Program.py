import random

def User_preferences():
    while True:
            UseLowercase = input("Include lowercase letters? (Y/N): ").strip().lower() == 'y'
            UseUppercase = input("Include uppercase letters? (Y/N): ").strip().lower() == 'y'
            UseSymbol = input("Include symbols? (Y/N): ").strip().lower() == 'y'
            UseNumber = input("Include numbers? (Y/N): ").strip().lower() == 'y'
            if not (UseLowercase or UseUppercase or UseSymbol or UseNumber):
                print("You must select at least one character type.")
                continue
            return UseLowercase, UseUppercase, UseSymbol, UseNumber

def Passgen(Length, UseLowercase, UseUppercase, UseSymbol, UseNumber, Lowercase, Uppercase, Symbol, Number):
    password_chars = []
    for i in range(Length):
        password_chars.append(random.choice((UseLowercase*Lowercase) + (UseUppercase*Uppercase) + (UseSymbol*Symbol) + (UseNumber*Number)))
    random.shuffle(password_chars)
    return ''.join(password_chars)

print ("The password generator")
while True:
    Length = int(input("Enter the length of the password (min 8 characters & max 32 characters): "))
    UseLowercase, UseUppercase, UseSymbol, UseNumber = User_preferences()
    Lowercase = "abcdefghijklmnopqrstuvwxyz"
    Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Symbol = "!@#$%^&*()_+-=[]{}|;:,.<>?/~"
    Number = "0123456789"

    password_chars = []
    if Length < 8:
        print("Password length should be at least 8 characters.")
    elif Length > 32:
        print("Password length should not exceed 32 characters.")
    else:
        password = Passgen(Length, Lowercase, Uppercase, Symbol, Number, UseLowercase, UseUppercase, UseSymbol, UseNumber)
        print("Generated Password: " + password)

    print("Do you want to generate another password? (yes/no)")
    if input().lower() != "yes":
        print ("--- Thank you for using the program ---")
        break
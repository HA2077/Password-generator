import secrets
import pyperclip

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
    passwordSET = set()
    available_chars = ""
    
    if UseLowercase: available_chars += Lowercase
    if UseUppercase: available_chars += Uppercase
    if UseSymbol: available_chars += Symbol
    if UseNumber: available_chars += Number

    if UseLowercase: passwordSET.add(secrets.choice(Lowercase))
    if UseUppercase: passwordSET.add(secrets.choice(Uppercase))
    if UseSymbol:    passwordSET.add(secrets.choice(Symbol))
    if UseNumber:    passwordSET.add(secrets.choice(Number))

    while len(passwordSET) < Length:
        Newchar = secrets.choice(available_chars)
        passwordSET.add(Newchar)

    Passwordchars = list(passwordSET)
    secrets.SystemRandom().shuffle(Passwordchars)
    return ''.join(Passwordchars)

print ("The password generator")
while True:
    Length = int(input("Enter the length of the password (min 8 characters & max 32 characters): "))
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
        UseLowercase, UseUppercase, UseSymbol, UseNumber = User_preferences()
        password = Passgen(Length, UseLowercase, UseUppercase, UseSymbol, UseNumber, Lowercase, Uppercase, Symbol, Number)
        print("Generated Password: " + password)
        pyperclip.copy(password)
        print("----------> Password copied to clipboard <----------")

    print("Do you want to generate another password? (yes/no)")
    if input().lower() != "yes":
        print ("--- Thank you for using the program ---")
        break
import secrets

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
        password_chars.append(secrets.choice((UseLowercase*Lowercase) + (UseUppercase*Uppercase) + (UseSymbol*Symbol) + (UseNumber*Number)))
    secrets.SystemRandom().shuffle(password_chars)
    return ''.join(password_chars)

def Improve_password(password, use_lowercase, use_uppercase, use_symbol, use_number, Lowercase, Uppercase, Symbol, Number):
    password_list = list(password)
    has_lowercase = any(c.islower() for c in password_list)
    has_uppercase = any(c.isupper() for c in password_list)
    has_symbol = any(not c.isalnum() for c in password_list)
    has_number = any(c.isdigit() for c in password_list)
    
    replacements = []
    if use_lowercase and not has_lowercase: replacements.append(secrets.choice(Lowercase))
    if use_uppercase and not has_uppercase: replacements.append(secrets.choice(Uppercase))
    if use_symbol and not has_symbol: replacements.append(secrets.choice(Symbol))
    if use_number and not has_number: replacements.append(secrets.choice(Number))

    for i, replacement in enumerate(replacements):
        if i < len(password_list):
            password_list[i] = replacement
    
    available_chars = ""
    if use_lowercase: available_chars += Lowercase
    if use_uppercase: available_chars += Uppercase
    if use_symbol: available_chars += Symbol
    if use_number: available_chars += Number

    seen = set()
    for i in range(len(password_list)):
        if password_list[i] in seen:
            for char in available_chars:
                if char not in seen:
                    password_list[i] = char
                    break
        seen.add(password_list[i])
    
    return ''.join(password_list)

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
        password = Improve_password(password, UseLowercase, UseUppercase, UseSymbol, UseNumber, Lowercase, Uppercase, Symbol, Number)
        print("Generated Password: " + password)

    print("Do you want to generate another password? (yes/no)")
    if input().lower() != "yes":
        print ("--- Thank you for using the program ---")
        break
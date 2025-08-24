import random

print ("The password generator")
Lowercase = "abcdefghijklmnopqrstuvwxyz"
Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Symbol = "!@#$%^&*()_+-=[]{}|;:,.<>?/~"
Number = "0123456789"

password_chars = [random.choice(Number), random.choice(Symbol), random.choice(Uppercase), random.choice(Uppercase), random.choice(Number), random.choice(Lowercase), random.choice(Lowercase), random.choice(Symbol)]
random.shuffle(password_chars)
password = ''.join(password_chars)

print("Generated password:", password)
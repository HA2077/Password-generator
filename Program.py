import random

print ("The password generator")
lowercase1 = chr(random.randint(97, 122))
lowercase2 = chr(random.randint(97, 122))
uppercase1 = chr(random.randint(65, 90))
uppercase2 = chr(random.randint(65, 90))
number1 = chr(random.randint(48, 57))
number2 = chr(random.randint(48, 57))
symbol1 = chr(random.randint(33, 47))
symbol2 = chr(random.randint(33, 47))

password_chars = [number2, symbol1, uppercase1, uppercase2, number1, lowercase1, lowercase2, symbol2]
random.shuffle(password_chars)
password = ''.join(password_chars)

print("Generated password:", password)
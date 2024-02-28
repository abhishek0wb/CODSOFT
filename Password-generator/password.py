import random
import string

special_char = string.punctuation
digits = string.digits
alphabates = string.ascii_letters


pool =  alphabates + digits + special_char

pass_lenght = int(input("How long do you want your password to be. Type in digits only \n"))

if pass_lenght <= 8:
   password =''.join(random.choice(pool) for _ in range (pass_lenght))
   print(password)
else:
   print("invaild input")


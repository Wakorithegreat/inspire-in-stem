import random
print("welcome to our project generator")
character = str("john wakori")
num_pass = int(input("enter number of password you would like to generate: "))
len_pass = int(input("length of password : "))

print(" \n here are your passwords : ")
for password in range(num_pass):
    password = " "
    for c in range(len_pass):
        password += random.choice(character)
    print(password)

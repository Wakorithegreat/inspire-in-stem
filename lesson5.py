# methods
from pkg_resources import safe_name


name = "john wakori"
name = "Ada love lace"
user_name = " Love lace"
age = 15
# age = 55
#person = "I am "str(name) +  "and my age is" + str(age)
#print(person)
# the format () method
#print("My name is {} and i am {}" .format(name, age)
# new line \n and tab \t
#print (f"My \t name is {name} \n and i am {age} years old")
print(user_name.lstrip())

#multiline strings

msg = """ QRST126XDG MPESA confirmed 
          you have received 1000 from john wakori
          18 may 2022
          safricom transparent for you
          """
print(msg)

#slice from the start
#by leaving out the start

city =    "Nairobi"
print(city[:5])


f_name = "john wakori" # SMALL LETTERS

print(f_name.upper())
s_name = "JOHN WAKORI"
print(s_name.lower())
#concatination -converting from one dat to another
#int -> float float(x)
#float -> int int (x)
#int -> string str(x)

number = 6
print(str(number))

y = 3.24
print(int(y))

f_name = "james"

s_name = "corden"

full_name = f_name + s_name
print(full_name)

name = "brett cooper"

print(name.replace("t" , "G"))

#the split () method returns a list where 

msg = "hello from john wakori how are you"
print(msg.split())
print(len(msg))
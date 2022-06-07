#!/usr/bin/python
###############
#functions
#name :john wakori
# date : 23/5/20
################




def say_hello():
    print("hello from JKUAT")

    x = 4
    y = 7
    z = x + y
    print(z)

say_hello()

def bark():
    print("dogs bark woof woof")

def cat():
     print("cat meows meows")
def wolf():
    print("a wolf howls howls")

bark()
cat()
wolf()

# a funcyions of adding numbers
def add_numbers (x,y):
    sum_nums = x + y
    print("the sum of the numbers : ",sum_nums)

add_numbers (40,50)
add_numbers (100,400)
add_numbers (1,4)

#a funcyion of multiplying numbers
def multiply_numbers (x,y):
    prod_nums = x * y
    print("the product of the numbers : ",prod_nums)

multiply_numbers (40,50)
multiply_numbers (100,400)
multiply_numbers (1,4)

#calling the function
import math
a = int(input("enter the coefficient of the first term "))
b = int(input("enter the coefficient of the second term "))
c = int(input("enter the constant(c)"))
w = math.sqrt((b**2)- 4*a*c)
def find_roots (a,b,c):
    y_1 = (( -b + w) /(2*a))
    y_2 = ((-b - w) /(2*a))
    print("the roots of the equation are :", y_1,y_2)
find_roots(a,b,c)

#using default parameters
def print_name (name = "john wakori " ):
    print(name)
print_name("rogue")
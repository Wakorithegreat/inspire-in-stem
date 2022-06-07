# using default parameters
def print_name (name = "john wakori " ):    
    print(name)
print_name("rogue")

#return from a function
def get_sum(num1 ,num2):
    sum_nums = num1 +num2
    return sum_nums
print(get_sum(5,83))

#function to get square of numbers
def powers(number , power):
    pow_num = number**power
    return pow_num
print(powers(5,6))

# printing full name
def get_full_name(f_name , s_name):
    full_name = f_name + " "  +  s_name
    return full_name.title()
print(get_full_name("john","wakori"))

# returning a dictionary
def create_full_name(f_name , s_name):
    person = {'first':f_name,'second':s_name}
    return person
student = create_full_name("john","wakori")
print(student)

# passing a list in a funtion
def greet_friends(names):
    for name in names:
        msg = " hello " + name.title() + " ! "
        print(msg)
friends = ['wakori', 'john', 'ngaruiya', 'moses']
greet_friends(friends)
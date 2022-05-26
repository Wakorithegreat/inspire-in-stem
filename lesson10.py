#!/usr/bin/python
#sum of numbers between (0,50)

sum_nums = 0
for numbers in range(0,50):
    if(numbers %2 == 0):
        sum_nums = sum_nums + numbers
        #print(sum_nums)

#product of numbers btw (0,50)
prod_nums = 1
for numbers in range(0,50):
    if(numbers %2 == 1):
        prod_nums = prod_nums *numbers
#print(prod_nums)

num = 0
while num < 10:
    if(num % 2 == 0):

        print(num)
    num = num + 1
        

    
   
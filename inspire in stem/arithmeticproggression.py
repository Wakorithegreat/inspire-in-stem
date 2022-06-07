#the first n terms of AP
a = int(input("enter the number"))
d = int(input("enter the number"))
n =int(input("enter the number"))
for i in  range ( 1,n+1):
    n_term = a + (i -1)*d
    print(n_term)

sum_n = (n_term/2)*(2*a +(n - 1)*d)
print(sum_n)
####
def isPalindrome(p):
    return p== p[::-1]
p =str(input("enter word or numbers : "))
ans = isPalindrome(p)
if ans:
    print("yes")
else:
    print("no")

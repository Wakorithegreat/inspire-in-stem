f = open("lesson.txt") #open existing file
f = open("lesson1.txt", 'x') #creates new file

print (f.readline())
"""
with open("lesson2.txt",'w') as f:#creates file and has writen addition
    f.write("this is my new file \n")
    f.write("i am john wakori \n")
    f.write("i am from nairobi \n")
#reading the file
print(f.read())
f.close()

f.read()

f.seek()
"""
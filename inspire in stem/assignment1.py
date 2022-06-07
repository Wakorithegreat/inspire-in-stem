#print all in upper case using loop
colors = ['red','green','blue','purple']

for color in colors:
    if(colors[0] == "red",colors[1]=="green",colors[2],"blue",colors[3],"purple"):
        print(colors[0].upper(),colors[1].upper(), colors[2].upper(),colors[3].upper())
colors = ["red","green","blue","purple"]
i = 0
while i < len(colors):
    if (colors[0] == 'green'):
        #print(colors[0].upper())
        i += 1 #this closes the loop ,so that the value is not run many times 

for color in colors:
    if(colors[0] == "red"):
        #print(colors[0].upper())
        i += 1
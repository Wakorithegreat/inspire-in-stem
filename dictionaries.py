#dictionaries is acollection of key value pairs
#syntax : dictionary = ["key":value]
list_name = {'john','mary'}
colors = {'color':"red"} 
vehicle = {'type':'toyota','plate_number':'HTLM45'}
#print(type(colors)) #use the type method
#acccessing values in a dictionary
#print(vehicle['type']) # you can ccess the value of an element inside adictionary using the key
#print type and plate number
#print(vehicle['type'] ,vehicle['plate_number'])
#creating dictionary person

person = {"name":"john",
         "phone_number":"0791511325",
         "location":"nairobi"}
person['age'] = '21'
person['color'] = 'orange'
del person['phone_number']
#print(type(person))
#print(person)
#lopping over adictionaries
for key , value in person.items():
    #print(f'{key}:{value}')

 colors = ["red","green","blue","purple"]
i = 0
while i < len(colors):
    if (colors[0] == 'green'):
        print(colors[0].upper())
        i += 1 #this closes the loop ,so that the value is not run many times 

for color in colors:
    if(colors[0] == "red"):
        print(colors[0].upper())
        i += 1

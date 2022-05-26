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
 # print(person.get('location','the location key is non existent'))
#using get to access value in adictionary

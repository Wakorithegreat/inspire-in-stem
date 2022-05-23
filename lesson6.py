#learning about lists
motorcycle_owner = "mojo jojo"
plate_number = ['HL234','YL234','SL234']
motorcycle = ["honda","yamaya","suzuki"]
#accessing list items using index
#print(motorcycle)
#motorcycle[2] = "buggati" #changing element in a list
#print( "(i love "  + str((motorcycle[0])))
#adding an element in a list
#motorcycle.append ('buggati')#adding item into a list
#task --- print the  motorcycle and thier plate number
#print(motorcycle[0],plate_number[0])
#print(motorcycle[1],plate_number[1])
#print(motorcycle[2],plate_number[2]
#deleting item from a list --del
# del motorcycle[0] #deleting an item from alist
popped_motorcycle = motorcycle.pop()
#print(popped_motorcycle)
#print a statement :my name is mojo jojo and i own a motorcycle plate number
#print("my name is " + str(motorcycle_owner) + " and i own a " + (motorcycle[0]))
#print("my name is {} and i own a {} with plate number {} " . format(motorcycle_owner,motorcycle[0], plate_number[0]))

#removing n iten from a list
#motorcycle.remove('yamaha')
#print(motorcycle)

print(motorcycle[-1])
motorcycle[1] = "duggati"

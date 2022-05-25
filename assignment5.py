#create a list of vehicles with the following:bmw,audi,toyota,mercedes,jeep 
#using if state#ment find a jeep inside the list and convert into upper case 
 
vehicles = ["bmw","audi","toyota","mercedes","jeep"]
# a list of vehicles
for vehicle in vehicles :
    print(vehicle.title())
if(vehicle == "jeep"):
    print(vehicle.upper())



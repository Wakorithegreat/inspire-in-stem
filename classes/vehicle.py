class Vehicle :
    def __init__(vehicle , _max_speed , _mileage):
        vehicle.max_speed = _max_speed
        vehicle.mileage = _mileage 

    def sayHi(vehicle):
            print("vehicle maximum speed : " + str(vehicle.max_speed) + " vehicle mileage : " + str(vehicle.mileage))
mercedes = Vehicle('260km/h',' 0m')
mercedes.sayHi()
    
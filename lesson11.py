mary_fav_food = ['beef','chicken','vegetable']
jane_fav_food = ['rice','ugali','potato']
#ditionary containing the above
food ={
       'mary':['beef','chicken','vegetable'],
       'jane':['rice','ugali','potato']
       }

for key , value in food.items():
       print(f'{key}: {value}')

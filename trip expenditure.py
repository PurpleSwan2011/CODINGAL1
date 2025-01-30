def hote_cot(nights):
    return 140*nights
def plane_ride_cost(city):
    if "charlotte"==city:
        return 183
    elif "tampa"==city:
        return 220
    elif "pittsburgh"==city:
        return 
    elif "los angeles"==city:
        return 
def rental_car_cost(days):
    if 7>=days:
        return 40*days-50
    elif 3>=days:
        return 40*days-30
    else:
        return 40*days
def trip_cost(city,days,spending_money):
    return rental_car_cost(days)+hotel_cost(days)+plan_ride_cost(city)+spending_money
print("cost of car rental",rental_car_cost(5))
print("cost of plane ride"),plan_ride_cost(los angeles)
print("cost of hotel room",hotel_cost(7))
print("total cost of trip",trip_cost,"los angeles",7,500)
print("trip cost("tampa),6,500")
# the holiday calculator will calculate the cost of the whole holiday
# taking the inputs from the user and working out all the details plus the final total cost
print()
for i in range(50):
  print("*", end=" ")
print()
print("holiday calculator".upper())
print()
print("Our destinations: London, Paris, Rome, Madrid, Vienna")
print()
# "destinations" is a dictionary with all the destinations as keys and the relevant cost as value  
destinations={"London": 100, "Paris": 120, "Rome": 110, "Madrid": 125, "Vienna": 115}

# the lines below ask the user to input the values for the functions
city_flight=(input("Please, select your destination: ")).lower()
print()
num_nights=int(input("Number of nights you will stay at the hotel: "))
rental_days=int(input("Number of days you will be hiring a car for: "))
print()
print()

# below are the three main functions: hotel_cost, plane_cost and car_rental
def hotel_cost(num_nights, one_night):
  return num_nights*one_night

# the if sentences followed by the get() methods let the program retreive the values for each destination
def plane_cost(city_flight):
    if city_flight == "london":
        return destinations.get("London")
    elif city_flight == "paris":
        return destinations.get("Paris")
    elif city_flight == "rome":
        return destinations.get("Rome")
    elif city_flight == "madrid":
        return destinations.get("Madrid")
    elif city_flight =="vienna":
        return destinations.get("Vienna")
                
def car_rental(rental_days, one_day):
  return rental_days*one_day

# one final function to sum the result of the previous three.
# seen that the sum of functions doesn't support the "+" operator,
# I created three variables (cost1, 2 and 3) to store the results of the functions,
# then created an empty list(total=[])
# finally appended the three variables and return the sum of them.
def holiday_cost(hotel_cost, plane_cost, car_rental):
   cost1=hotel_cost(num_nights, 50)
   cost2=plane_cost(city_flight)
   cost3=car_rental(rental_days, 60)
   total=[]
   total.append(cost1)
   total.append(cost2)
   total.append(cost3)
   return cost1+cost2+cost3


# finally, all the functions get called and printed
print("The hotel will cost: ", hotel_cost(num_nights, 50))
print("Your flight cost: ", plane_cost(city_flight))
print("The car will cost: ", car_rental(rental_days, 60))
print()
print("The total cost for your holiday is: £". upper(), holiday_cost(hotel_cost, plane_cost, car_rental))
print()
for i in range(50):
  print("*", end=" ")

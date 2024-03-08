# Print holiday destinations.
# Ask user to pick a city, numember of hotel nights and car rental days
print ('You can choose a holiday to the following destinations: ') 
print ('LA \nNYC \nLas Vegas \nHonolulu')

city_flight = input("Where are you flying to? ")
num_nights = int(input("How many days are you staying at the hotel? "))
rental_days = int(input("How many days will you hire a car? "))

city_flight = city_flight.upper()

# Create function whith the argument city_flight.
# Function determine the price of the flight with if and elif statements.
def plane_cost(city_flight):
    if city_flight == "LA":
        return 800
    elif city_flight == "NYC":
        return 600
    elif city_flight == "LAS VEGAS":
        return 700
    elif city_flight == "HONOLULU":
        return 1200
    else:
        print ('Your destination is not recognised, please try again.')
    
print (f"Total flight costs to {city_flight} is ${plane_cost(city_flight)}. ")


# Create the function hotel_cost with num_nights as argument.
# Calculate total hotel costs with price per night fixed at 200.
def hotel_cost(num_nights,price_per_night=200):
    total = num_nights * price_per_night
    return total

print (f"Total hotel costs will be ${hotel_cost(num_nights)}.")

# Create the function car_rental with rental_days as argument.
# Calculate total with price per day fixed at 60
def car_rental(rental_days,price_per_day=60):
    total = rental_days * price_per_day
    return total

print (f'Total car rental costs will be ${car_rental(rental_days)}.')


# Create function holiday_costs to sum all outcomes from above.
def holiday_cost(hotel_cost,plane_cost,car_rental):
    total = hotel_cost + plane_cost + car_rental
    return total

hotel_cost = hotel_cost(num_nights)
plane_cost = plane_cost(city_flight)
car_rental = car_rental(rental_days)

print (f"\nTotal holiday cost will be ${holiday_cost(hotel_cost,plane_cost,car_rental)}.") 
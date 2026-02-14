# Daniel Kantor
# February 14, 2026
# P2LAB2
# Code that stores key, value pairs inside a dictionary and interacts with the User


car_dict = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}
keys = car_dict.keys()
values = car_dict.values()

print(keys)
user_car = input("\nPlease pick one of the vehicles displayed above. ")

if user_car in car_dict:
    print(f"The {user_car} gets {car_dict[user_car]} mpg.")
else:
    print("That vehicle is not within the dictionary. Sorry")

user_mileage = float(input(f"\nHow many miles will you drive the {user_car}? "))

if user_mileage <= 0:
    print("So... you're not going anywhere?")
else:
    mpg_needed = user_mileage / car_dict[user_car]
    print(f"{mpg_needed:.2f} gallon(s) of gas are needed to drive the {user_car} {user_mileage} miles.")
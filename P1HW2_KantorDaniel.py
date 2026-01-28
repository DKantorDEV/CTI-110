# Daniel Kantor
# January 28, 2026
# P1HW2
# This python code will do mathmatical sequences to calculate whatever numbers we want it to.


# Pseudocode Logic:
# 1) Display what this program does
# 2) Ask user their budget
# 3) Their travel destination
# 4) How much they will spend on gas
# 5) How much they will spend on a hotel
# 6) How much they need for food
# 7) All that gets calculated in remaining_balance variable
# 8) Returns all the information to the user with the calculations complete



print("This program calculates and displays travel expenses")

print("\n")

budget = int(input("Enter Budget: "))

print("\n")

location = input("Enter your travel destination: ")

print("\n")

gas_money = int(input("How much do you think you will spend on gas? "))

print("\n")

hotel_money = int(input("Approximately, how much will you need for accomodation/hotel? "))

print("\n")

food_money = int(input("Last, how much do you need for food? "))

print("\n")

remaining_balance = budget - (gas_money + hotel_money + food_money)

print("------------Travel Expenses------------")

print(f"Location: {location}")
print(f"Initial Budget: {budget}")

print("\n")

print(f"Fuel: {gas_money}")
print(f"Accomodation: {hotel_money}")
print(f"Food: {food_money}")

print("\n")

print(f"Remaining Balance: {remaining_balance}")
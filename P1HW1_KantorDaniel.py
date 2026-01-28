# Daniel Kantor
# January 28, 2026
# P1HW1
# This program will use mathmatical expressions to do what we tell it to do.

print("-----Calculating Exponents-----")

print("\n")

base_value = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

total = base_value ** exponent

print("\n")

print(f"{base_value} raised to the power of {exponent} is {total} !!")

print("\n")

print("-----Addition and Subtraction-----")

print("\n")

first_int = int(input("Enter a starting integer: "))
second_int = int(input("Enter an integer to add: "))
third_int = int(input("Enter an integer to subtract: "))

total_int = first_int + second_int - third_int

print("\n")

print(f"{first_int} + {second_int} - {third_int} is equal to {total_int}")
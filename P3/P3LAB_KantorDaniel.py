# Daniel Kantor
# February 14, 2026
# P3LAB
# User enters a money value, gets returned efficient result of currency amount (coins/dollars)



change = float(input("Change amount as a float: $"))
change = int(change * 100)


# Logic for quantity of what change needs to be given

# Dollar Logic
num_dollars = change // 100
change -= (num_dollars * 100)

# Quarter Logic
num_quarters = change // 25
change -= (num_quarters * 25)

# Dime Logic
num_dimes = change // 10
change -= (num_dimes * 10)

# Nickel Logic
num_nickels = change // 5
num_nickels -= (num_nickels * 5)

# Penny Logic
num_pennies = change


# if statements for printing how much of what needs to be displayed

if num_dollars > 0:
    print(f"{num_dollars} Dollar(s)")

if num_quarters > 0:
    print(f"{num_quarters} Quarter(s)")

if num_dimes > 0:
    print(f"{num_dimes} Dime(s)")

if num_nickels > 0:
    print(f"{num_nickels} Nickel(s)")

if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} Penny")
    else:
        print(f"{num_pennies} Pennies")
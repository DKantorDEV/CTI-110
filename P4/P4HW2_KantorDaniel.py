# Daniel Kantor
# February 14, 2026
# P4HW2
# Displays a workers paystub/info and keeps a running count

# Pseudocode
# 1) Create global variables to tally counts for different employees
# 2) Start a while loop so this program continues until made false i.e. "Done"
# 3) Ask for Employees name and if it is "Done" terminate the program
# 4) If not, ask the hours and pay rate
# 5) Calculate the overtime/regular hours
# 6) Add the total count of that single employee to be added to the global variables.
# 7) Display that employees paystub then the same prompt again because the while loop restarted
# 8) If continue, run the program again
# 9) If the user types "Done", terminate the program then print the global variables



repeat = True

# Variables declared so we can count the total for x amount of employees
total_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

while repeat:

    # Start of the program
    employee_name = input("""\nEnter employee's name or "Done" to terminate: """)

    if employee_name == "Done":
        break

    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    if hours_worked > 40:
        regular_hours = 40
        overtime_hours = hours_worked - 40
    else:
        regular_hours = hours_worked
        overtime_hours = 0

    # Total amount for each part
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay


    print(f"\nEmployee name:    {employee_name}\n")


    print(f"{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<15}{"RegHour Pay":<15}{"Gross Pay":<12}")
    print("-" * 80)

    print(f"{hours_worked:<15}{pay_rate:<12.2f}{overtime_hours:<12}${overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<12.2f}")

#------------------------------------------------------------------------------------------------------------------------------------------------

print(f"\nTotal number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
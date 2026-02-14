# Daniel Kantor
# February 14, 2026
# P3HW2
# Displays a workers paystub/info


# User inputs required info for questions asked
employee_name = input("Enter employee's name: ")
hours_worked = int(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))


# Calculate pay hours based off hours_worked
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


print("-" * 40)
print(f"Employee's name:    {employee_name}\n")


print(f"{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<15}{"RegHour Pay":<15}{"Gross Pay":<12}")
print("-" * 80)

print(f"{hours_worked:<15}{pay_rate:<12}{overtime_hours:<12}${overtime_pay:<15}${regular_pay:<15}${gross_pay:<12}")
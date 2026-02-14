# Daniel Kantor
# February 14, 2026
# P2HW2
# Takes user grades per module and calculates a series of results (lowest, highest, sum and avg)


# Pseudocode Logic:
# 1) Display what we want the user to answer
# 2) Have the user's answer appended to an empty list
# 3) Calculate everything we want displayed before being displayed
# 4) Display the results


user_grades = []

user_grades.append(float(input("Enter grade for Module 1: ")))
user_grades.append(float(input("Enter grade for Module 2: ")))
user_grades.append(float(input("Enter grade for Module 3: ")))
user_grades.append(float(input("Enter grade for Module 4: ")))
user_grades.append(float(input("Enter grade for Module 5: ")))
user_grades.append(float(input("Enter grade for Module 6: ")))
print('\n')

# Calculations Made Here
lowest_grade = min(user_grades)
highest_grade = max(user_grades)
sum_of_grade = sum(user_grades)
avg_grade = sum_of_grade / len(user_grades)

# Displayed Results
print("---------------- Results ----------------")
print(f"Lowest Grade:          {lowest_grade}")
print(f"Highest Grade:         {highest_grade}")
print(f"Sum of Grades:         {sum_of_grade}")
print(f"Average:               {avg_grade:.2f}")
print("-----------------------------------------")
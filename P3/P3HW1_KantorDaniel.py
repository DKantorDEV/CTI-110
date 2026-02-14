# Daniel Kantor
# February 14, 2026
# P3HW1
# Takes user grades per module and calculates a series of results (lowest, highest, sum and avg)



# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))


# add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]


# TO DO: determine lowest, highest , sum and average for grades
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grade = sum(grades)
avg_grade = sum_of_grade / len(grades)


# Results Displayed Here
print("\n---------------- Results ----------------")
print(f"Lowest Grade:          {lowest_grade}")
print(f"Highest Grade:         {highest_grade}")
print(f"Sum of Grades:         {sum_of_grade}")
print(f"Average:               {avg_grade:.2f}")
print("-----------------------------------------")


# determine letter grade for average
if avg_grade >= 90:
    print('Your grade is: A')
elif avg_grade >= 80:
    print('Your grade is: B')
elif avg_grade >= 70:
    print('Your grade is: C')
elif avg_grade >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')
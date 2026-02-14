# Daniel Kantor
# February 14, 2026
# P4HW1
# Takes a users scores, calculates and displays certain parameters (lowest, new list, avg and etc.)


# Pseudocode Logic:
# 1) Ask the user the amount of scores to enter
# 2) Create empty list before for loop
# 3) Create for loop based on number user entered
# 4) while loop so it continues so long as it's true
# 5) If number is valid, sets it to score
# 6) If number is invalid, repeats the question
# 7) Calculate / remove what is necessary
# 8) if statements for the letter grades
# 9) Display everything


amount_of_scores = int(input("How many scores do you want to enter? "))

print('\n')

valid_score_list = []

for _ in range(amount_of_scores):

    while True:
        score = float(input(f"Enter score #{_ + 1}: "))

        if 0 <= score <= 100:
            valid_score_list.append(score)
            break
        else:
            print("\nINVALID Score entered!!!!")
            print("Score should be between 0 and 100.")


# Finding the values before displaying
lowest_score = min(valid_score_list)
valid_score_list.remove(lowest_score)
avg_score = sum(valid_score_list) / len(valid_score_list)

# Grade decision
grade = None

if avg_score >= 90:
    grade = "A"
elif avg_score >= 80:
    grade = "B"
elif avg_score >= 70:
    grade = "C"
elif avg_score >= 60:
    grade = "D"
else:
    grade = "F"


# Displayed Results
print("\n---------------- Results ----------------")
print(f"Lowest Score:           {lowest_score}")
print(f"Modified List:          {valid_score_list}")
print(f"Scores Average:         {avg_score:.2f}")
print(f"Grade:                  {grade}")
print("-----------------------------------------\n")
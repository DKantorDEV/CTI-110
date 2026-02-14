# Daniel Kantor
# February 14, 2026
# P4LAB2
# Loop program that shows a users # multiplied by the numbers 1 - 12


run_program = True

while run_program:
    user_number = int(input("\nEnter an integer: "))

    if user_number < 0:
        print("\nThis program does not handle negative numbers.")

    else:
        for i in range(1, 13):
            result = user_number * i
            print(f"{user_number} * {i} = {result}")

    repeat_program = input("\nWould you like to run the program again? (yes/no): ").lower()
    if repeat_program != "yes":
        run_program = False
        print("\nExiting program...\n")
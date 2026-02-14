# Daniel Kantor
# February 14, 2026
# P4LAB2
# Loop program that shows a users # multiplied by the numbers 1 - 12


run_program = True

while run_program:

    user_number = int(input("\nEnter an integer: "))

    print('\n')

    if user_number < 0:
        print("This program does not handle negative numbers.\n")
        repeat_program = input("Would you like to run the program again? ")
        if repeat_program != "yes":
            run_program = False
            print("\nExiting program...")
    else:
        for _ in range(1, 13):
            result = user_number * _
            print(f"{user_number} * {_} = {result}")

    repeat_program = input("\nWould you like to run the program again? ")
    if repeat_program != "yes":
            run_program = False
            print("\nExiting program...\n")
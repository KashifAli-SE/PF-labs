try:
    # Attempt to take input from the user
    user_input = input("Enter something (or press Ctrl+Z to simulate EOF): ")
    print("You entered:", user_input)
except EOFError:
    print("EOFError: No input received, end of file reached.")

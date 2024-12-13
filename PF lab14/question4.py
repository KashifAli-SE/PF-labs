try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except IOError:
    print("IOError: The file could not be opened or read because it does not exist.")

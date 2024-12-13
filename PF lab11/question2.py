def create_directory():
    phone_directory = {
        "Ali (Father)": "0301-1234567",
        "Ayesha (Mother)": "0302-7654321",
        "Ahmed (Brother)": "0311-2345678",
        "Fatima (Sister)": "0321-8765432",
        "Hamza (Friend)": "0333-4567890",
        "Sara (Friend)": "0345-9876543",
        "Bilal (Friend)": "0308-1122334",
        "Zainab (Friend)": "0315-2233445",
        "Hina (Friend)": "0331-3344556",
        "Usman (Friend)": "0340-5566778",
        "Amna (Friend)": "0304-6677889",
        "Yousuf (Friend)": "0317-7788990"
    }
    return phone_directory
def delete_member(phone_directory, name):
    if name in phone_directory:
        del phone_directory[name]
        print(f"{name} has been deleted from the directory.")
    else:
        print(f"{name} not found in the directory.")
        
def print_total_members(phone_directory):
    print(f"Total members in the phone directory: {len(phone_directory)}")

phone_directory = create_directory()

# Print the initial directory and total members
print("Initial Phone Directory:")
for name, number in phone_directory.items():
    print(f"{name}: {number}")
print_total_members(phone_directory)

# Delete a member
delete_member(phone_directory, "Sara (Friend)")

# Print the updated directory and total members
print("\nUpdated Phone Directory:")
for name, number in phone_directory.items():
    print(f"{name}: {number}")
print_total_members(phone_directory)

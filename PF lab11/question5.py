def get_guest_list():
    guests = {}
    print("Enter guest names and the number of family members attending. Type 'done' when finished.")
    while True:
        guest = input("Guest Name (or 'done' to finish): ").strip()
        if guest.lower() == 'done':
            break
        try:
            members = int(input(f"How many family members for {guest}? "))
            guests[guest] = members
        except ValueError:
            print("Please enter a valid number for family members.")
    return guests

def find_common_guests(list1, list2):
    return {guest: max(list1[guest], list2[guest]) for guest in list1 if guest in list2}

def total_guest_count(guest_list):
    return sum(guest_list.values())

# Get guest lists from you and your parents
print("Enter your guest list:")
my_guests = get_guest_list()
print("\nEnter your parents' guest list:")
parents_guests = get_guest_list()

# Find common guests
common_guests = find_common_guests(my_guests, parents_guests)

all_guests = {**my_guests, **parents_guests}
for guest in common_guests:
    all_guests[guest] = common_guests[guest]

total_guests_with_members = total_guest_count(all_guests)
total_individual_guests = len(all_guests)

print("\nCommon Guests:", common_guests)
print("Total Guests (including family members):", total_guests_with_members)
print("Total Individual Guests:", total_individual_guests)

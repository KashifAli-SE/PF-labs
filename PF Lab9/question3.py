best_dishes= set()
while True:
    dish=input("enter your favourite dish or Q to end ")
    if dish=='Q':
        break
    best_dishes.add(dish)
print("Best Dishes:", best_dishes)
while best_dishes:
    dish = best_dishes.pop()
    print("Removed:", dish)
    print("Remaining Dishes:", best_dishes)
print("All dishes have been removed. The set is now empty.")



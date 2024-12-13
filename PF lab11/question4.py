def compare_dishes():
    favorite_dishes = {
        1: "Biryani",
        2: "Karahi",
        3: "Haleem",
        4: "Pulao",
        5: "Koftay",
        6: "Qorma"
    }
    # Dictionary of dishes cooked in a week
    cooked_dishes = {
        "Monday": "Karahi",
        "Tuesday": "Nihari",
        "Wednesday": "Haleem",
        "Thursday": "Biryani",
        "Friday": "Aloo Gosht",
        "Saturday": "Pulao",
        "Sunday": "Daal Chawal"
    }
    # Find matching dishes
    favorite_cooked = [dish for dish in cooked_dishes.values() if dish in favorite_dishes.values()]

    # Print results
    print(f"Dishes you will get of your choice next week: {len(favorite_cooked)}")
    print("These dishes are:")
    for dish in favorite_cooked:
        print(f"- {dish}")

compare_dishes()

dog_only = 83
cat_only = 101
fish_only = 22
dog_cat = 31
dog_fish = 8
cat_fish = 10
dog_cat_fish = 6
other_pets = 34

dog_only_count = dog_only - dog_cat - dog_fish + dog_cat_fish
cat_only_count = cat_only - dog_cat - cat_fish + dog_cat_fish
dog_or_fish_count = dog_only + fish_only - dog_fish

total_purchases = (
    dog_only + cat_only + fish_only 
    - dog_cat - dog_fish - cat_fish 
    + dog_cat_fish + other_pets
)
print("i. Purchases for a dog product only:", dog_only_count)
print("ii. Purchases for a cat product only:", cat_only_count)
print("iii. Purchases for a dog or a fish product:", dog_or_fish_count)
print("iv. Total purchases:", total_purchases)

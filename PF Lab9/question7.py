# Venn diagram regions
only_english = 25
only_spanish = 10
only_french = 11
english_spanish_not_french = 20
english_french_not_spanish = 17
spanish_french_not_english = 9
all_three = 13
# Total students
total_students = 110
# Sum of all regions
sum_regions = (
    only_english
    + only_spanish
    + only_french
    + english_spanish_not_french
    + english_french_not_spanish
    + spanish_french_not_english
    + all_three
)
# Calculations
neither_languages = total_students - sum_regions
exactly_two_languages = (
    english_spanish_not_french + english_french_not_spanish + spanish_french_not_english
)
only_one_language = only_english + only_spanish + only_french
# Results
print("a. English and Spanish but not French:", english_spanish_not_french)
print("b. Neither English, Spanish, nor French:", neither_languages)
print("c. French, but neither English nor Spanish:", only_french)
print("d. Only one of the three languages:", only_one_language)
print("e. Exactly two of the three languages:", exactly_two_languages)

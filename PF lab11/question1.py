family = {
    "father": "Ali",
    "mother": "Ayesha",
    "siblings": ["kashif", "jawad"]
}

print("Initial family dictionary:")
print(family)

family.update({
    "paternal_grandparents": {"grandfather": "Akbar", "grandmother": "Zainab"},
    "maternal_grandparents": {"grandfather": "Yousuf", "grandmother": "Khadija"},
    "paternal_uncles": ["Hamza", "Bilal"],
    "maternal_uncles": ["Ibrahim", "Usman"],
    "paternal_aunts": ["Sana", "Farah"],
    "maternal_aunts": ["Amna", "Hina"]
})
print("\nUpdated family dictionary:")
print(family)

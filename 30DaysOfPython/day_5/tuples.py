# Module 5: Tuples

# --------------------
# Level 1
# --------------------

# 1. Create an empty tuple
empty_tuple = ()

# 2. Tuple of sisters and brothers
sisters = ('Aisha', 'Zainab')
brothers = ('Abdullahi', 'Sadiq')

# 3. Join brothers and sisters
siblings = sisters + brothers
print("Siblings:", siblings)

# 4. Number of siblings
print("Number of siblings:", len(siblings))

# 5. Add parents to siblings and assign to family_members
family_members = siblings + ('Father', 'Mother')
print("Family members:", family_members)

# --------------------
# Level 2
# --------------------

# 6. Unpack siblings and parents
*siblings, father, mother = family_members
print("Siblings:", siblings)
print("Father:", father)
print("Mother:", mother)

# 7. Create food tuples
fruits = ('Apple', 'Banana', 'Orange')
vegetables = ('Carrot', 'Spinach', 'Onion')
animal_products = ('Milk', 'Eggs', 'Meat')

# Join food tuples
food_stuff_tp = fruits + vegetables + animal_products
print("Food stuff tuple:", food_stuff_tp)

# 8. Convert tuple to list
food_stuff_lt = list(food_stuff_tp)
print("Food stuff list:", food_stuff_lt)

# 9. Slice middle item(s)
length = len(food_stuff_tp)
middle = length // 2

if length % 2 == 0:
    print("Middle items:", food_stuff_tp[middle - 1: middle + 1])
else:
    print("Middle item:", food_stuff_tp[middle])

# 10. Slice first three and last three items
print("First three:", food_stuff_lt[:3])
print("Last three:", food_stuff_lt[-3:])

# 11. Delete food_stuff_tp
del food_stuff_tp

# 12. Check if a country is nordic
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print("Estonia is a nordic country:", 'Estonia' in nordic_countries)
print("Iceland is a nordic country:", 'Iceland' in nordic_countries)

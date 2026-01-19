# Module 8: Dictionaries

# 1. Create an empty dictionary
dog = {}

# 2. Add name, color, breed, legs, age
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'German Shepherd'
dog['legs'] = 4
dog['age'] = 5

print("Dog dictionary:", dog)

# 3. Create a student dictionary
student = {
    'first_name': 'Yusuf',
    'last_name': 'Bugaje',
    'gender': 'Male',
    'age': 26,
    'marital_status': 'Single',
    'skills': ['Python', 'Git'],
    'country': 'Nigeria',
    'city': 'Katsina',
    'address': 'Katsina State'
}

print("Student dictionary:", student)

# 4. Get the length of the student dictionary
print("Length of student dictionary:", len(student))

# 5. Get the value of skills and check data type
skills = student['skills']
print("Skills:", skills)
print("Type of skills:", type(skills))

# 6. Modify skills by adding new skills
student['skills'].append('JavaScript')
student['skills'].append('SQL')
print("Updated skills:", student['skills'])

# 7. Get dictionary keys as a list
keys_list = list(student.keys())
print("Keys:", keys_list)

# 8. Get dictionary values as a list
values_list = list(student.values())
print("Values:", values_list)

# 9. Change dictionary to list of tuples
items_list = list(student.items())
print("Dictionary as list of tuples:", items_list)

# 10. Delete one item from dictionary
del student['address']
print("After deleting address:", student)

# 11. Delete one of the dictionaries
del dog

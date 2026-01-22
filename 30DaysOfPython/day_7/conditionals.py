# Module 7: Conditionals

# --------------------
# Level 1
# --------------------

# 1. Driving age check
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_left = 18 - age
    print(f"You need {years_left} more years to learn to drive.")


# 2. Compare my_age and your_age
my_age = 25
your_age = int(input("Enter your age: "))

age_diff = abs(my_age - your_age)

if your_age > my_age:
    if age_diff == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {age_diff} years older than me.")
elif your_age < my_age:
    if age_diff == 1:
        print("You are 1 year younger than me.")
    else:
        print(f"You are {age_diff} years younger than me.")
else:
    print("We are the same age.")


# 3. Compare two numbers
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")


# --------------------
# Level 2
# --------------------

# 4. Student grade system
score = int(input("Enter student score: "))

if 80 <= score <= 100:
    print("Grade: A")
elif 70 <= score <= 89:
    print("Grade: B")
elif 60 <= score <= 69:
    print("Grade: C")
elif 50 <= score <= 59:
    print("Grade: D")
elif 0 <= score <= 49:
    print("Grade: F")
else:
    print("Invalid score")


# 5. Season checker
month = input("Enter a month: ").capitalize()

if month in ['September', 'October', 'November']:
    print("Season: Autumn")
elif month in ['December', 'January', 'February']:
    print("Season: Winter")
elif month in ['March', 'April', 'May']:
    print("Season: Spring")
elif month in ['June', 'July', 'August']:
    print("Season: Summer")
else:
    print("Invalid month")


# 6. Fruit checker
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ").lower()

if fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit)
    print("Updated fruits list:", fruits)


# --------------------
# Level 3
# --------------------

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 7. Print middle skill
if 'skills' in person:
    skills = person['skills']
    middle_skill = skills[len(skills) // 2]
    print("Middle skill:", middle_skill)

# 8. Check for Python skill
if 'skills' in person:
    print("Has Python skill:", 'Python' in person['skills'])

# 9. Determine developer type
skills_set = set(person['skills'])

if {'JavaScript', 'React'} <= skills_set and len(skills_set) == 2:
    print("He is a front end developer")
elif {'Node', 'Python', 'MongoDB'} <= skills_set:
    print("He is a backend developer")
elif {'React', 'Node', 'MongoDB'} <= skills_set:
    print("He is a fullstack developer")
else:
    print("Unknown title")

# 10. Marriage and country check
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")

# Day 2: 30 Days of python programming

first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on = (
    'Yusuf', 'Bugaje', 'Yusuf Bugaje', 'Nigeria', 'Katsina', 26, 1999, False, True, True
)

# Data types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# Length
print(len(first_name))

# Compare name lengths
print(len(first_name) == len(last_name))

# Numbers
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
variable_exp = num_one ** num_two
floor_division = num_one // num_two

print(total, diff, product, division, remainder, variable_exp, floor_division)

# Circle calculations
radius = 30
pi = 3.14

area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius

print(area_of_circle)
print(circum_of_circle)

# User input
radius_of_circle = float(input('Enter the radius of the circle: '))
print(pi * radius_of_circle ** 2)

user_first_name = input("Write your first name: ")
user_last_name = input("Write your last name: ")
user_country = input("Write your country: ")
user_age = input("How old are you?: ")

# Python keywords
help('keywords')

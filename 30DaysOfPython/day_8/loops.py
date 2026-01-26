# --------------------
# Level 1
# --------------------

# 1. Iterate 0 to 10 using for loop
for i in range(11):
    print(i)

# Using while loop
i = 0
while i <= 10:
    print(i)
    i += 1


# 2. Iterate 10 to 0 using for loop
for i in range(10, -1, -1):
    print(i)

# Using while loop
i = 10
while i >= 0:
    print(i)
    i -= 1


# 3. Triangle pattern
for i in range(1, 8):
    print('#' * i)


# 4. Nested loop pattern (8x8)
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()


# 5. Multiplication pattern
for i in range(11):
    print(f"{i} x {i} = {i * i}")


# 6. Iterate through a list
languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for language in languages:
    print(language)


# 7. Print even numbers from 0 to 100
for i in range(0, 101):
    if i % 2 == 0:
        print(i)


# 8. Print odd numbers from 0 to 100
for i in range(0, 101):
    if i % 2 != 0:
        print(i)


# --------------------
# Level 2
# --------------------

# 9. Sum of all numbers from 0 to 100
total = 0
for i in range(101):
    total += i

print("The sum of all numbers is", total)


# 10. Sum of evens and odds from 0 to 100
sum_even = 0
sum_odd = 0

for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print(f"The sum of all evens is {sum_even}. And the sum of all odds is {sum_odd}.")


# --------------------
# Level 3
# --------------------

# 11. Countries containing 'land'
from data.countries import countries

countries_with_land = []

for country in countries:
    if 'land' in country.lower():
        countries_with_land.append(country)

print(countries_with_land)


# 12. Reverse fruits list using loop
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print(reversed_fruits)


# 13. Countries data analysis
from data.countries_data import countries_data

# Total number of languages
languages = set()

for country in countries_data:
    for language in country['languages']:
        languages.add(language)

print("Total number of languages:", len(languages))


# 14. Ten most spoken languages
language_count = {}

for country in countries_data:
    for language in country['languages']:
        language_count[language] = language_count.get(language, 0) + 1

most_spoken_languages = sorted(
    language_count.items(),
    key=lambda x: x[1],
    reverse=True
)[:10]

print("Ten most spoken languages:")
for language, count in most_spoken_languages:
    print(language, count)


# 15. Ten most populated countries
most_populated_countries = sorted(
    countries_data,
    key=lambda x: x['population'],
    reverse=True
)[:10]

print("Ten most populated countries:")
for country in most_populated_countries:
    print(country['name'], country['population'])

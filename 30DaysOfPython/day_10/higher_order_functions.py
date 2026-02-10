from functools import reduce
from collections import Counter

# ================================
# Data
# ================================

countries = [
    'Estonia', 'Finland', 'Sweden',
    'Denmark', 'Norway', 'Iceland'
]

names = ['Asabeneh', 'David', 'Donald', 'Bill']
numbers = [1, 2, 3, 4, 5]


# ================================
# Level 1 – Basics & for loops
# ================================

# Print each country
for country in countries:
    print(country)

# Print each name
for name in names:
    print(name)

# Print each number
for num in numbers:
    print(num)


# ================================
# Level 2 – map()
# ================================

countries_upper = list(map(lambda c: c.upper(), countries))
numbers_squared = list(map(lambda n: n ** 2, numbers))
names_upper = list(map(lambda n: n.upper(), names))

print(countries_upper)
print(numbers_squared)
print(names_upper)


# ================================
# Level 2 – filter()
# ================================

countries_with_land = list(filter(lambda c: 'land' in c.lower(), countries))
six_char_countries = list(filter(lambda c: len(c) == 6, countries))
six_or_more_countries = list(filter(lambda c: len(c) >= 6, countries))
countries_start_e = list(filter(lambda c: c.startswith('E'), countries))

print(countries_with_land)
print(six_char_countries)
print(six_or_more_countries)
print(countries_start_e)


# ================================
# Chaining map → filter → reduce
# ================================

chained_result = reduce(
    lambda a, b: a + b,
    map(lambda x: x ** 2, filter(lambda x: x > 0, numbers))
)

print(chained_result)


# ================================
# Functions
# ================================

def get_string_lists(lst):
    """Return only string items from a list"""
    return list(filter(lambda x: isinstance(x, str), lst))


def categorize_countries(countries, pattern):
    """Return countries containing a specific pattern"""
    return list(filter(lambda c: pattern.lower() in c.lower(), countries))


def countries_by_starting_letter(countries):
    """Return dict of starting letter counts"""
    result = {}
    for country in countries:
        letter = country[0]
        result[letter] = result.get(letter, 0) + 1
    return result


def get_first_ten_countries(countries):
    return countries[:10]


def get_last_ten_countries(countries):
    return countries[-10:]


# ================================
# reduce()
# ================================

# Sum numbers
total_sum = reduce(lambda a, b: a + b, numbers)
print(total_sum)

# Concatenate countries into a sentence
sentence = reduce(
    lambda a, b: a + ', ' + b,
    countries[:-1]
) + f", and {countries[-1]} are north European countries."

print(sentence)


# ================================
# Level 3 – countries_data.py
# ================================

try:
    from countries_data import countries_data

    # Sort by name
    sorted_by_name = sorted(countries_data, key=lambda c: c['name'])

    # Sort by capital
    sorted_by_capital = sorted(countries_data, key=lambda c: c['capital'])

    # Sort by population
    sorted_by_population = sorted(
        countries_data, key=lambda c: c['population']
    )

    # Ten most spoken languages
    languages = Counter(
        lang
        for country in countries_data
        for lang in country['languages']
    )

    ten_most_spoken = languages.most_common(10)

    # Ten most populated countries
    ten_most_populated = sorted(
        countries_data,
        key=lambda c: c['population'],
        reverse=True
    )[:10]

    print(ten_most_spoken)
    print(ten_most_populated)

except ImportError:
    print("countries_data.py not found. Skipping Level 3.")

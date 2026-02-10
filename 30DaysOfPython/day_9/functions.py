# =========================
# MODULE 9 - FUNCTIONS
# =========================

import math

# -------------------------
# LEVEL 1
# -------------------------

def add_two_numbers(a, b):
    return a + b


def area_of_circle(r):
    return math.pi * r * r


def add_all_nums(*nums):
    total = 0
    for num in nums:
        if not isinstance(num, (int, float)):
            return "All arguments must be numbers"
        total += num
    return total


def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def check_season(month):
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return 'Autumn'
    elif month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    else:
        return 'Invalid month'


def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


def solve_quadratic_eqn(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return "No real roots"
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return x1, x2


def print_list(lst):
    for item in lst:
        print(item)


def reverse_list(arr):
    result = []
    for i in range(len(arr) - 1, -1, -1):
        result.append(arr[i])
    return result


def capitalize_list_items(lst):
    return [item.upper() for item in lst]


def add_item(lst, item):
    lst.append(item)
    return lst


def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst


def sum_of_numbers(n):
    return sum(range(n + 1))


def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)


def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)


# -------------------------
# LEVEL 2
# -------------------------

def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = sum(1 for i in range(n + 1) if i % 2 != 0)
    return f"The number of odds are {odds}. The number of evens are {evens}."


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_empty(value):
    return not bool(value)


def calculate_mean(lst):
    return sum(lst) / len(lst)


def calculate_median(lst):
    lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (lst[mid - 1] + lst[mid]) / 2
    return lst[mid]


def calculate_mode(lst):
    return max(set(lst), key=lst.count)


def calculate_range(lst):
    return max(lst) - min(lst)


def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)


def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))


# -------------------------
# LEVEL 3
# -------------------------

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def all_unique(lst):
    return len(lst) == len(set(lst))


def same_data_type(lst):
    return all(type(item) == type(lst[0]) for item in lst)


def is_valid_variable(var):
    return var.isidentifier()


def most_spoken_languages(data, top=10):
    languages = {}
    for country in data:
        for lang in country.get('languages', []):
            languages[lang] = languages.get(lang, 0) + 1
    return sorted(languages.items(), key=lambda x: x[1], reverse=True)[:top]


def most_populated_countries(data, top=10):
    return sorted(data, key=lambda x: x.get('population', 0), reverse=True)[:top]


# =========================
# LIST COMPREHENSION TASKS
# =========================

# 1. Filter only negative and zero values
def filter_negative_and_zero(numbers):
    return [num for num in numbers if num <= 0]


# 2. Flatten list of lists of lists
def flatten_nested_list(nested_list):
    return [num for outer in nested_list for inner in outer for num in inner]


# 3. Create list of tuples
def generate_tuples():
    return [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]


# 4. Flatten countries list and format output
def format_countries(countries):
    return [
        [country.upper(), country[:3].upper(), city.upper()]
        for item in countries
        for country, city in item
    ]


# 5. Convert countries list to list of dictionaries
def countries_to_dict(countries):
    return [
        {'country': country.upper(), 'city': city.upper()}
        for item in countries
        for country, city in item
    ]


# 6. Convert list of lists to concatenated strings
def concatenate_names(names):
    return [
        f"{first} {last}"
        for item in names
        for first, last in item
    ]


# =========================
# LAMBDA FUNCTIONS
# =========================

# Slope of a line
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

# Y-intercept of a line
y_intercept = lambda x, y, m: y - (m * x)


# =========================
# TEST / OUTPUT SECTION
# =========================

if __name__ == "__main__":

    numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
    print(filter_negative_and_zero(numbers))

    list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
    print(flatten_nested_list(list_of_lists))

    print(generate_tuples())

    countries = [
        [('Finland', 'Helsinki')],
        [('Sweden', 'Stockholm')],
        [('Norway', 'Oslo')]
    ]
    print(format_countries(countries))
    print(countries_to_dict(countries))

    names = [
        [('Asabeneh', 'Yetayeh')],
        [('David', 'Smith')],
        [('Donald', 'Trump')],
        [('Bill', 'Gates')]
    ]
    print(concatenate_names(names))

    m = slope(2, 2, 6, 10)
    b = y_intercept(2, 2, m)

    print("Slope:", m)
    print("Y-intercept:", b)

# Module 5: Lists

# Exercise 1

# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
numbers = [1, 2, 3, 4, 5, 6, 7]

# 3. Find the length of the list
print(len(numbers))

# 4. Get first, middle and last items
first_item = numbers[0]
middle_item = numbers[len(numbers) // 2]
last_item = numbers[-1]
print(first_item, middle_item, last_item)

# 5. Mixed data types list
mixed_data_types = ['Yusuf', 26, 1.75, 'Single', 'Nigeria']
print(mixed_data_types)

# 6. IT companies list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list
print(it_companies)

# 8. Number of companies
print(len(it_companies))

# 9. First, middle and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]
print(first_company, middle_company, last_company)

# 10. Modify one company
it_companies[0] = 'Meta'
print(it_companies)

# 11. Add an IT company
it_companies.append('Twitter')
print(it_companies)

# 12. Insert company in the middle
it_companies.insert(len(it_companies) // 2, 'Intel')
print(it_companies)

# 13. Change one company name to uppercase (IBM excluded)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# 14. Join with '#;  '
print('#;  '.join(it_companies))

# 15. Check if a company exists
print('Google' in it_companies)

# 16. Sort list
it_companies.sort()
print(it_companies)

# 17. Reverse list
it_companies.reverse()
print(it_companies)

# 18. Slice first 3 companies
print(it_companies[:3])

# 19. Slice last 3 companies
print(it_companies[-3:])

# 20. Slice middle company/companies
middle_index = len(it_companies) // 2
print(it_companies[middle_index:middle_index + 1])

# 21. Remove first company
it_companies.pop(0)
print(it_companies)

# 22. Remove middle company
it_companies.pop(len(it_companies) // 2)
print(it_companies)

# 23. Remove last company
it_companies.pop()
print(it_companies)

# 24. Remove all IT companies
it_companies.clear()
print(it_companies)

# 25. Destroy the list
del it_companies

# 26. Join front_end and back_end lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

joined_list = front_end + back_end
print(joined_list)

# 27. Copy joined list and insert Python and SQL
full_stack = joined_list.copy()
redux_index = full_stack.index('Redux')

full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')

print(full_stack)

# Module 5: Lists - Level 2

# Given list of ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1. Sort list and find min and max
ages.sort()
min_age = min(ages)
max_age = max(ages)
print("Sorted ages:", ages)
print("Min age:", min_age)
print("Max age:", max_age)

# 2. Add min and max age again
ages.append(min_age)
ages.append(max_age)
print("After adding min and max:", ages)

# 3. Find median age
ages.sort()
length = len(ages)
middle = length // 2

if length % 2 == 0:
    median = (ages[middle - 1] + ages[middle]) / 2
else:
    median = ages[middle]

print("Median age:", median)

# 4. Find average age
average = sum(ages) / len(ages)
print("Average age:", average)

# 5. Find range of ages
age_range = max(ages) - min(ages)
print("Range of ages:", age_range)

# 6. Compare (min - average) and (max - average)
print(abs(min_age - average))
print(abs(max_age - average))

# 7. Find middle country(ies)
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
countries_length = len(countries)
middle_country = countries[countries_length // 2]
print("Middle country:", middle_country)

# 8. Divide countries list into two equal lists
first_half = countries[:countries_length // 2 + 1]
second_half = countries[countries_length // 2 + 1:]
print("First half:", first_half)
print("Second half:", second_half)

# 9. Unpack countries
china, russia, usa, *scandic_countries = countries
print("China:", china)
print("Russia:", russia)
print("USA:", usa)
print("Scandic countries:", scandic_countries)



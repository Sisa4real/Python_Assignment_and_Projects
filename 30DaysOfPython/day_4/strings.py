# Module 4: Strings

# 1. Concatenate strings
string1 = 'Thirty'
string2 = 'Days'
string3 = 'Of'
string4 = 'Python'
result1 = string1 + ' ' + string2 + ' ' + string3 + ' ' + string4
print(result1)

# 2. Concatenate Coding For All
result2 = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(result2)

# 3. Company variable
company = "Coding For All"

# 4. Print company
print(company)

# 5. Length of company
print(len(company))

# 6. Uppercase
print(company.upper())

# 7. Lowercase
print(company.lower())

# 8. Capitalize, title, swapcase
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Slice first word
print(company[7:])

# 10. Check if contains 'Coding'
print(company.find('Coding') != -1)

# 11. Replace Coding with Python
print(company.replace('Coding', 'Python'))

# 12. Change Python for Everyone to Python for All
sentence = "Python for Everyone"
print(sentence.replace('Everyone', 'All'))

# 13. Split string
print(company.split())

# 14. Split at comma
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '))

# 15. Character at index 0
print(company[0])

# 16. Last index
print(len(company) - 1)

# 17. Character at index 10
print(company[10])

# 18. Acronym for Python For Everyone
phrase1 = "Python For Everyone"
acronym1 = ''.join(word[0] for word in phrase1.split())
print(acronym1)

# 19. Acronym for Coding For All
phrase2 = "Coding For All"
acronym2 = ''.join(word[0] for word in phrase2.split())
print(acronym2)

# 20. Index of first C
print(company.index('C'))

# 21. Index of first F
print(company.index('F'))

# 22. rfind of last l
text = "Coding For All People"
print(text.rfind('l'))

# 23. First occurrence of 'because'
sentence2 = "You cannot end a sentence with because because because is a conjunction"
print(sentence2.find('because'))

# 24. Last occurrence of 'because'
print(sentence2.rfind('because'))

# 25. Slice out 'because because because'
start = sentence2.find('because')
end = sentence2.rfind('because') + len('because')
print(sentence2[start:end])

# 26. Starts with Coding
print(company.startswith('Coding'))

# 27. Ends with coding
print(company.endswith('coding'))

# 28. Strip spaces
text_with_spaces = '   Coding For All      '
print(text_with_spaces.strip())

# 29. isidentifier
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# 30. Join list with hash
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))

# 31. New line escape
print("I am enjoying this challenge.\nI just wonder what is next.")

# 32. Tab escape
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# 33. String formatting (circle area)
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# 34. Arithmetic formatting
a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")

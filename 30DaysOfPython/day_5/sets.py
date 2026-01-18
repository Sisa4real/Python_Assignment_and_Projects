# Module 5: Sets

# Given sets and list
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# --------------------
# Level 1
# --------------------

# 1. Length of it_companies
print(len(it_companies))

# 2. Add 'Twitter'
it_companies.add('Twitter')
print(it_companies)

# 3. Insert multiple IT companies
it_companies.update(['Intel', 'Cisco', 'SAP'])
print(it_companies)

# 4. Remove one company
it_companies.remove('Oracle')
print(it_companies)

# 5. Difference between remove and discard
# remove() raises an error if the item does not exist
# discard() does NOT raise an error if the item does not exist

# --------------------
# Level 2
# --------------------

# 6. Join A and B
print(A.union(B))

# 7. Intersection
print(A.intersection(B))

# 8. Subset check
print(A.issubset(B))

# 9. Disjoint check
print(A.isdisjoint(B))

# 10. Join A with B and B with A
print(A.union(B))
print(B.union(A))

# 11. Symmetric difference
print(A.symmetric_difference(B))

# 12. Delete sets
del A
del B

# --------------------
# Level 3
# --------------------

# 13. Convert ages list to set and compare lengths
age_set = set(age)
print("List length:", len(age))
print("Set length:", len(age_set))

# 14. Explanation of data types
print("""
String:
- Ordered
- Immutable
- Stores text

List:
- Ordered
- Mutable
- Allows duplicates

Tuple:
- Ordered
- Immutable
- Allows duplicates

Set:
- Unordered
- Mutable
- Does NOT allow duplicates
""")

# 15. Unique words in a sentence
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)

print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))

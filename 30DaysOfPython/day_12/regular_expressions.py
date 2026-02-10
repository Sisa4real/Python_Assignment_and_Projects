import re
from collections import Counter

# ==============================
# Exercises: Level 1
# ==============================

# 1️⃣ Most frequent words in a paragraph
paragraph = (
    "I love teaching. If you do not love teaching what else can you love. "
    "I love Python if you do not love something which can give you all the "
    "capabilities to develop an application what else can you love."
)

# Clean punctuation and split words
words = re.findall(r'\b\w+\b', paragraph)

word_count = Counter(words)
most_common_words = word_count.most_common()

print("Most frequent words:")
print(most_common_words)
print("Most frequent word:", most_common_words[0])


# 2️⃣ Extract numbers and find distance between furthest particles
text = "The position of particles are -12, -4, -3, -1, 0, 4 and 8"

numbers = list(map(int, re.findall(r'-?\d+', text)))

distance = max(numbers) - min(numbers)

print("\nExtracted points:", numbers)
print("Distance between furthest particles:", distance)


# ==============================
# Exercises: Level 2
# ==============================

# 3️⃣ Check if string is a valid Python variable
def is_valid_variable(variable):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, variable))


print("\nValid variable checks:")
print(is_valid_variable('first_name'))   # True
print(is_valid_variable('first-name'))   # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))    # True


# ==============================
# Exercises: Level 3
# ==============================

# 4️⃣ Clean text and find three most frequent words
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;.
There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple.
;I found tea@ching m%o@re interesting tha@n any other %jo@bs.
%Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(text):
    cleaned = re.sub(r'[^a-zA-Z\s]', '', text)
    return cleaned

def most_frequent_words(text, n=3):
    words = text.split()
    counter = Counter(words)
    return counter.most_common(n)


cleaned_text = clean_text(sentence)
print("\nCleaned text:")
print(cleaned_text)

print("\nThree most frequent words:")
print(most_frequent_words(cleaned_text))

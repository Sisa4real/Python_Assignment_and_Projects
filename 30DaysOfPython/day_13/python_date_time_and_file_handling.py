# =========================
# MODULE: DATETIME
# =========================
from datetime import datetime, timedelta
import time
import json
import re
from collections import Counter
import csv

# 1️⃣ Get current date, time and timestamp
now = datetime.now()
print("Current date & time:", now)
print("Day:", now.day)
print("Month:", now.month)
print("Year:", now.year)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Timestamp:", now.timestamp())

# 2️⃣ Format current date
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted date:", formatted_date)

# 3️⃣ Convert string to datetime
date_str = "5 December, 2019"
date_obj = datetime.strptime(date_str, "%d %B, %Y")
print("Converted datetime:", date_obj)

# 4️⃣ Time difference to New Year
new_year = datetime(now.year + 1, 1, 1)
diff_to_new_year = new_year - now
print("Time until New Year:", diff_to_new_year)

# 5️⃣ Time difference since 1 Jan 1970
epoch = datetime(1970, 1, 1)
diff_from_epoch = now - epoch
print("Time since 1 Jan 1970:", diff_from_epoch)


# =========================
# MODULE: FILE HANDLING
# =========================

# Function to count lines and words in a file
def count_lines_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        lines = text.splitlines()
        words = text.split()
    return len(lines), len(words)

# Example usage (assuming files exist in ./data/)
speeches = [
    'obama_speech.txt',
    'michelle_obama_speech.txt',
    'donald_speech.txt',
    'melina_trump_speech.txt'
]

for speech in speeches:
    try:
        lines, words = count_lines_words(f'./data/{speech}')
        print(f"{speech}: {lines} lines, {words} words")
    except FileNotFoundError:
        print(f"File {speech} not found")


# Function to get most spoken languages from countries_data.json
def most_spoken_languages(filename='./data/countries_data.json', top_n=10):
    with open(filename, 'r', encoding='utf-8') as f:
        countries = json.load(f)
    lang_counter = Counter()
    for country in countries:
        for lang in country.get('languages', []):
            lang_counter[lang] += 1
    return lang_counter.most_common(top_n)


# Function to get most populated countries from countries_data.json
def most_populated_countries(filename='./data/countries_data.json', top_n=10):
    with open(filename, 'r', encoding='utf-8') as f:
        countries = json.load(f)
    sorted_countries = sorted(countries, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:top_n]


# Example usage
try:
    print("\nTop 10 languages:")
    print(most_spoken_languages(top_n=10))

    print("\nTop 3 languages:")
    print(most_spoken_languages(top_n=3))

    print("\nTop 10 populated countries:")
    print(most_populated_countries(top_n=10))

    print("\nTop 3 populated countries:")
    print(most_populated_countries(top_n=3))
except FileNotFoundError:
    print("countries_data.json not found")


# =========================
# Level 2: Extract emails from a file
# =========================
def extract_emails(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}', text)
    return emails

# Example
# emails = extract_emails('./data/email_exchange_big.txt')
# print("Extracted emails:", emails)


# =========================
# Level 2: Most common words in a file
# =========================
def find_most_common_words(filename, n=10):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().lower()
        words = re.findall(r'\b\w+\b', text)
        counter = Counter(words)
    return counter.most_common(n)

# Example
# print(find_most_common_words('./data/sample.txt', 10))
# print(find_most_common_words('./data/sample.txt', 5))


# =========================
# Level 2: Text similarity
# =========================
def clean_text(text):
    return re.sub(r'[^a-zA-Z\s]', '', text).lower()


def remove_support_words(words, stopwords_file='./data/stop_words.txt'):
    with open(stopwords_file, 'r') as f:
        stopwords = f.read().splitlines()
    return [w for w in words if w not in stopwords]


def check_text_similarity(file1, file2, stopwords_file='./data/stop_words.txt'):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = clean_text(f1.read()).split()
        text2 = clean_text(f2.read()).split()

    text1 = set(remove_support_words(text1, stopwords_file))
    text2 = set(remove_support_words(text2, stopwords_file))

    similarity = len(text1.intersection(text2)) / len(text1.union(text2))
    return similarity

# Example
# sim = check_text_similarity('./data/michelle_obama_speech.txt', './data/melina_trump_speech.txt')
# print("Text similarity:", sim)


# =========================
# Level 2: Top repeated words in Romeo & Juliet
# =========================
def top_repeated_words(filename, n=10):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().lower()
        words = re.findall(r'\b\w+\b', text)
        counter = Counter(words)
    return counter.most_common(n)

# Example
# print(top_repeated_words('./data/romeo_and_juliet.txt', 10))


# =========================
# Level 2: Hacker News CSV analysis
# =========================
def hacker_news_analysis(filename):
    python_count = js_count = java_count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        for row in reader:
            line = ' '.join(row)
            if re.search(r'\bpython\b', line, re.I):
                python_count += 1
            if re.search(r'\bjavascript\b', line, re.I):
                js_count += 1
            if re.search(r'\bjava\b', line) and not re.search(r'\bjavascript\b', line, re.I):
                java_count += 1
    return python_count, js_count, java_count

# Example
# python_count, js_count, java_count = hacker_news_analysis('./data/hacker_news.csv')
# print("Python lines:", python_count)
# print("JavaScript lines:", js_count)
# print("Java lines:", java_count)



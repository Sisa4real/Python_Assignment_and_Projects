# =========================
# MODULES
# =========================
import requests
from bs4 import BeautifulSoup
from collections import Counter
import numpy as np

# -------------------------
# 1️⃣ Romeo and Juliet: 10 most frequent words
# -------------------------
def most_frequent_words_from_url(url, n=10):
    response = requests.get(url)
    text = response.text.lower()
    # Remove punctuation
    text = ''.join(c if c.isalpha() or c.isspace() else ' ' for c in text)
    words = text.split()
    counter = Counter(words)
    return counter.most_common(n)

romeo_url = 'http://www.gutenberg.org/files/1112/1112.txt'
print("10 most frequent words in Romeo and Juliet:", most_frequent_words_from_url(romeo_url, 10))


# -------------------------
# 2️⃣ Cats API: Weight & Lifespan Stats
# -------------------------
cats_api_url = 'https://api.thecatapi.com/v1/breeds'

def cats_weight_lifespan_stats():
    response = requests.get(cats_api_url)
    cats = response.json()

    # Extract weight and lifespan
    weight_metric = []
    lifespan_years = []
    countries = []
    breeds = []

    for cat in cats:
        try:
            # weight: "3 - 5" kg -> average it
            w = cat['weight']['metric'].split(' - ')
            avg_weight = (float(w[0]) + float(w[1])) / 2
            weight_metric.append(avg_weight)
        except:
            continue

        try:
            # lifespan: "12 - 15" -> average it
            l = cat['life_span'].split(' - ')
            avg_life = (float(l[0]) + float(l[1])) / 2
            lifespan_years.append(avg_life)
        except:
            continue

        countries.append(cat.get('country_codes', 'Unknown'))
        breeds.append(cat.get('name', 'Unknown'))

    # Weight stats
    weight_array = np.array(weight_metric)
    print("\nCats Weight (kg) Stats:")
    print("Min:", weight_array.min())
    print("Max:", weight_array.max())
    print("Mean:", weight_array.mean())
    print("Median:", np.median(weight_array))
    print("Std Dev:", weight_array.std())

    # Lifespan stats
    lifespan_array = np.array(lifespan_years)
    print("\nCats Lifespan (years) Stats:")
    print("Min:", lifespan_array.min())
    print("Max:", lifespan_array.max())
    print("Mean:", lifespan_array.mean())
    print("Median:", np.median(lifespan_array))
    print("Std Dev:", lifespan_array.std())

    # Frequency table: country and breed
    print("\nCountry & Breed Frequency Table:")
    country_breed_pairs = list(zip(countries, breeds))
    counter = Counter(country_breed_pairs)
    for pair, freq in counter.most_common(10):
        print(pair, ":", freq)

cats_weight_lifespan_stats()


# -------------------------
# 3️⃣ Countries API: Population & Languages
# -------------------------
countries_api_url = 'https://restcountries.com/v3.1/all'

def countries_api_stats():
    response = requests.get(countries_api_url)
    countries = response.json()

    # 10 largest countries by area
    sorted_by_area = sorted(countries, key=lambda x: x.get('area', 0), reverse=True)
    print("\n10 Largest Countries:")
    for c in sorted_by_area[:10]:
        print(c.get('name', {}).get('common'), "-", c.get('area'))

    # Languages stats
    languages_counter = Counter()
    for c in countries:
        langs = c.get('languages', {})
        for lang in langs.values():
            languages_counter[lang] += 1

    print("\n10 Most Spoken Languages:")
    for lang, freq in languages_counter.most_common(10):
        print(lang, ":", freq)

    print("\nTotal number of languages:", len(languages_counter))


countries_api_stats()


# -------------------------
# 4️⃣ UCI ML Repository Scraping
# -------------------------
uci_url = 'https://archive.ics.uci.edu/ml/datasets.php'

def scrape_uci_datasets():
    response = requests.get(uci_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # The tables with datasets have cellpadding="3"
    tables = soup.find_all('table', {'cellpadding': '3'})
    if not tables:
        print("No tables found. UCI page structure may have changed.")
        return

    table = tables[0]
    datasets = []
    for row in table.find_all('tr')[1:]:  # skip header
        cols = row.find_all('td')
        if len(cols) >= 1:
            dataset_name = cols[0].text.strip()
            datasets.append(dataset_name)

    print("\nFirst 20 datasets at UCI ML Repository:")
    print(datasets[:20])

scrape_uci_datasets()

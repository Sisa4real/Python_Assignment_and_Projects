# =========================
# IMPORT REQUIRED LIBRARIES
# =========================
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# =========================
# EXERCISE 1: Scrape BU Facts and Stats
# =========================
def scrape_bu_facts(url='http://www.bu.edu/president/boston-university-facts-stats/'):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    data = {}
    
    # Example: extracting key-value pairs from definition lists or tables
    dl_tags = soup.find_all('dl')
    for dl in dl_tags:
        for dt, dd in zip(dl.find_all('dt'), dl.find_all('dd')):
            key = dt.text.strip()
            value = dd.text.strip()
            data[key] = value
    
    # Save to JSON
    with open('bu_facts.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    
    print("BU facts saved to bu_facts.json")
    return data

# Example usage:
# bu_data = scrape_bu_facts()


# =========================
# EXERCISE 2: Extract UCI ML Datasets Table
# =========================
def scrape_uci_datasets(url='https://archive.ics.uci.edu/ml/datasets.php'):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    tables = soup.find_all('table', {'cellpadding': '3'})
    
    if not tables:
        print("No table found")
        return
    
    table = tables[0]  # first table
    df = pd.read_html(str(table))[0]
    
    # Save as JSON
    df.to_json('uci_datasets.json', orient='records', indent=4)
    print("UCI datasets table saved to uci_datasets.json")
    return df

# Example usage:
# uci_data = scrape_uci_datasets()


# =========================
# EXERCISE 3: Scrape US Presidents Table from Wikipedia
# =========================
def scrape_presidents(url='https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Wikipedia tables usually have class "wikitable"
    tables = soup.find_all('table', {'class': 'wikitable'})
    
    presidents_list = []
    
    for table in tables:
        df = pd.read_html(str(table))[0]  # convert table to dataframe
        presidents_list.append(df)
    
    # Combine all tables if there are multiple
    combined_df = pd.concat(presidents_list, ignore_index=True)
    
    # Save to JSON
    combined_df.to_json('us_presidents.json', orient='records', indent=4)
    print("US Presidents table saved to us_presidents.json")
    return combined_df

# Example usage:
# presidents_df = scrape_presidents()


# =========================
# EXERCISE 4: API Exercises (Example)
# =========================
def get_countries_api(url='https://restcountries.com/v3.1/all'):
    response = requests.get(url)
    data = response.json()
    
    # Save to JSON
    with open('countries_api.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    
    print("Countries API data saved to countries_api.json")
    return data

# Example usage:
# countries_data = get_countries_api()
